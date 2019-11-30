import csv
import numpy as np
import pandas as pd
import math
import sys as s
file_path = s.argv[1]
output_path = s.argv[2]
dataframe=pd.read_csv(file_path,header=None)

# output_path="/Users/shivalika/PycharmProjects/MLAssignment2/Assignment2write.xml"

rows,columns=dataframe.shape
g2=dataframe.groupby(columns-1).size()

test=dataframe.groupby(dataframe[dataframe.columns[columns-1]])
headers=list(dataframe.columns.values)

headers.remove(columns-1)
uniqueValues=dataframe[columns-1].value_counts()





def getEntropyagain(dataframe):
    Entropy=0
    Entropy1=0
    groupByClass=dataframe.groupby(columns-1)
    countRows=0
    rowArray=[]
    i=0
    for val,data in groupByClass:
        feature=val
        row,col=data.shape
        rowArray.append(row)

        countRows=countRows+row

    for i in range(len(rowArray)):
        # print(rowArray[i])
        Entropy= abs(((rowArray[i]/countRows)*(math.log(rowArray[i]/countRows,len(uniqueValues)))))
        Entropy1=Entropy1+Entropy
    # print('leaf',val)
    # print('Tree Node Entropy:',Entropy1)

    return Entropy1


def informationGain(dataframe,Entropy)   :
    # print(("new info func"))
    GainArray=[]
    for i in headers:
         infoGain = 0.00
         feature= ""
         g = dataframe.groupby(dataframe[dataframe.columns[i]])
         proportion = []
         featureEntropy=[]
         ArrayOfGroupedByclass=[]

         for feature, data in g:
             total=0

             TotalCountOfFeatures = 0
             prevFeature=feature

             groupedDataByClass = data.groupby(data.columns[columns-1])
             ArrayOfGroupedByclass.append(groupedDataByClass)
             classCount = []
             k=0
             for valueInGrouped, dataInGrouped in groupedDataByClass:
                 noOfRows,noOfColumns=dataInGrouped.shape
                 classCount.append(noOfRows)

                 if(prevFeature == feature):
                     # TotalCountOfFeatures=noOfRows
                     TotalCountOfFeatures=TotalCountOfFeatures+noOfRows
                     # print("totalcount::",TotalCountOfFeatures)

             calcEntropy=getEntropyagain(data)
             # print("Entropy Feature",calcEntropy)




             featureEntropy.append(calcEntropy)
             # print('Feature entropy:',featureEntropy)

             proportion.append(TotalCountOfFeatures/rows)
             #print('proportion:',proportion)

         for k in range(len(proportion)):
             infoGain =infoGain+ proportion[k]*featureEntropy[k]
             # print('Gain',infoGain)
         Gain=Entropy-infoGain
         GainArray.append(Gain)
         # print('next column--------')
         #print('features---',feature)
    maxGain=max(GainArray)


    rootNode=GainArray.index(maxGain)
    uniqueValues=dataframe[rootNode].value_counts()
    return rootNode


def decisionTree(dataframe):
    # iterNo=0

    Entropy=getEntropyagain(dataframe)
    rootNode = informationGain(dataframe, Entropy)
    # print("RootNode in decision tree", rootNode)

    groupbyroot=dataframe.groupby(rootNode, sort=False)
    for val,data in groupbyroot:
        Entrop = getEntropyagain(data)
        # print("Node value", val)
        # print("Entropy", Entrop)
        # print('value going',val)
        file_op.write('<node entropy="' + str(Entrop) + '" feature="att' + str(rootNode) + '" value="' + str(val) +
                      '">')

        if Entrop == 0.0:
            # print("Leaf Node:",val)
            file_op.write(str(data[columns - 1].unique()[0]))
            # break #leaf node
        else:
            nodes_to_ignore.add(rootNode)
            # attr_parent = informationGain(data,)

            decisionTree(data)

        file_op.write("</node>")


entropy_tree = getEntropyagain(dataframe)

nodes_to_ignore = set()
nodes_to_ignore.add(columns-1)
file_op = open(output_path, 'w')
file_op.write('<tree entropy="' + str(entropy_tree) + '">')
decisionTree(dataframe)
file_op.write('</tree>')







































