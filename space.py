print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 8

# Write an if statement below:

if planet == 1:
  gravity = 0.91
  print("You are on Venus")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
elif planet == 2:
  gravity = 0.38
  print("You are on Mars")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
elif planet == 3:
  gravity = 2.34
  print("You are on Jupiter")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
elif planet == 4:
  gravity = 1.06
  print("You are on Saturn")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
elif planet == 5:
  gravity = 0.92
  print("You are on Uranus")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
elif planet == 6:
  gravity = 1.19
  print("You are on Neptune")
  weight_on_planet = weight * gravity
  print("Your weight will be", weight_on_planet)
else:
  print("We dont have the data yet")