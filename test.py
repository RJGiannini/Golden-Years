import csv
import os
import requests
import sys
import fire
import questionary
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
from pathlib import Path
import datetime


def user_amount_savings():  
    """Prompt to input current savings amount"""
    savings_account = []  
    input_savings_account = True  

    while input_savings_account:
        savings = int(input("Please enter the amount you current have in your savings account."))
        if savings > 0:
            print ("Great! We will suggest some investments that have a return over time.")
        else:
            print ("Sorry, we need a valid amount for your savings account.")