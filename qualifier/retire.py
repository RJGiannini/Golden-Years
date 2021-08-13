def retirement_plan (estimated_savings, state_costs):
    """filter out with states and their cost of living comfortably.
    
        args: 
            estimated_savings(float): The customer's expected amount of savings.
            state_cost: The list of available states of where the users wants to live 
    
    QUESTIONS TO ANSWER:
        "WHERE DO YOU WANT TO LIVE/ HOW MUCH DO YOU PLAN OF SAVING."

    Return:
        a list of available state depending on how much the customer has in savings


        """
    state_approval_list=[]

    for state in state_costs:
        if estimated_savings >= float(state[2]):
                state_approval_list.append(state)
    return state_approval_list

