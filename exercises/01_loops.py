"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
#1.
for i in range(1, 11):
    print(i)
#2
#num = 0
#while num <=20:
#    if num % 2 == 0:
#        print(num)
#    num += 1
#or.
for i in range (2, 21, 2):
    print(i)
#3. Calculate the sum of numbers from 1 to 100
num = 0
for i in range(1, 101):
    num += i
print(num)

#4. multiplication table of 5.
for i in range(1, 13):
    print(f"5 x {i} = {i * 5}")
