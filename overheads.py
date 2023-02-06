from pathlib import Path
import csv

def highest_overheads():
    """
    - The function is to find the overhead category with the highest value
    - No parameters are required
    """

    # Create a file path to the overheads csv file
    fp_read = Path.cwd()/"csv_reports"/"overheads.csv"

    # Create an empty dictionary to store the overhead categories and overhead values
    overheads = {}

    # Opens the overheads csv file to extract the overhead categories and overhead values
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        # The csv.reader() function reads the overhead categories and overhead values from the csv file 
        reader = csv.reader(file)
        # The next() function skips reading of the header row 
        next(reader)
        #  Used a for loop to iterate over the other rows aside from header row
        for index in reader:
            # Assigned the overhead categories in the dictionary to a variable called category
            category = index[0]
            # Assigned the overhead values in the dictionary to a variable called amount
            # Converted the string to a float value
            amount = float(index[1])
            # Add the overhead category and its corresponding amount to the overhead dictionary
            overheads[category] = amount

    # The max() function returns the overhead category with the maximum value, and the overheads.get key function 
    # is used to compare the values of the overhead categories in the dictionary
    # The overhead category with the maximum value in the dictionaries is assigned to the highest_category variable 
    highest_category = max(overheads, key=overheads.get)
    
    # The overhead value of the category assigned to the highest_category variable will be assigned to the highest_overhead variable
    highest_overhead = overheads[highest_category]

    # This returns the highest overhead category and its value
    return(f"[HIGHEST OVERHEADS] {highest_category.upper()}: {highest_overhead}%")

# create a file path object for the text file summary_report_txt 
file_path = Path.cwd()/"summary_report.txt"

# Open the text file in mode = "a" which is append mode and encoding= "UTF-8" 
with file_path.open(mode="a", encoding="UTF-8") as file:
    # file. writelines allows the writing of multiple lines of the data in the text file 
    # include "/n" to start a new line for the data  
    file.writelines(highest_overheads() + "\n")

