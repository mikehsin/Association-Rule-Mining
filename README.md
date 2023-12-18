# Association-Rule-Mining - Apriori Association Rule Mining

## Overview
This project focuses on utilizing the Apriori algorithm to generate frequent item sets and derive strong association rules. The main objective is to familiarize users with the process of association rule mining, as outlined in Chapter 6 of the course textbook.

## Dataset
The project uses the “Play_Tennis_Data_Set.csv” file, which includes 14 records across 5 fields: Outlook, Temperature, Humidity, Windy, and PlayTennis. This CSV (Comma-Separated Values) file is structured with a header line followed by data entries, making it ideal for analysis.

## Program Requirements
The program, named “RuleMining”, is designed to:

- Be executed in a command-based interface.
- Prompt the user to enter the minimum support threshold (`min_sup`) and minimum confidence threshold (`min_conf`).
- Calculate the minimum support count by multiplying `min_sup` by the total number of tuples in the dataset and rounding up to the nearest integer.
- Read the “Play_Tennis_Data_Set.csv” file and generate all strong association rules based on the provided thresholds.

## Output
The generated association rules are saved in a file named “Rules.txt” in the same directory as the program. The support and confidence for each rule are rounded to the nearest hundredth.

## Usage
1. Place the “Play_Tennis_Data_Set.csv” in the same directory as the “RuleMining” program.
2. Run the “RuleMining” program.
3. When prompted, input the `min_sup` and `min_conf` values as fractional numbers (e.g., 0.25).
4. The program will process the data and save the resulting rules in “Rules.txt”.

## Testing Instructions
For detailed testing instructions, please refer to the `readme.txt` file provided with the project.

## Appendix
Refer to Appendix 1 at the end of the assignment file for the expected structure of the “Rules.txt” file. The order of the rules is not critical as long as the set of rules is correct.


