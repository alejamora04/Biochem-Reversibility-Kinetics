# Take all of the sample data and plot it using matplotlib
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import combined dataframes into memory to plot
cwd = os.getcwd
plot_path = "reversibility _assay/ouput/csv/combine-out/combined-output.csv"
plate_path = os.join(cwd, plot_path)
sample_plate_df = pd.read_csv(plate_path, index_col[0])
print(sample_plate_df.head)

"""
Create outline for a simple scatter plot from one sample of data in matplotlib
Access Data from Pandas Dataframe

X-axis [Generate List of time points from 0-60 minutes]
Y-axis [Generate list of absorbance values at each time point for a sample]
"""
# X-axis
x_axis = np.arange(0, 60)

# Convert Pandas df Rows into list of values

# DMSO Control Data
DMSO = sample_plate_df.iloc[2, 1:61].values.flatten().tolist()
# No Enzyme control data 
No_Compound = sample_plate_df.iloc[9, 1:61].values.flatten().tolist()
no_compound = sample_plate_df.index[9]

# Format compound
Current_sample = sample_plate_df.ilox[22, 1:61].values.flatten().tolist()
current_sample = sample_plate_df.index[22]

# Plot generated data as line plot.
plt.plot(x, y)
plt.plot(x, y, 'b-', label=compound)
plt.plot(x, No_Compound, 'r-', label=no_compound)
plt.plot(x, Current_sample, 'yo-', label=current_sample)

# As connected scatter plot
plt.plot(x, DMSO, 'bo-', label="DMSO")
plt.plot(x, No_Compound, 'ro-', label=no_compound)
plt.plot(x, Current_sample, 'yo-', label=current_sample)

# Format plot, labels, legends and axis
plt.xlabel('Time [Minutes]')
plt.ylabel('Recorded Absorbance')
plt.title('sample_reversibilitty readout')
plt.legend(loc='upper right')
plt.show

# File output
plot_out_path = "reversibility _assay/ouput/csv/combine-out/combined-output.csv"
plot_path = os.join(cwd, plot_out_path)
plt.save_fig(f"plot_path".png)
print("[+] Plot.py has finished plotting figures. Plots located at:", plot_path)