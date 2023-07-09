import Data_Formatting as format
import plot as plot

# Run all necessary modules to clean data and plot it.
def main():
    # Data_Formatting.py Open a CSV to map sample locations to well on 384 plate. Cleans up readouts
    format.main()
    # plot.py: Loops through cleaned dataframe and generates unique scatterplot for each sample.
    plot.main()

    print("[+] Kinetics modeling has completed all operations.")
    return

if __name__ == '__main__':
    main()