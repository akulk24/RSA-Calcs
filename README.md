# RSA-Calcs
This repository includes Python programs for analyzing solvent accessible surface area (SASA) and relative solvent accessibility (RSA) using MaxASA source values from Rose et al. (1985), Miller et al. (1987), Tien et al. (2013), and SphereCon (open source; 2021).

# Guide to Files per RSA Analysis Method
## SphereCon
ANALYSIS CODE: "spherecon_analysis_code.py" <br>
ORIGINAL FILE with raw SASA and RSA data: "1gsk_spherecon.tsv" <br>
RAW DATA FILE with exposed/buried classifications added (16% and 27% thresholds): "res_class_output.tsv" <br>
EXPOSED/BURIED CLASSIFICATIONS with headers added: "res_class_output_headers.tsv" <br>
TSV INPUT FILE with switch class data: "vis_info_to_add.tsv" <br>
EXPOSED/BURIED CLASSIFICATIONS with headers added merged with switch class data: "spherecon_merged_file" <br>
MERGED FILE with comparison between visual evaluation and 16%/27% thresholds: "spherecon_merged_file_UPDATED.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES: "spherecon_merged_file_UPDATED_with4classes" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with headers added: "spherecon_final.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with column order rearranged: "spherecon_final_columnsrearranged.tsv" <br>

## Tien
ANALYSIS CODE: "tien_analysis_code.py" <br>
ORIGINAL FILE with raw SASA and RSA data: "tien_raw.tsv" <br>
RAW DATA FILE with exposed/buried classifications added (16% and 27% thresholds): "res_class_output.tsv" <br>
EXPOSED/BURIED CLASSIFICATIONS with headers added: "res_class_output_headers.tsv" <br>
B/E FILE with comparison between visual evaluation and 16%/27% thresholds: "tien_file_UPDATED.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES: "tien_file_UPDATED_with4classes" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with headers added: "tien_final.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with column order rearranged: "tien_final_columnsrearranged.tsv" <br>

## Miller
ANALYSIS CODE: "miller_analysis_code.py" <br>
ORIGINAL FILE with raw SASA and RSA data: "miller_raw.tsv" <br>
RAW DATA FILE with exposed/buried classifications added (16% and 27% thresholds): "res_class_output.tsv" <br>
EXPOSED/BURIED CLASSIFICATIONS with headers added: "res_class_output_headers.tsv" <br>
B/E FILE with comparison between visual evaluation and 16%/27% thresholds: "miller_file_UPDATED.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES: "miller_file_UPDATED_with4classes" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with headers added: "miller_final.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with column order rearranged: "miller_final_columnsrearranged.tsv" <br>

## Rose
ANALYSIS CODE: "rose_analysis_code.py" <br>
ORIGINAL FILE with raw SASA and RSA data: "rose_raw.tsv" <br>
RAW DATA FILE with exposed/buried classifications added (16% and 27% thresholds): "res_class_output.tsv" <br>
EXPOSED/BURIED CLASSIFICATIONS with headers added: "res_class_output_headers.tsv" <br>
B/E FILE with comparison between visual evaluation and 16%/27% thresholds: "rose_file_UPDATED.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES: "rose_file_UPDATED_with4classes" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with headers added: "rose_final.tsv" <br>
FILE WITH 4 B/E vs. 1/0 CLASSES with column order rearranged: "rose_final_columnsrearranged.tsv" <br>
