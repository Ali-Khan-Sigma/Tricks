roughStringVar = "this is rough string"
stringVar = "this is string"

if "rough" in roughStringVar:
    e=3
    for var in stringVar:
      print("done with %s"%var)
    print("single char %s" %stringVar[e])

#slice
if "rough" in roughStringVar:
    print(roughStringVar[-12:-7])

#split
fruitNames = "Mango, Bananas, Oranges, Guava"
myStat= "i really love {}, {}, {}, {}"
listHolder = []
stringHolder =None
print(fruitNames.split(','))
for c in fruitNames.split(','):
    listHolder.append(c.strip())
    stringHolder = c.strip()
    print("----%s"%type(listHolder))
    print(stringHolder)
print(myStat.format(stringHolder))
print(listHolder)
#format
# myStat= "i really love {}, {}, {}, {}"
# print(myStat.format(listHolder.split(',')))