#import overheads, cash on hand , profit_loss py files  
import overheads,cash_on_hand,profit_loss

def main():
    """
    - This function modulazes the overheads, profit and loss and cash on hand functions 
    - No parameters are required
    """

    # call the highest.overheads() function from the overheads module 
    overheads.highest_overheads()

    # call the net_profit() function from the profit loss module 
    profit_loss.net_profit()

    # call the cash_difference() function from the cash on hand module
    cash_on_hand.cash_difference()

# execute main function
main()