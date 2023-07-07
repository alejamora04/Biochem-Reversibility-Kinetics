# Loads and 384-well, & sample location into consolidated pandas dataframes
import os
import platform
import pandas as pd
import numpy as np

# File IO Iterate through specified directory to load specified files.
def get_file_paths(path, file_extension):
    file_paths = []
    current_os = platform.system()

    for root, dir, files in os.walk(path, topdown=False):
        for name in files:
            if file_extension in name:
                current_path = os.path.join(root, name)
                if current_os == "Linux":
                    linux_path = current_path.replace('\\', '/')
                    file_paths.append(linux_path)
                elif current_os == "Windows":
                    file_paths.append(current_path)
    print("[+] Retrieved all file paths using get_file_paths function for directory: ", path)
    return file_paths

# Parse all files within directory into list of names.
def get_file_names(file_path):
    file_names = []
    i = 0
    for file in file_path:
        current_file = file_path[i].split("\\")
        current_file = current_file[-1].split(".")
        current_file = current_file[0]
        file_names.append(current_file)
        i = i + 1 
    return file_names

# CSV iterator parses into pandas Dataframe. 
def csv_to_pandas(dataframe, start_position=0):
    condensed_list = []
    consolidated_list = []
    for column in dataframe:
        current_list = dataframe[column].values.tolist()
        condensed_list.append(current_list)

    for i in condensed_list[start_position:]:
        for j in i:
            consolidated_list.append(j)
    return consolidated_list

def main():
    # INPUT: Read layout of 384 well plate format and sample locations into pandas df.
    cwd = os.getcwd()
    # Load 384 plate and sample layout from csv
    plate_path = "/input/plate-maps/"
    plate_well_layout = os.path.join(cwd + plate_path)
    # Load Sample readout data from csv file
    sample_data_path = "input/plate-data/"
    sample_plate_inpath = os.path.join(cwd + sample_data_path)
    file_ext = ".csv"

    # CSVs outlining sample well location and plate layout for each plate.
    parsed_paths = get_file_paths(plate_well_layout, file_ext)
    file_names = get_file_names(parsed_paths)
    # Read Layout of 384 well plate and store it into pd Column
    plate_well_layout = parsed_paths[0]
    sample_layout = parsed_paths[1]
    # Plate Data Readouts
    sample_paths = get_file_paths(sample_plate_inpath, file_ext)
    sample_file_names = get_file_names(sample_paths)

    # [Sample Data Readouts]
    # Delete Extraneuos rows.
    plate_df = pd.read_csv(sample_paths[0], header = None)
    plate_df.drop(index=plate_df.index[0:2], axis = 0, inplace=True)
    plate_df.drop(index=plate_df.index[384], axis = 0, inplace=True)

    # Create a time label for the first row of the dataframe.
    list_label = []
    for i in range(0, 61):
        list_label.append("Abs_min: " + i)

    x = "Well"
    list_label.insert(0, x)

    # Assign list to the column labels
    plate_df.columns=(list_label)
    plate_df.index=np.arange(384)

    # [Well and Sample position manipulations]
    # Read sample position from 384-well plate into Pandas Df 
    sample_location_df = pd.read_csv(sample_layout, header=None)
    consolidated_sample_list = csv_to_pandas(sample_location_df, start_position=1)

    well_layout_df = pd.read_csv(plate_well_layout, header=None)
    consolidated_wells = csv_to_pandas(well_layout_df)

    # Combine Multiple df into single indexed dataframe
    plate_map_df = pd.DataFrame({"Compound": consolidated_sample_list, "Wells": consolidated_wells})
    merged_dataframe = pd.merge(plate_map_df, plate_df, on="Well")
    merged_dataframe["Compound"].replace(" ", np.nan, inplace=True)
    merged_dataframe.dropna(subset=["Compound"], inplace=True)

    # Assign name to dataframe to add pivot table indexing as an option
    merged_dataframe.name = sample_file_names[0] 

    # OUTPUT: Write Output to CSV file 
    out_path = "output/csv/{sample_file_names[0]}_formatted.csv"
    file_out_path = os.path.join(cwd + out_path)

    plate_map_df.to_csv(out_path)
    print("[+] Format_Data.py has mapped the sample locations to the relevant wells and formatted the read data.")

    return

if __name__=='__main__':
    main()