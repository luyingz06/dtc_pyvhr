import yaml
import h5py
import torch
from torch.utils.data import DataLoader, random_split, TensorDataset
from model.PhysFormer import ViT_ST_ST_Compact3_TDC_gra_sharp
import torch.optim as optim
from loss.PhysFormerLossComputer import TorchLossComputer
from train.PhysFormerTrainer import PhysFormerTrainer
torch.cuda.empty_cache()
import torch.utils.checkpoint as checkpoint

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the configuration from the YAML file
with open('/home/luying/dtc_pyvhr/rPPG/configs/physformer.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Load the .h5 file
file_path = 'preprocessed_data.h5'

# Open the file in read mode
with h5py.File(file_path, 'r') as f:
    videos = torch.tensor(f['videos'][:]).to(device)  # Convert to PyTorch tensor
    labels = torch.tensor(f['labels'][:]).to(device)  # Convert to PyTorch tensor
    print(f"Videos shape: {videos.shape}")  # Shape of video data
    print(f"Labels shape: {labels.shape}")  # Shape of label data

# Create TensorDataset directly from loaded data
full_dataset = TensorDataset(videos, labels)

# Split dataset into training and validation
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

# Create DataLoaders
batch_size = 1
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Initialize PhysFormerTrainer
trainer = PhysFormerTrainer(config=config, data_loader={"train": train_loader, "valid": val_loader})
trainer.model.to(device)

# Train the model
trainer.train({"train": train_loader, "valid": val_loader})

# Optionally validate the model after training
validation_loss = trainer.valid({"valid": val_loader})
print(f"Validation Loss: {validation_loss:.4f}")