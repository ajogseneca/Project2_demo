import numpy as np
import pandas as pd

print("\n")
data = {'Course Name': ['BTP', 'BTS', 'BTI', 'BTN'],
        'Course Code': [405, 435, 425, 415],
        'Course Section': ['NBB', 'NBB', 'NBB', 'NBB'],
        'Classes Per Week': [4, 2, 3, 2],}

df = pd.DataFrame(data)

print(df)
print("\n")
print('The mean class per week is :', np.mean(df['Classes Per Week']))
