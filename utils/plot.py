import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the .ods file
df = pd.read_excel('compare_hr.ods', engine='odf')

# Convert the data into lists
heart_rate = df['Heart Rate'].tolist()
pyvhr_1 = df['Pyvhr_1'].tolist()
pyvhr_2 = df['Pyvhr_2'].tolist()
pyvhr_3 = df['Pyvhr_3'].tolist()
mttscan_1 = df['MTTSCAN_1'].tolist()
mttscan_2 = df['MTTSCAN_2'].tolist()
mttscan_3 = df['MTTSCAN_3'].tolist()

# Compute means and standard deviations for pyvhr and mtts_can
pyvhr_means = [np.mean(triplet) for triplet in zip(pyvhr_1, pyvhr_2, pyvhr_3)]
pyvhr_stds = [np.std(triplet) for triplet in zip(pyvhr_1, pyvhr_2, pyvhr_3)]

mtts_means = [np.mean(triplet) for triplet in zip(mttscan_1, mttscan_2, mttscan_3)]
mtts_stds = [np.std(triplet) for triplet in zip(mttscan_1, mttscan_2, mttscan_3)]

# Plotting
x = np.arange(1, len(heart_rate) + 1)

plt.figure(figsize=(12, 6))

# Highlight ±5 bpm area around the ground truth
plt.fill_between(
    x,
    [gt - 5 for gt in heart_rate],
    [gt + 5 for gt in heart_rate],
    color='lightgray',
    alpha=0.5,
    label='Acceptable Range (±5 bpm)'
)

# Plot pyvhr and mtts_can with error bars
plt.errorbar(x, pyvhr_means, yerr=pyvhr_stds, fmt='o-', label='pyvhr', capsize=3, color='blue', alpha=0.8)
plt.errorbar(x, mtts_means, yerr=mtts_stds, fmt='s-', label='mtts_can', capsize=3, color='red', alpha=0.8)

# Plot ground truth
plt.plot(x, heart_rate, 'k--', label='Ground Truth', linewidth=2)

# Labels and legend
plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Heart Rate (bpm)', fontsize=12)
plt.title('Heart Rate Estimation Comparison with Acceptable Range', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()


### Plot high heart rate
high_hr = df[df['Heart Rate'] > 85]
high_hr = high_hr.reset_index(drop=True)
pyvhr_1_high = high_hr['Pyvhr_1'].tolist()
pyvhr_2_high = high_hr['Pyvhr_2'].tolist()
pyvhr_3_high = high_hr['Pyvhr_3'].tolist()
mttscan_1_high = high_hr['MTTSCAN_1'].tolist()
mttscan_2_high = high_hr['MTTSCAN_2'].tolist()
mttscan_3_high = high_hr['MTTSCAN_3'].tolist()

pyvhr_means_high = [np.mean(triplet) for triplet in zip(pyvhr_1_high, pyvhr_2_high, pyvhr_3_high)]
pyvhr_stds_high = [np.std(triplet) for triplet in zip(pyvhr_1_high, pyvhr_2_high, pyvhr_3_high)]

mtts_means_high = [np.mean(triplet) for triplet in zip(mttscan_1_high, mttscan_2_high, mttscan_3_high)]
mtts_stds_high = [np.std(triplet) for triplet in zip(mttscan_1_high, mttscan_2_high, mttscan_3_high)]

x_high = np.arange(1, len(high_hr) + 1)

plt.figure(figsize=(12, 6))

plt.fill_between(
    x_high,
    [gt - 5 for gt in high_hr['Heart Rate']],
    [gt + 5 for gt in high_hr['Heart Rate']],
    color='lightgray',
    alpha=0.5,
    label='Acceptable Range (±5 bpm)'
)

plt.errorbar(x_high, pyvhr_means_high, yerr=pyvhr_stds_high, fmt='o-', label='pyvhr', capsize=3, color='blue', alpha=0.8)
plt.errorbar(x_high, mtts_means_high, yerr=mtts_stds_high, fmt='s-', label='mtts_can', capsize=3, color='red', alpha=0.8)

plt.plot(x_high, high_hr['Heart Rate'], 'k--', label='Ground Truth', linewidth=2)

plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Heart Rate (bpm)', fontsize=12)
plt.title('Heart Rate Estimation Comparison with Acceptable Range (High HR)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()
