# Take all of the sample data and plot it using matplotlib
import os
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import Data_Formatting as format

# TODO: Perform curve fitting to classify readouts as reversible(FAST, SLOW, IRREVERSIBLE)

# Take the average Abs data readout for the control samples. Combine data from multiple samples.
def avg_pd_rows(pd_dataframe):
    avg_readout = []
    for i in range(60):
        data = pd_dataframe["Abs_Min: "+ str(i)].values.flatten().tolist()
        Avg_Calc = statistics.mean(data)
        avg_readout.append(Avg_Calc)
    return avg_readout

def main():
    # File IO
    # [INPUT] Load formatted and cleaned csv to plot
    cwd = os.getcwd
    plot_path = "/ouput/csv/"
    plate_path = os.path.join(cwd + plot_path)
    file_ext = ".csv"

    # Parse file paths and names refer to Data_Formatting.py for function details
    plot_data_paths = format.get_file_paths(plate_path, file_ext)
    plot_names = format.get_file_names(plot_data_paths)
    formatted_plate = plot_data_paths[0]
    plate_name = plot_names[0]

    sample_plate_df = pd.read_csv(formatted_plate, index_col=[1])

    """

    [Scatter Plot Outline]

    X-axis: Generate List of time points from 0-60 minutes
    Y-axis: Read plate absorbance data at each time point for a sample
    DMSO [+] Ctrl: Average DMSO value readouts for plot data.
    No Enzyme [-] Ctrl: Format no enzyme control.


    """
    x_axis = np.arange(0, 60)

    # Convert Pandas df Rows into list of values

    # [DMSO] Extract DMSO readouts into smaller df
    DMSO_df = sample_plate_df.loc["DMSO"]
    DMSO_Avg = avg_pd_rows(DMSO_df)

    # [No Enzyme] control data 
    No_Compound_df = sample_plate_df.loc["no enzyme"]
    No_Enzyme_Avg = avg_pd_rows(No_Compound_df)

    # Drop [+ & -] Controls to extract sample information
    Compound_df = sample_plate_df.drop["DMSO", "no enzyme"]
    
    # [OUTPUT] Path for generated plots
    out_path = "/output/plots/"
    plot_path = os.path.join(cwd + out_path)

    i = 0
    for i in range(len(Compound_df)):
        current_sample_ro = Compound_df.iloc[i, 2:62].values.flatten().tolist()
        current_sample_label = Compound_df.index[i]
        sample_well = Compound_df.iloc[i, 0]

        # Plot generated data
        plt.clf()
        plt.plot(x_axis, DMSO_Avg, 'bo-', label="DMSO n=15")
        plt.plot(x_axis, No_Enzyme_Avg, 'ro-', label="no_compound n=13")
        plt.plot(x_axis, current_sample_ro, 'yo-', label= current_sample_label)

        # Format plot, labels, legends and axis
        plt.xlabel('Time [Minutes]')
        plt.ylabel('Recorded Absorbance')
        plt.title(plate_name)
        plt.legend(loc='upper right')
        #plt.show()

        # [Checkpoint] Check generated plots
        plt.savefig(f"{plot_path}Well({sample_well})_Sample_{current_sample_label}.png")
        i = i + 1
    
    print("[+] Plot.py has finished plotting figures. Plots located at:", plot_path)
    return

if __name__ == '__main__':
    main()