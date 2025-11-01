budget = float(input())
price_per_1kg_flour = float(input())
price_1pack_eggs = 0.75 * price_per_1kg_flour
price_1L_milk = (0.25 + 1) * price_per_1kg_flour
milk_price = price_1L_milk / 4
loaf_price = milk_price + price_1pack_eggs + price_per_1kg_flour
number_of_loaves = 0
colored_eggs = 0
money_left = budget

while money_left >= loaf_price:
    money_left -= loaf_price
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")