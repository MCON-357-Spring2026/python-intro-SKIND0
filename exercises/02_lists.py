"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is the length of the corresponding food item in the original list.
"""

#1.
fav_foods = ["apple", "pear", "cherry"]

#2.
print(fav_foods[0])
print(fav_foods[2])
#3.
fav_foods.append("orange")

#4.
fav_foods.remove("apple")

#5.
for food in fav_foods:
    print(food)

#6.
lengths = []
for food in fav_foods:
    lengths.append(len(food))
print(lengths)
