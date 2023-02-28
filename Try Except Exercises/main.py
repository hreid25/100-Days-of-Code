
height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("That height is not valid.")

bmi = weight/height ** 2
print(bmi)

