import csv
import pandas as pd

def print_messages():
    colnames = ['probability', 'Predict', 'flag', 'id', 'Text']
    data = pd.read_csv('output.csv',names=colnames)

    flags = data.flag.tolist()
    message = data.Text.tolist()

    output = []

    for i in range(1,len(flags)):
        if int(flags[i]) > 0:
            output.append(message[i])
    return(output)

if __name__ == '__main__':
    for i in print_messages():
        print(i)