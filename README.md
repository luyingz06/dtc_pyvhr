# dtc_pyvhr

This is the virtual heart rate detection code for DARPA Triage Challenge (Team Pronto).

It takes in frames extracted from rosbags and process them through heart rate estimation algorithms.

## Two methods
- Conventional computation using model-based method CHROM.
It analyzes the color signals in G channel (from RGB camera) and calculate BVP and BPM.
Return heart rate as an integer.

- Deep learning models and gives out the final estimation.
It takes in frames and return heart rate as an integer.
