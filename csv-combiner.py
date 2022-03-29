"""
Task: PMG coding challenge:csv combiner

Description: This is a python program that takes several CSV files as arguments.
Each CSV file (found in the fixtures directory of this repo) will have the same columns.
This script will output a new CSV file to stdout that contains the rows from each of the
inputs along with an additional column that has the filename from which the row came
(only the file's basename, not the entire path). Use filename as the header for the additional column.

Author: Yuexin(Cindy) Chen
I add inline comments for each step I did. Please let me know if you have any questons about them.
Thank you so much for your time and consideration.
"""
import sys
import os
import pandas as pd

class csv_c:
    def combine_files(self, combine_files: list):
        # check if we are missing input
        if len(combine_files) <= 1:
            print("ERROR: missing input file name")
            return False

        # remove the first element because it stores the current file name
        # the remaining arguments are our input file names
        combine_files = combine_files[1:]

        # check if all the input files exist
        list1 = []
        for file in combine_files:
            list1.append(os.path.isfile(file))

        if all(list1):
            # concatenate multiple files
            # reference: https://www.youtube.com/watch?v=V0KxE6AfodM
            all_df = []
            for f in combine_files:
                # read in one input file
                df = pd.read_csv(f, sep=',')
                # append the source file name to the last column as 'filename'
                df['filename'] = f.split('/')[-1]
                # append the dataframe to a temp list
                all_df.append(df)

            # merge dataset using pandas package function
            merged_df = pd.concat(all_df, ignore_index=True)

            # check if the columns are correct after concatenation
            # print(merged_df.columns)

            # final stdout output: output the merged datasets
            print(merged_df)
            return True
        else:
            print("ERROR: Input file list contain invalid file names. Please check. ")
            print(combine_files)
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create a class object for csv combiner
    combiner = csv_c()
    # call the function to concatenate files
    combiner.combine_files(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
