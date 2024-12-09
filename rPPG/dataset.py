import os
import cv2
import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import h5py  # For efficient storage
cv2.setNumThreads(0)

class VideoDataset(Dataset):
    def __init__(self, video_path, gt, frame_size=None, max_frames=300):
        """
        Custom dataset for loading videos and labels.

        Args:
            video_path (str): Path to the directory containing videos.
            gt (str): Path to the CSV file that contains labels and video names.
            frame_size (tuple): Desired height and width of video frames. If None, keep original size.
            max_frames (int): Maximum number of frames to extract per video.
        """
        self.frame_size = frame_size
        self.max_frames = max_frames
        self.video_path = video_path

        # Read CSV and map video names to ground truth
        self.data = pd.read_csv(gt)
        self.video_names = self.data['Name'] + '.avi'
        self.labels = self.data['Average Heart Rate'].astype(float)

    def __len__(self):
        return len(self.video_names)

    def __getitem__(self, idx):
        video_name = self.video_names[idx]
        label = self.labels[idx]

        video_file = os.path.join(self.video_path, video_name)
        if not os.path.exists(video_file):
            print(f"Warning: Video file {video_file} not found. Skipping...")
            return None, None
        
        # Read video and process frames
        cap = cv2.VideoCapture(video_file)
        frames = []
        while len(frames) < self.max_frames:
            ret, frame = cap.read()
            if not ret:
                break
            if self.frame_size:
                frame = cv2.resize(frame, self.frame_size)  # Resize each frame
            frame = torch.tensor(frame, dtype=torch.float32).permute(2, 0, 1) / 255.0  # Normalize to [0, 1]
            frames.append(frame)

        cap.release()
        
        # Check if any frames were read
        if not frames:
            print(f"Warning: No frames read for video {video_file}. Skipping this video.")
            return None, None

        # Pad or truncate to max_frames
        if len(frames) < self.max_frames:
            pad_frames = [torch.zeros_like(frames[0]) for _ in range(self.max_frames - len(frames))]
            frames.extend(pad_frames)
        elif len(frames) > self.max_frames:
            frames = frames[:self.max_frames]

        video_tensor = torch.stack(frames, dim=0)  # Shape: (T, C, H, W)

        return video_tensor, torch.tensor(label, dtype=torch.float32)

# Define paths and parameters
video_path = '/home/luying/dtc_pyvhr/rPPG/videos'
gt = '/home/luying/dtc_pyvhr/rPPG/train/DTC.csv'
frame_size = (224, 224)  # Resize to 224x224
max_frames = 300
batch_size = 8
output_file = 'preprocessed_data.h5'  # Use HDF5 format for more efficient saving

# Create dataset and dataloader
dataset = VideoDataset(video_path, gt, frame_size=frame_size, max_frames=max_frames)

with h5py.File(output_file, 'w') as f:
    # Create a dataset for storing video frames and labels
    video_data = f.create_dataset('videos', (0, max_frames, 3, 224, 224), maxshape=(None, max_frames, 3, 224, 224), chunks=(batch_size, max_frames, 3, 224, 224))
    label_data = f.create_dataset('labels', (0,), maxshape=(None,), chunks=(batch_size,))

    for i in range(len(dataset)):
        video, label = dataset[i]
        if video is None:
            print(f"Skipping video at index {i} due to missing data.")
            continue
        
        print(f"Processing video at index {i}: {video.shape}, label: {label}")
        
        # Resize each frame and convert back to tensor (this section seems to be outside the loop, adjust accordingly)
        if frame_size:
            if video is not None:
                video = torch.stack([torch.tensor(cv2.resize(frame.permute(1, 2, 0).numpy(), frame_size), dtype=torch.float32).permute(2, 0, 1) / 255.0 for frame in video])

        # Append to HDF5 datasets
        video_data.resize((video_data.shape[0] + 1, video_data.shape[1], video_data.shape[2], video_data.shape[3], video_data.shape[4]))
        label_data.resize((label_data.shape[0] + 1,))
        video_data[-1] = video
        label_data[-1] = label

        # Print progress
        if i % 100 == 0:
            print(f"Processed {i}/{len(dataset)} videos.")
    
    print("Preprocessing completed and data saved.")


# Load the .h5 file
file_path = 'preprocessed_data.h5'

# Open the file in read mode
with h5py.File(file_path, 'r') as f:
    # List all datasets in the file
    print("Datasets in the file:")
    print(list(f.keys()))
    
    # Assuming the file contains two datasets: 'videos' and 'labels'
    if 'videos' in f and 'labels' in f:
        # Load the entire datasets (note: these are large, so consider reading in chunks if necessary)
        videos = f['videos'][:]
        labels = f['labels'][:]
        
        # Print the shape and type of the datasets
        print(f"Videos shape: {videos.shape}")  # Shape of the video data (e.g., (num_samples, T, C, H, W))
        print(f"Labels shape: {labels.shape}")  # Shape of the label data (e.g., (num_samples,))
        print(f"First label: {labels[0]}")  # Print the first label value
        print(f"First video shape: {videos[0].shape}")  # Shape of the first video (e.g., (T, C, H, W))
        print(f"First frame of the first video: {videos[0][0]}")  # Print the first frame of the first video
    else:
        print("No 'videos' or 'labels' dataset found.")