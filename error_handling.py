x = 4
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Division by Zero is not allowed')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
