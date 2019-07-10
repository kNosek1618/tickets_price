
import random
age = random.randint(1,100)

print("the customer's age is: "+ str(age))

if age >=1 and age <=8:
    print("he must pay 2 dollars.")
elif age >= 9 and age <= 65:
    print("he must pay 10 dollars.")
else:
    print("he must pay 5 dollars.")