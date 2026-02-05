"""
TODO:
Dictionary of students -> grades
Print averages
"""
Students = {"Alice": 98, "Bella": 86, "Candy": 85, "Destiny": 92, "Eva": 100}

average = 0
for k, v in Students.items():
    average += v
    print(k, v)
average = average / len(Students)
print(f"Average: {round(average, 2)}")

