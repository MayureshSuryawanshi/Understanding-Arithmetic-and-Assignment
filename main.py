# Mayuresh Suryawanshi 2/24/2024
# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
profit = 0
salePrice = 0
saleProfit = 0

# Write your assignment statements here for profit, salePrice, and saleProfit
profit = retailPrice - wholesalePrice
salePrice = retailPrice - (retailPrice * 0.25)
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))