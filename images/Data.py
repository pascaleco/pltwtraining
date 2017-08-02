import os.path
import matplotlib.pyplot as plt
import numpy as np
#this is to get the data set
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'Data(1).csv')
datafile = open(filename, 'r')
data = datafile.readlines()

genders = []
races = []
for line in data[1:]:
    gender, race = line.split(',')
    if gender == "Male":
        genders.append(1)
    elif gender == "Female":
        genders.append(2)
        
for line in data[1:]:
    gender, race = line.split(',')
    if "White" in race:
        races.append(1) 
    elif "Hispanic" in race:
        races.append(2)
    elif "Black" in race:
        races.append(3)
    elif "Unknown" in race:
        races.append(4)
    elif "Asian" in race:
        races.append(5)
    else:
        races.append(6)

fig, ax = plt.subplots(1,1)
n, bins, patches = plt.hist(genders, bins=np.arange(0, 6, 1), align='left', color='b')
patches[2].set_fc('r')

plt.title("Accidental Drug Related Death in CT 2012-2016 by Gender")
plt.xlabel("Gender: Male (Blue) & Female (Red)")
plt.ylabel("Frequency")
fig.canvas.draw()
fig.show()

fig2, ax = plt.subplots(1,1)
n, bins, patches = plt.hist(races, bins=np.arange(1, 8, 1), align='left', color='b')
patches[0].set_fc('r')

plt.title("Accidental Drug Related Death in CT 2012-2016 by Race")
plt.xlabel("Race: 1(White), 2(Hispanic), 3(Black), 4(Unknown), 5(Asian), 6(Other)")
plt.ylabel("Frequency")
fig2.show()