#testing github desktop functionality
#will add detail to app throughout day

import csv
from pathlib import Path
from qualifier.fileio import load_csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.retire import retirement_plan
from qualifier.comfort import comfort_buffer

#write a code that will prompt the user to answer the questions "Where do you plan to live and how much are you planning to save by 65"


def save_csv(csvpath,state_plan ):

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["State","Cost of Living","Comfort Buffer","Comfortable Retirement"])
        for row in state_plan:
            csvwriter.writerow(row)


def csv_prompt():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The US retirement data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    state = questionary.text("Which State do you want to live in?").ask()
    savings = questionary.text("How much do you plan to save by 65?").ask()


    State = str(state)
    savings = float(savings)
    return State, savings

