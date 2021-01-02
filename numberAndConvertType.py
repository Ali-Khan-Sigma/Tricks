import random

intValues = 145
floatValues = 4.555

print(intValues)
print(floatValues)

#type conversion
convertToInt = int(floatValues)
convertToFloat = float(intValues)

print(convertToInt)
print(convertToFloat)

rand = random.randrange(convertToInt, intValues)
print(rand)