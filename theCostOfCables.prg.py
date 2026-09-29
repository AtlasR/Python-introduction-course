print ('Welcome to The Cost of Cables')

# configuring string data
feet_of_cable = float(input("Enter the amount of cable per ft"))

feet_of_cable = float(feet_of_cable)
costOfCable = feet_of_cable * .87
 

if (feet_of_cable > 500):
    costOfCable = float(feet_of_cable) * .50
elif (feet_of_cable > 250):
    costOfCable = float(feet_of_cable) * .70
elif (feet_of_cable > 100):
    costOfCable + float(feet_of_cable) * .80
else:
    costOfCable = float(feet_of_cable) * .80
'''
if (feet_of_cable > 500):
cost_of_cable = float(feet_of_cable) * .50
if (feet_of_cable > 250):
cost_of_cable = float(feet_of_cable) * .70
if (feet_of_cable > 100):
    cost_of_cable + float(feet_of_cable) * .80
else:
    cost_of_cable = feet_of_cable * .87
'''

#message = ' The cost of your Cables is: ' + str(costOfCable) + ' for installing ' + str(costOfCable) + ' feet of cable.'
message = f'The cost is {costOfCable} for installing {feet_of_cable} feet of cable'
print(message)