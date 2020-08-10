import csv

data = []

#reading data from the csv file
with open ("dataset/data.csv","r") as input_data:
    reader = csv.reader(input_data)
    for row in reader:
        data.append(row)

na = len(data[0])-1 #the number of attributes

#Initial specific and general hypothesis
S = ['0'] * na
print("S[0] = ",S)

G = ['?'] * na
print("G[0] = ",G)

#taking the first training example
for i in range(0,na):
    S[i] = data[0][i]

print("For example {0} the S[{0}]".format(1),S)
print("For example {0} the G[{0}]".format(1),G)
#applying candidate elimination

print("Applying Canidate elimination hypothesis version space....")

G_SET = []

for i in range(1,len(data)):

    #For a positive training example
    if data[i][na] == "Yes":
        for j in range(0,na):
            if data[i][j] != S[j]:
                S[j] = '?'

        #candidate elimination
        for j in range(0,na):
            for k in range(0,len(G_SET)):
                if G_SET[k][j] != '?' and G_SET[k][j] != S[j]:
                    del G_SET[k]

        print("For example {0} the S[{0}]".format(i+1),S)

        if(len (G_SET)== 0):
            print("For example {0} the G[{0}]".format(i+1),G)
        else:
            print("For example {0} the G[{0}]".format(i+1),G_SET)

    else:
        for j in range(0,na):
            #if it doesn't match with specific hypothesis store it separately
            if data[i][j] != S[j] and S[j] != '?':
                G[j] = S[j]
                G_SET.append(G)
                G = ['?'] * na
        print("For example {0} the S[{0}]".format(i+1),S)
        print("For example {0} the G[{0}]".format(i+1),G_SET)
