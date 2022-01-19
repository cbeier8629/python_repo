print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
percentage_tip = int(input(
    'What percentage tip would you liuke to give? 10, 12,or 15?'))
people = int(input('How many people to split the bill?'))

bill_with_tip = percentage_tip / 100 * bill + bill

print(bill_with_tip)


# tip = bill * percentage_tip/100
# total_bill = bill + tip
# print(f"tip: ${tip}")
# print(f"Total Cost: ${total_bill}")
