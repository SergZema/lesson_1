"""
квадраты чётных чисел от нуля до десяти

"""

squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]

squares_cube = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]

print(squares_odds)
print(squares_cube)