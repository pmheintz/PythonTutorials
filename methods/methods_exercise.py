"""
Exercise:
Create a method, which takes the state and gross income as the
arguments and returns the net income after deducting tax based
on the state.
Assume federal tax is 10%
Assume state tax is 5%, 6%, 7%
"""
# Federal tax rate
fed_tax_rate = .1
# Dictionary of select state tax rates
state_tax_rate = {'WI': .05, 'IL': .06, 'NY': .09}

def calculateIncome(state, gross_pay):
    """
    Calculates net income after taxes
    :param state: The state the income was earned in
    :param gross_pay: Pay before taxes
    :return: Net income
    """
    # Calculate federal tax
    fed_tax = gross_pay * fed_tax_rate
    # Calculate state tax
    if state in state_tax_rate:
        state_tax = gross_pay * state_tax_rate[state]
    # Return error if state not in list
    else:
        return "Unable to calculate. State tax is not in the list"
    # Return net pay
    return gross_pay - fed_tax - state_tax

print("Your income in Wisconsin is: " + str(calculateIncome('WI', 100000)))
print("Your income in Illinois is: " + str(calculateIncome('IL', 100000)))
print("Your income in Texas is: " + str(calculateIncome('TX', 100000)))
print("Your income in New York is: " + str(calculateIncome('NY', 100000)))