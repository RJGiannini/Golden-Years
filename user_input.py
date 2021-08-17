
#imports
import csv
from pathlib import Path
import sys
import fire
import questionary
from datetime import datetime

from data.retire import retirement_plan
from data.comfort import comfort_buffer
from data.americanstates import fifty_states


###### Below are all the code that are for the API#######
# Call current market price for user 
def eth_api():
    eth_crypto = print("")
    return eth_crypto

def btc_api():
    btc_crypto = print("Code here")
    return btc_crypto

def fb_stock():
    fb = print("Code for API here")
    return fb

def amazon_stock():
    amazon = print("Code for API here")
    return amazon

def apple_stock():
    apple = print("Code for API here")
    return apple

def netflix_stock():
    netflix = print("Code for API here")
    return netflix

def google_stock():
    google = print("Code for API here")
    return google

###### ------ ########

#write a code that will prompt the user to answer the questions "Where do you plan to live and how much are you planning to save by 65"
def prompting_user_state():
    """ Prompt user to choose from a list of fifty states where they currently live to get started.
    
        Return: "Great, this how much you need to live comfortably in this (State)____($x)"""
    
    prompt_fifty_states = questionary.select("Select the state you live in to get started",choices=fifty_states).ask()
   
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
        investment_stock_crypto()
    else:
        pose_investment()
        


def pose_investment():
    push_investment = questionary.confirm("Would you like to view investment options anyway?").ask()
    if push_investment:
        investment_stock_crypto()
    else: 
        print ("Thank you for your time.Goodbye")


def investment_stock_crypto():
    """Prompt user to start with crypto or stocks to view (first).
    
        Return either crypto or stock"""

    stock_crypto = questionary.select("Select either 'Stock', 'Crypto', or both to get started",choices=["Crypto","Stocks", "Stocks and Crypto"]).ask()
    if stock_crypto == "Crypto":
        crypto_api()
    else:
        stock_api()
    
def crypto_api():
    """This is a segway into crpyto API and Monte Carlo
        Return information on crypto"""
    crypto_btc_eth = questionary.select ("Crypto is a great to start saving. Select a crypto to continue:",choices =["ETH","BTC"]).ask()
    if crypto_btc_eth == "ETH":
        eth_api()
    else:
        btc_api()

    
def stock_api():
    """This is a segway into the Monte Carlo/API.
        Return: Monte Carlo/API"""

    stock_faang = questionary.select("Please select a company to begin:",choices= ["Facebook","Amazon","Apple","Netflix","Google"]).ask()
    if stock_faang == "Facebook":
        fb_stock()
    elif stock_faang == "Amazon":
        amazon_stock()
    elif stock_faang == "Apple":
        apple_stock()
    elif stock_faang == "Netflix":
        netflix_stock()
    else:
        google_stock()

def run():
    #load CSV file
    data = prompting_user_state()
    print (data)
    data = investment_choice()
if __name__=="__main__":
    fire.Fire(run)

