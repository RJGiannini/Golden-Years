

#testing github desktop functionality
#will add detail import csv
import csv
from pathlib import Path
import sys
import fire
import questionary

from qualifier.retire import retirement_plan
from qualifier.comfort import comfort_buffer
from qualifier.americanstates import fifty_states


#write a code that will prompt the user to answer the questions "Where do you plan to live and how much are you planning to save by 65"
def prompting_user_state():
    """ Prompt user to choose from a list of fifty states to get started.
    
        Return: "great, this how much you need to live comfortably in (State)____($x)"""
    
    prompt_fifty_states = questionary.select("Select a state to get started",choices=fifty_states).ask()
   
    return "Great, this how much you need to live comfortably in " + prompt_fifty_states + " $" + comfortability_cost(prompt_fifty_states)

def comfortability_cost(comfort_state):
    """Display comfortability per state"""
    stateDic = {}
    with open("./Resources/us_retirement_data.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            stateDic[row[0]] = row[3]
    return stateDic[comfort_state]

def investment_choice():
    """ Ask user if they plan to invest to increase savings.
    
        Return either: yes or no. if no, return to the beginning, if yes, continue with choices.
    """
    investment_q = questionary.confirm("Do you plan to invest to increase your savings?").ask()
    if investment_q:
        data = investment_stock_crypto()
        print (data)
    else:
        run()
        


def investment_stock_crypto():
    """Prompt user to start with crypto or stocks to view (first).
    
        Return either crypto or stock"""

    stock_crypto = questionary.select("Select either 'Stock' or 'Crypto' to get started",choices=["Crypto","Stocks"]).ask()
    return "Sounds like an amazing choice, you've selected "+ stock_crypto
    



def run():
    #load CSV file
    data = prompting_user_state()
    print (data)
    data = investment_choice()
if __name__=="__main__":
    fire.Fire(run)

