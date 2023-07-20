"""
PROBLEM STATEMENT: Write a program in any language of your choice 
to accept the free time of all the Technical core member and print the most suitable time ( in which maximum members are free).

MY APPROACH: 
- How would you go on and collect the data? -> ideally google forms or something similar (and the club used it too)
- OK, so lets make a google form with time-slots, I did, values of timeslots would be between 7:00pm to 11:30 (thats when everyone is free and 
    when the committee members said they hold most meetings)
- Generated Dummy responses using a script (I didn't do this myself though :>, haven't learnt a web automation library YET (working on it...))
- Download the csv and USE THE BEST OPTION EVER FOR DATA - **PANDAS** and python
- import the data, get the best value, plot it to flex extra hard (makes sense too, to look at the variation of responses) 

SIDE NOTE:
Problem statement is redundant because google forms already gives the relevant dat, (pie chart form)
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# importing and cleaning data
df = pd.read_csv('responses.csv')
df = df.rename(columns={'What time suits you best for *WORK*!!!!!!!':'Slot'})

# Extracting our target value
max_freq = df['Slot'].value_counts().index
print(f'Ideal time-slot: {max_freq[0]}')

# Plotting (I like looking at graphs)
sns.countplot(x='Slot', data=df, order=max_freq)
plt.xticks(rotation=45)
plt.show()

