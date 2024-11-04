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













