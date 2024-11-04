# 1. 3D Convolutional Neural Networks for Remote Pulse Rate Measurement and Mapping from Facial Video

## Main Innovation: 
A new framework: 3D convolutional neural network and concurrent mapping.

## Background: 
Photoplethysmography consists in indirect observation of blood volume variations by measuring absorption and reflection of light on skin tissues. 

Motion is to the main limitation of PPG or BCG methods. BCG methods are more affected by natural motion than PPG methods and are more prone to noise and artifacts when larger distance are considered.

Deriving pulse rate from video recordings generally follows four basic procedures: (1) video recording; (2) image processing, i.e., selection of relevant pixels of interest (e.g., face and/or skin detection), channel combination, and color space conversion; (3) signal processing (e.g., band-pass filtering based on Fourier or wavelet transform); (4) biomedical parameter extraction (e.g., pulse rate, pulse rate variability, SpO2).

In CNN, different trainable filters followed by pooling operations are applied on input images, they are quite invariant to pose and lighting variations. 

# 2. A Broader Look: Camera-Based Vital Sign Estimation across the Spectrum

From bandpass-Filtering to Machine and Deep learning.

Since 2016, the “average publication” on camera-based vital sign estimation is made of a laboratory study including about 20 subjects, filmed with an industrial-grade or laboratory RGB camera under ambient light conditions Since 2016, the “average publication” on camera-based vital sign estimation is made of a laboratory study including about 20 subjects, filmed with an industrial-grade or laboratory RGB camera under ambient light conditions.

# 3. Architectural Tricks for Deep Learning in Remote Photoplethysmography

## Scenarios:
Stationary scenarios and Mixed Motion scenarios. Three different cameras.

## Methods:
CNN model. Feature extraction(conv layers) - HR prediction - Filtering.
Color signals as inputs, heart rate(40-125bpm integer) as labels.Regression and classification tasks. Squared error for regression and cross entropy for classification. 

# 4. A deep learning approach for remote heart rate estimation

## Innovation:
Proposed a method based on the Long Short Term Memory (LSTM) deep neural network.
While maintaining the accuracy comparable to ICA and POS algorithms, the LSTM network works well also beyond the visible spectrum, e.g., with infrared lighting when the color signal is not available and is easily adaptable to telemedicine applications.
Also works in grayscale.

## Process
ROI selection - raw color signal extraction - VPG signal extraction (G, ICA, POS, ExG) - VPG signal postprocessing (band-pass filtering) - pulse rate estimation.

# 5. Chaos in Motion: Unveiling Robustness in Remote Heart Rate Measurement through Brain-Inspired Skin Tracking

## Innovation
Apply chaos theory to computer vision.

Design a robust motion-aware remote heart rate measurement framework, which can accurately
identify skin ROI and be applied to body parts other than the face, making it applicable for special patients and addressing privacy protection concerns.

ROI extraction: continuous coupled neural network (CCNN).

Filter G-channel, conduct time-frequency analysis. 

## non-facial experiments

In addressing subject privacy, we conducted remote heart rate experiments on six non-facial
body parts, reducing individual identifiable information. These parts included the palm, back of the hand, forearm, upper arm, back, and sole.

limited skin color

# 6. Deep Learning Methods for Remote Heart Rate Measurement: A Review and Future Research Agenda

Discuss advances of DL-based methods.

rPPG methods utilize signal processing techniques to separate the specular reflections and extract the diffuse reflections associated with the underlying signals of interest.

2D CNN - 3D CNN - 2D CNN + RNN - NAS - Attention

More importantly, new methods should provide insight into how these challenges are handled from a technical and biophysical perspective, rather than just evaluating their performance on a dataset that contains the influencing factors.

Other challenges, such as skin-tone variations, multiple persons detection, and long distance estimations, need to be overcome.

# 7. More Reliable Remote Heart Rate Measurement by Signal Quality Indexes





