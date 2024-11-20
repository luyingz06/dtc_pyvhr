# dtc_pyvhr

This is the virtual heart rate detection code for DARPA Triage Challenge (Team Pronto).

It takes in frames extracted from rosbags and process them through heart rate estimation algorithms.

## Two methods
- Conventional computation using model-based method CHROM.
It analyzes the color signals in G channel (from RGB camera) and calculate BVP and BPM.
Return heart rate as an integer.

- Deep learning models and gives out the final estimation.
It takes in frames and return heart rate as an integer.

## Todo

Test on existing data using pyvhr pipeline and give estimated results vs ground truth (Nov. 20th - Nov. 24th).

Utilize deep learning model after the image preprocess (skin extraction) and get results (Nov. 24th - Nov. 28th).

Train new deep neural network models (Further schedule).
