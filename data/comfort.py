def comfort_buffer (estimated_savings, state_costs):
    """filter out with states and their cost of living comfortably.
    
        args: 
            estimated_savings(float): The customer's expected amount of savings.
            state_cost: The csv/list of available state of where to the customer want to live
    
    QUESTIONS TO ANSWER:
        "WHERE DO YOU WANT TO LIVE/ HOW MUCH DO YOU PLAN OF SAVING."

    Return:
        a list of available state depending on how much the customer has in savings


        """
    comfort_buffer=[]

    for state in state_costs:
        if estimated_savings >= float(state[3]):
                comfort_buffer.append(state)
    return comfort_buffer

