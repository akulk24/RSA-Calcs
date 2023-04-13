import csv

# Set the delimiter to tab ('\t')
delimiter = '\t'

# Open the input file
with open('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/1gsk_spherecon.tsv', 'r') as infile:
    reader = csv.reader(infile, delimiter=delimiter)
    # Open the output file
    with open('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/res_class_output.tsv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=delimiter)
        # For each row in the input file
        next(infile) # skip first line of file when comparing
        for row in reader:
            # Determine if the value in the 2nd column is greater than 0.16
            if float(row[1]) > 0.16:
                # If so, add a new column with the value "Exposed"
                row.append("Exposed")
                # If less than 0.16, add "Buried" in the cell
            else:
                row.append("Buried")
            # Determine if the value in the 2nd column is greater than 0.27
            if float(row[1]) > 0.27:
                # If so, add a new column with the value "Exposed"
                row.append("Exposed")
                # If less than 0.27, add "Buried" in the cell
            else:
                row.append("Buried")
            # Write the modified row to the output file
            writer.writerow(row)

### ADDING HEADERS

header = ["Residue", "SphereCon Value", "Buried/Exposed (RSA = 16%)", "Buried/Exposed (RSA = 27%)"]  # list of header column names

with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/res_class_output.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t")
    rows = [row for row in reader]  # read all rows into a list

with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/res_class_output_headers.tsv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerow(header)  # write the header row first
    writer.writerows(rows)  # write the rest of the rows

### MERGING OUTPUT FILE WITH OTHER FILE CONTAINING BONDUGULA SWITCH CLASS AND MY VIS B/E CLASSIFICATIONS

# Load the two TSV files
with open('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/res_class_output_headers.tsv', 'r') as file1, open('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/vis_info_to_add.tsv', 'r') as file2:

    # Create CSV reader objects
    reader1 = csv.reader(file1, delimiter='\t')
    reader2 = csv.reader(file2, delimiter='\t')

    # Create a list of rows for each file
    rows1 = [row for row in reader1]
    rows2 = [row for row in reader2]

    # Merge the rows by concatenating them horizontally
    merged_rows = [row1 + row2 for row1, row2 in zip(rows1, rows2)]

# Write the merged rows to a new TSV file
with open('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file.tsv', 'w') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    writer.writerows(merged_rows)

### COMPARING MY VIS TO 16%/27% THRESHOLDS FOR SPHERECON

# open the TSV file and read its contents into a list
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t")
    rows = [row for row in reader]
    # next(infile) # skip first line of file when comparing
# iterate over the rows and compare the two columns
for row in rows:
    if row[2] == row[4]:
        row.append("True")
    else:
        row.append("False")
    if row[3] == row[4]:
        row.append("True")
    else:
        row.append("False")

# write the updated data to a new TSV file
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file_UPDATED.tsv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows(rows)

## ADDING NEW COLUMNS (FOR 16% AND 27%) FOR SWITCH VS. B/E CLASSIFICATION

# open the TSV file and read its contents into a list
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file_UPDATED.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t")
    rows = [row for row in reader]
    # next(infile) # skip first line of file when comparing
# iterate over the rows and compare the two columns
for row in rows:
    if row[2] == "Exposed" and row[5] == 0:
        row.append("Exposed and Not a Switch")
    elif row[2] == "Exposed" and row[5] == 1:
        row.append("Exposed and a Switch")
    elif row[2] == "Buried" and row[5] == 0:
        row.append("Buried and Not a Switch")
    else:
        row.append("Buried and a Switch")
    if row[3] == "Exposed" and row[5] == 0:
        row.append("Exposed and Not a Switch")
    elif row[3] == "Exposed" and row[5] == 1:
        row.append("Exposed and a Switch")
    elif row[3] == "Buried" and row[5] == 0:
        row.append("Buried and Not a Switch")
    else:
        row.append("Buried and a Switch")

# write the updated data to a new TSV file
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file_UPDATED_with4classes.tsv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows(rows)

### ADDING HEADERS FOR THE NEW COLUMNS

header = ["Residue", "SphereCon Value", "Buried/Exposed (RSA = 16%)", "Buried/Exposed (RSA = 27%)", "Exposed/Buried Based on Vis.", "Bondugula Switch Class", "Matches Up with Vis? (16%)", "Matches Up with Vis? (27%)", "Switch vs. B/E (16%)", "Switch vs. B/E (27%)"]  # list of header column names

with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file_UPDATED_with4classes.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t")
    rows = [row for row in reader]  # read all rows into a list

with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_final.tsv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerow(header)  # write the header row first
    writer.writerows(rows)  # write the rest of the rows

# THEN manually delete row 2 of spherecon_final.tsv to only keep updated headers

### REARRANGE COLUMN ORDER

import csv

# define the desired column order
desired_order = ["Residue", "SphereCon Value", "Buried/Exposed (RSA = 16%)", "Matches Up with Vis? (16%)", "Buried/Exposed (RSA = 27%)", "Matches Up with Vis? (27%)", "Exposed/Buried Based on Vis.", "Bondugula Switch Class", "Switch vs. B/E (16%)", "Switch vs. B/E (27%)"]

# open the input TSV file and read its contents into a list
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_final.tsv", "r") as infile:
    reader = csv.DictReader(infile, delimiter="\t")
    rows = [row for row in reader]

# create a new list of rows with the desired column order
new_rows = []
for row in rows:
    new_row = {col: row[col] for col in desired_order}
    new_rows.append(new_row)

# write the updated data to a new TSV file with the desired column order
with open("/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_final_columnsrearranged.tsv", "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, delimiter="\t", fieldnames=desired_order)
    writer.writeheader()
    writer.writerows(new_rows)


