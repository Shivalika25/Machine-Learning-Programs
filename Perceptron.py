
import argparse
import csv

#parse the arguments
parser=argparse.ArgumentParser()
parser.add_argument("--data")
parser.add_argument("--output")
args=parser.parse_args()
input=args.data
output=args.output




#open tsv
with open(input,'r') as csv_file, open(output, 'a', encoding='utf8', newline='') as tsv_file: #Read the csv file
    csv_reader1 = csv.reader(csv_file, delimiter='\t')
    num_columns=3
    csv_file.seek(0)
    csv_reader = list(csv_reader1)
    iterationNo = 0

    Data=[]

    for row in csv_reader:
        if (row.count('') > 0):
            row.remove('')

        Data.append(row)
    #Calculate row length
    rowLength=len(Data[0])
    # print(rowLength)
    y1=0
    ww0 = 0
    w = [0] * (num_columns - 1)

    time = 1
    annealing=0
    while(annealing != 2):

        while (iterationNo !=101):
            # print('time',time)
            eta=1
            squaredError = 0
            sumOfSquaredError = 0
            grad0 = float(0)
            gradient1 = [0] * (rowLength - 1)
            missclassified=0
            #iterate through each row
            sample=csv_reader
            for line in sample:

                y1=0

                y1 = y1 + ww0
                for j in range(rowLength -1):
                    y1 += w[j] * float(line[j+1])
                if(y1>0):
                    y1=1
                else:
                    y1=0
                if(line[0]=='A'):
                    y=1
                else:
                    y=0
                if(y!=y1):
                    missclassified=missclassified+1

                error=y-y1
                x0 =1
                gradient =[0]*(rowLength-1)
                #Calculate gradient
                grad0 = grad0 + error*(eta/time)

                for i in range(rowLength - 1):
                    gradient[i] = (eta/time ) * error* float(line[i+1])
                    gradient1[i]=gradient1[i] + gradient[i]
            #Calculate weights
            ww0 = ww0 + float(grad0) #calc w0
            for k in range(num_columns - 1):
                w[k] = w[k] + gradient1[k]
                # print('weights:',w,ww0)
            iterationNo = iterationNo + 1
            miss=str(missclassified)
            if(annealing==1):
                time = time + 1

            # print('missclassified count', str(missclassified))

            # writer=csv.writer(tsv_file)

            tsv_file.write(miss+'\t')
        annealing=annealing+1
        iterationNo=0
        y1 = 0
        ww0 = 0
        w = [0] * (num_columns - 1)
        tsv_file.write('\n')

        # print("annnealing",annealing)





