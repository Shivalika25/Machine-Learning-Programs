
import argparse
import csv


parser=argparse.ArgumentParser()
parser.add_argument("--data")
parser.add_argument("--threshold")
parser.add_argument("--learningRate")
args=parser.parse_args()
print('args data:',args.data)
threshold=float(args.threshold)
learningRate=float(args.learningRate)




with open(args.data,'r') as csv_file:
    csv_reader1 = csv.reader(csv_file,delimiter=',')
    num_columns=len(next(csv_reader1))
    csv_file.seek(0)


    rowCounter = 0
    csv_reader = list(csv_reader1)
    isThreshold=True

    iterationNo = 0

    prevSum = 0
    y1=0
    ww0 = 0
    w = [0] * (num_columns - 1)

    while (isThreshold):

        squaredError = 0
        sumOfSquaredError = 0
        grad0 = float(0)
        gradient1 = [0] * (num_columns - 1)

        sample=csv_reader
        for line in sample:

            y1=0



            y=float(line[num_columns-1])

            y1 = y1 + ww0
            for j in range(num_columns - 1):
                # y1 = float(0)
                y1 += float(w[j]) * float(line[j])

            error=y-y1


            x0 =1
            gradient =[0]*(num_columns-1)

            grad0 = grad0 + error



            for i in range(num_columns - 1):
                gradient[i] = (float(line[i]) * float(error))
                gradient1[i]=gradient1[i] + gradient[i]

            squaredError = error * error

            sumOfSquaredError = sumOfSquaredError + squaredError

        print('iteration {} Weights {}'.format(iterationNo, ww0), sep=' ', end='')
        for i in range(num_columns-1):
            print(' {} '.format(w[i]), sep=' ', end='')

        print('sum',sumOfSquaredError)

        if(abs(sumOfSquaredError - prevSum) <= threshold):
            isThreshold=False
        prevSum = sumOfSquaredError
        if(isThreshold == False):
            break
        ww0 = ww0 + learningRate * float(grad0)
        for k in range(num_columns - 1):
            w[k] = float(w[k]) + learningRate * float(gradient1[k])

        iterationNo += 1











