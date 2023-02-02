from pathlib import Path 
import csv 
 
def cash_difference(): 
#     """ 
#     - This function calculates any difference in the net profit column of the cash on hand csv file  
#     - if the net profit of the current day is lower than the day before that 
#     - No parameters required  
#     """ 
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
                return(f"[CASH DEFICIT] DAY: {number + 85} AMOUNT: USD{difference}") 
 
        # use else statement if there is not any cash deficit throughout all the 6 days    
        else: 
 
            # return statement of cash surplus and each day is higher than its previous 
            return(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
            
file_path = Path.cwd()/"summary_report.txt"
with file_path.open(mode="a", encoding="UTF-8") as file:
    file.writelines(cash_difference() + "\n")


