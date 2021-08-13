import csv

def retirement_plan (state_name, state_costs):
    """filter out with states and their cost of living comfortably.
    
    
    QUESTIONS TO ANSWER:
        "WHERE DO YOU WANT TO LIVE/ HOW MUCH DO YOU PLAN OF SAVING."

    Return:
        the chosen state


        """
    state_name=[]

    for state in state_costs:
        if estimated_savings >= float(state[2]):
                state_approval_list.append(state)
    return state_approval_list

