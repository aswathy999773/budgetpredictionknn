import csv


dpt=[]
dpd=[]
dfn=[]
dsn=[]

# opening the CSV file
i=0
x=[]
y=[]
# with open(r'C:\django\budgetprediction\static\budgetdataset.csv', mode ='r')as file:
with open(r'C:\Users\aswat\Downloads\budgetprediction\budgetprediction\static\budgetdataset.csv', mode ='r')as file:

# reading the CSV file

    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        if i!=0:
            print(lines[3],lines[4],lines[5],lines[6],lines[11])
            if lines[3].lower() not in dpt:
                dpt.append(lines[3].lower())
            if lines[4].lower() not in dpd:
                dpd.append(lines[4].lower())
            if lines[5].lower() not in dfn:
                dfn.append(lines[5].lower())
            if lines[6].lower() not in dsn:
                dsn.append(lines[6].lower())
            try:
                op=int(lines[11])
                print(op,"****************=====================")

                if op<= int(500000):
                    y.append(0)
                elif op<= int(1000000):
                    y.append(1)
                elif op<= int(5000000):
                    y.append(2)
                elif op<= int(25000000):
                    y.append(3)
                elif op <= int(50000000):
                    y.append(4)
                elif op <= int(100000000):
                    y.append(5)
                elif op <= int(150000000):
                    y.append(6)
                else:
                    y.append(7)

                x.append([lines[3].lower(),lines[4].lower(),lines[5].lower(),lines[6].lower()])
            except Exception as e:
                print("1234567",e)
                print(lines[11])

        i=i+1
X=[]
for i in x:
    row=[dpt.index(i[0]),dpd.index(i[1]),dfn.index(i[2]),dsn.index(i[3])]
    X.append(row)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.10)

# Remember that we are trying to come up
# with a model to predict whether
# someone will TARGET CLASS or not.
# We'll start with k = 1.

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(pred, "+++++++++++++++++++++++++++++++")
# Predictions and Evaluations
# Let's evaluate our KNN model !
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred))

print(classification_report(y_test, pred))

def knn_predict(i):
    print(i)
    row =[]
    try:
        print(dpt)
        print(i[0])
        print("====================================")
        row.append(dpt.index(i[0].lower()))
    except:
        row.append(-1)
    try:
        print(dpd)
        print(i[1])
        print("====================================")
        row.append(dpd.index(i[1].lower()))
    except:
        row.append(-1)
    try:
        print(dfn)
        print(i[2])
        print("====================================")
        row.append(dfn.index(i[2].lower()))
    except:
        row.append(-1)
    try:
        print(dsn)
        print(i[3])
        print("====================================")
        row.append(dsn.index(i[3].lower()))
    except:
        row.append(-1)
    print(row)
    pred = knn.predict([row])
    print(pred,"+++++++++++++++++++++++++++++++")
    return pred
    # Predictions and Evaluations
    # Let's evaluate our KNN model !
    # from sklearn.metrics import classification_report, confusion_matrix
    #
    # print(confusion_matrix(y_test, pred))
    #
    # print(classification_report(y_test, pred))