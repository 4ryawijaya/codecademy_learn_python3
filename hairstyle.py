hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

new_prices = [price + 5 for price in prices]
print(new_prices)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print("Cuts under 30:", cuts_under_30)

total_price = 0
total_revenue = 0
num_purchase = len(prices)
num_hairstyles = len(hairstyles)

for price in prices:
  total_price += price
print(total_price)

average_price = total_price / num_purchase
print("Average Haircut Price", average_price)

for i in range(0, num_hairstyles):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average daily revenue:", average_daily_revenue)


