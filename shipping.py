weight = 41.5
service = "GROUND SHIPPING"
flat_cost = 20
flat_cost_premium = 125
drone_cost = 0
price = 0

#GROUND SHIPPING CONDITION
if service == "GROUND SHIPPING":
  if weight <= 2:
    price += weight * 1.5 + flat_cost
  elif weight >= 2 and weight <= 6:
    price += weight * 3.0 + flat_cost
  elif weight >= 6 and weight <= 10:
    price += weight * 4.0 + flat_cost
  else:
    price += weight * 4.75 + flat_cost

#GROUND SHIPPING PREMIUM
elif service == "GROUND SHIPPING PREMIUM":
    price += flat_cost_premium
  
#DRONE SHIPPING
elif service == "DRONE SHIPPING":
  if weight <= 2:
    price += weight * 4.5 + drone_cost
  elif weight >= 2 and weight <= 6:
    price += weight * 9.0 + drone_cost
  elif weight >= 6 and weight <= 10:
    price += weight * 12.0 + drone_cost
  else:
    price += weight * 14.25 + drone_cost

print("For the weight: " + str(weight) + ' and with the service of ' + service + ' total cost will be: $ ' + str(price))

#What is the cheapest method of shipping a 4.8 pound package 
#and how much would it cost?
"""
For the weight: 4.8 and with the service of GROUND SHIPPING total cost will be: 34.4
For the weight: 4.8 and with the service of GROUND SHIPPING PREMIUM total cost will be: 125.0
For the weight: 4.8 and with the service of DRONE SHIPPING total cost will be: 43.199999999999996
"""


#What is the cheapest method of shipping a 41.5 pound package 
#and how much would it cost?
"""
For the weight: 41.5 and with the service of GROUND SHIPPING total cost will be: 217.125
For the weight: 41.5 and with the service of GROUND SHIPPING PREMIUM total cost will be: 125.0
For the weight: 41.5 and with the service of DRONE SHIPPING total cost will be: 591.375
"""