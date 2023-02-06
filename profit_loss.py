from pathlib import Path
import csv 

def net_profit(): 
    """ 
    - This function calculates any difference in the net profit column of the profit and loss csv file  
    - if the net profit of the current day is lower than the day before that, it would shows net deficit for those days 
    - if the net profit of the current day is higher than the day before that for that whole period, it would show net profit surplus 
    - no parametres required 
    """ 
    # Create a file path to the profit and loss csv file
    fp_read = Path.cwd()/"csv_reports"/"profit_and_loss.csv" 

    # Create an empty list to store the net profit for day 85-90 
    net_profit_list= [] 
 
    # Opens the profit_and_lost csv file to extract the data for day 85-90 
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file: 
        
        # The csv.reader() function reads the "Day","Sales","Trading Profit","Operating Expense","Net Profit" 
        # for each day from day 85-90 from the csv file 
        reader = csv.reader(file)  
        # The next() function skips reading of the header row   
        next(reader)   
 
        # Used a for loop to iterate over the other rows aside from header row    
        for index in reader: 

            # use int() to covert the net profit values from a string into a integer   
            # use .append() and indexing to add the net profit values into the empty list                                 
            net_profit_list.append(int(index[4])) 

        # use len() to get total number of items in list
        # use a for loop and range() to iterate loop within the six days  
        for number in range(1,len(net_profit_list)): 

        # use if statement to check if the current day net profit is smaller than the previous day net profit     
         if net_profit_list[number] < net_profit_list[number-1]: 

            # calculate the difference of the current day net profit the previous day net profit 
            difference = net_profit_list[number] - net_profit_list[number-1]
            # use abs() to convert the difference value from a negative into a positive integer
            difference = abs(difference)

            # return statement of the day when the profit deficit occurs and the amount of profit deficit in USD
            return(f"[PROFIT DEFICIT] DAY: {number + 85}, AMOUNT: USD{difference}") 
         
        # use else statement if there is not any profit deficit throughout all the 6 days  
        else:
            # return statement "net profit surplus and each day is higher than its previous day"  
            return(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 

# create a file path object for the text file summary_report_txt
file_path = Path.cwd()/"summary_report.txt"

# Open the text file in mode = "a" which is append mode and encoding= "UTF-8" 
with file_path.open(mode="a", encoding="UTF-8") as file:
    # file. writelines allows the writing of multiple lines of the data in the text file 
    # include "/n" to start a new line for the data  
    file.writelines(net_profit() + "\n")
