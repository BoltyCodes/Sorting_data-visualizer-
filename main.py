
import matplotlib.pyplot as plt
import numpy as np
import random



data = []

for i in range(0,50):
    data.append(random.randint(0,100))


for i in range(0,len(data)):
    for r in range(0,len(data)-i-1):
        if data[r] > data[r+1]:
            temp = data[r]
            data[r] = data[r+1]
            data[r+1] = temp


half_data = data[:len(data)//2]
full_data = data[len(data)//2:]



#plotting time!

x = np.array([data])
y = np.array([data])



fig = plt.figure(figsize = (50,50))

    
plt.bar(half_data,full_data,color = "green",width = 0.8)
    


    

 
