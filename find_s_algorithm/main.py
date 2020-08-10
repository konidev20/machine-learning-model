#Find S Algorithm [Concept Learning]
import csv

#data
data = []

with open('dataset/data.csv','rt') as input_data:
    data_buffer = csv.reader(input_data)
    for row in data_buffer:
        data.append(row)

no_of_attr = len(data[0])-1

#general hypothesis
g = ['?' for i in range(0,no_of_attr)]

print("initial Most General hypotheis g = ",g,"\n")

hypothesis = ['phi' for i in range(0,no_of_attr)]

print("Initial Most Specific hypothesis h(0) = ",hypothesis)
print(" ")
#Comparing with the first data point
for i in range(0,no_of_attr):
    hypothesis[i] = data[0][i]

print("Positive Training Example No.{0} = ".format(1),data[0])
print("Hypothesis h({0}) = ".format(1),hypothesis)
print(" ")
#Starting Find S Algorithm
for i in range(1,len(data)):
    #considering only the positive samples
    print("Training Example No.{0} = ".format(i+1),data[i])
    if data[i][no_of_attr] == "Yes":
        print("\tPositive")
        for j in range(0,no_of_attr):
            if data[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = data[i][j]
    else:
        print("\tNegative")
    print("Hypothesis h({0}) = ".format(i+1),hypothesis)
    print(" ")

print("The maximal specific hypothesis for the given data = ",hypothesis)
