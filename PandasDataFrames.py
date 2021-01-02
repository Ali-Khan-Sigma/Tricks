# playing with pandas data frames

dInput = {"country": ["Brazil", "Russia", "China", "South Africa"],
          "capital": ["Brasilia", "Moscow", "Beijing", "Pretoria"],
          "area": [8.516, 17.10, 9.597, 1.221],
          "population": [200.4, 143.5, 1357, 52.98]}

#for k,v in dInput.items():
#    print("your key: {0}\t and your value {1}".format(k, v))

import pandas as pd

temp=pd.DataFrame(dInput)
print(temp)