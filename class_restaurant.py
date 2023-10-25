class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    rep = "You can reach our place at {}. See you there!".format(self.address)
    return rep

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    rep = "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)
    return rep

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
      else:
        ValueError("We don't have the menu.")
    return bill

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}


brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
kids_menu = Menu("Kids", kids_items, 1100, 2100)
arepas_menu = Menu("Arepa", arepas_items, 1000, 2000)


brunch_purchase = brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])
# print(brunch_purchase)
early_purchase = early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
# print(early_purchase)

menu = [brunch_menu, early_bird_menu, dinner_menu, kids_menu, arepas_menu]

flagship_store = Franchise("1232 West End Road", menu)
new_installment = Franchise("12 East Mulberry Street", menu)
arepas_place = Franchise("89 Fitzgerald Avenue", menu)
# print(arepas_place.available_menus(2000))

franchise_list = [flagship_store, new_installment, arepas_place]

Basta = Business("Basta Fazoolin' with my Heart", franchise_list)
Arepa = Business("Take a' Arepa", franchise_list)

print(Arepa.franchises[0].menus[4])















