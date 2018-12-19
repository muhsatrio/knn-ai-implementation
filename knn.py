import csv
import math

train = []
test = []
hasil = []

def writeResult(file):
    with open(file, 'w', newline='') as fileResult:
        writer = csv.writer(fileResult)
        for rowHasil in hasil:
            writer.writerow([rowHasil])

def hitungAkurasi():
    lenTesting = len(test)
    size = len(train)
    ok = 0
    for i in range(0,lenTesting):
        if (test[i][6]==train[i][6]):
            ok += 1
    akurasi = (ok/lenTesting) * 100

    print("Akurasi: ", akurasi, "%")

def importTrain(fileName):
    with open(fileName) as file:
        reader = csv.reader(file)
        for row in reader:
            train.append(row)
    for row in train:
        row[0] = float(row[0])
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = float(row[5])
        row[6] = float(row[6])
    # print(train)

def importTest(fileName):
    with open(fileName) as file:
        reader = csv.reader(file)
        for row in reader:
            test.append(row)
    for row in test:
        row[0] = float(row[0])
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = float(row[5])

def proses():
    i = 0
    akurasi = 0
    for rowTest in test:
        jarak = []
        for rowTrain in train:
            euclideanX1 = math.pow(rowTest[1]-rowTrain[1], 2)
            euclideanX2 = math.pow(rowTest[2] - rowTrain[2], 2)
            euclideanX3 = math.pow(rowTest[3] - rowTrain[3], 2)
            euclideanX4 = math.pow(rowTest[4] - rowTrain[4], 2)
            euclideanX5 = math.pow(rowTest[5] - rowTrain[5], 2)
            jarak.append(math.sqrt(euclideanX1 + euclideanX2 +
                        euclideanX3 + euclideanX4 + euclideanX5))
        for rowJarak in jarak:
            rowJarak = math.sqrt(rowJarak)
        print(jarak)

        k = []
        for i in range(0, 5):
            k.append(i)
        lengthJarak = len(jarak)
        for i in range(0,lengthJarak):
            if (jarak[i] < jarak[k[0]]):
                k[0] = i
            elif (jarak[i] < jarak[k[1]]):
                k[1] = i
            elif (jarak[i] < jarak[k[2]]):
                k[2] = i
            # elif (jarak[i] < jarak[k[3]]):
            #     k[3] = i
            # elif (jarak[i] < jarak[k[4]]):
            #     k[4] = i
            # elif (jarak[i] < jarak[k[5]]):
            #     k[5] = i
            # elif (jarak[i] < jarak[k[6]]):
            #     k[6] = i
            # elif (jarak[i] < jarak[k[7]]):
            #     k[7] = i
            # elif (jarak[i] < jarak[k[8]]):
            #     k[8] = i
            # elif (jarak[i] < jarak[k[9]]):
            #     k[9] = i

        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        for rowK in k:
            if (train[rowK][6]==0):
                c1+=1
            elif (train[rowK][6]==1):
                c2+=1
            elif (train[rowK][6]==2):
                c3+=1
            elif (train[rowK][6]==3):
                c4+=1
        if (c1>=c2 and c1>=c3 and c1>=c4):
            rowTest[6] = 0
            hasil.append(0)
        elif (c2>=c1 and c2>=c3 and c2>=c4):
            rowTest[6] = 1
            hasil.append(1)
        elif (c3>=c1 and c3>=c2 and c3>=c4):
            rowTest[6] = 2
            hasil.append(2)
        elif (c4>=c1 and c4>=c2 and c4>=c3):
            rowTest[6] = 3
            hasil.append(3)
        print(k)
# jarak = []

importTrain("DataTrain_Tugas3_AI.csv")
importTest("DataTest_Tugas3_AI.csv")

# print(train[0][4])
proses()

# hitungAkurasi()
print(train)
print(test)
print(hasil)
writeResult('TebakanTugas3.csv')