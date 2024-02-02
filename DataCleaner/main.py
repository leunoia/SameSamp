import csv
import re
import os

# rootdir = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/DataCleaner/'
# dirty_file_path = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/DataCleaner/dirtycsvs/'
# clean_file_path = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/DataCleaner/cleancsvs/'

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         #print os.path.join(subdir, file)
#         filepath = subdir + os.sep + file

#         if filepath.endswith(".csv"):
#             print (filepath)

input_file = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/DataCleaner/dirtycsvs/the_champ.csv'
output_file = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/DataCleaner/cleancsvs/the_champ_cleaned.csv'

def extract_year(text):
    match = year_regex.search(text)
    if match:
        return match.group(1)
    else:
        return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Regular expression to match a year in parentheses
    year_regex = re.compile(r'\((\d{4})\)')


    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Iterate over each row in the input file
        for row in reader:
            # Check if the row has at least 5 columns
            if len(row) >= 5:
                # Extract the year from the fifth column (0-indexed)
                year = extract_year(row[4])

                # If a year is found, update the fifth column
                if year is not None:
                    row[4] = year

            # Write the updated row to the output file
            writer.writerow(row)

    print('CSV file processing complete.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
