from pathlib import Path 
import csv 
 
def cash_difference(): 
    """ 
        - This function calculates any difference in the cash on hand column of the cash on hand file  
        - if the cash on hand of the current day is lower than the day before that, it would show cash deficit for those days 
        - if the cash on hand of the current day is higher than the day before that for that whole period, it would show cash surplus 
        - No parameters required  
    """ 
    # Create a file path to the cash on hand csv file 
    fp_read = Path.cwd()/"csv_reports"/"cash_on_hand.csv" 
 
    # Create an empty list to store the cash on hand for day 85-90 
    cash_on_hand_list= [] 
     
    # Opens the cash_on_hand csv file to extract the cash on hand for day 85-90 
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file: 
        # The csv.reader() function reads the value of the cash on hand for each day from day 85-90 and from the csv file  
        reader = csv.reader(file) 
 
        #The next() function skips reading of the header row  
        next(reader)    
 
        # Used a for loop to iterate over the other rows aside from header row                          
        for index in reader:  
 
            # use int() to covert the cash on hand values from a string into a integer   
            # use .append() to add the cash on hand values into the empty list               
            cash_on_hand_list.append(int(index[1])) 
 
        # use len() to get total number of items in list 
        # use a for loop and range() to iterate loop within the six days  
        for number in range(1,len(cash_on_hand_list)): 
 
            # use if statement to check if the current day cash on hand is smaller than the previous day cash on hand  
            if cash_on_hand_list[number] < cash_on_hand_list[number-1]: 
 
                # calculate the difference of the current day cash on hand and the previous day cash on hand 
                difference = cash_on_hand_list[number]-cash_on_hand_list[number-1] 
 
                # use abs() to convert the difference value from a negative into a positive integer  
                difference = abs(difference) 
 
                # return statement of the day when the cash deficit occurs and the amount of cash deficit in USD  
                return(f"[CASH DEFICIT] DAY: {number + 85:.1F}, AMOUNT: USD{difference}") 
 
        # use else statement if there is not any cash deficit throughout all the 6 days    
        else: 
 
            # return statement "cash surplus and each day is higher than its previous day" 
            return(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
          
# create a file path object for the text file summary_report_txt 
file_path = Path.cwd()/"summary_report.txt"

# Open the text file in mode = "a" which is append mode and encoding= "UTF-8" 
with file_path.open(mode="a", encoding="UTF-8") as file:
    # file. writelines allows the writing of multiple lines of the data in the text file 
    # include "/n" to start a new line for the data  
    file.writelines(cash_difference() + "\n")


