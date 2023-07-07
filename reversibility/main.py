import Data_Formatting as format
import plot as plot

# Run all necessary modules to clean data and plot it.
def main():

    format.main()
    plot.main()

    print("[+] Kinetics modeling has completed all operations.")
    return

if __name__ == '__main__':
    main()