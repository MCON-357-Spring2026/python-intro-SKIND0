# Demonstration of defining and using functions in Python
# Defining a simple function
def greet(name):
    return f"Hello, {name}"
print(greet("Alice"))


#function with different types of parameters
def process(a:int=0, b:str="default_value", *args, **kwargs) -> None:
    print(f"a: {a}, b: {b}")
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

process(10, "test", 1, 2, 3, {"key1": "value1", "key2": "value2"})
process(args=(4, 5), kwargs={"key3": "value3"})

# Using a lambda function - anonymous function
my_lambda = lambda x: x * 2
print(my_lambda(5))
# Using lambda with map function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)
# Using lambda with filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
# Using lambda with sorted function
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print("Points sorted by y-coordinate:", sorted_points)

