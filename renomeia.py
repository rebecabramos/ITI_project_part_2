import os

instrumentos = ["cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio"]

for i in instrumentos:

    folderPath = r'C:\Users\rebec\IRMAS-TrainingData_red\\' + i 

    fileSequence = 1

    for filename in os.listdir(folderPath):
        os.renames(folderPath + "\\" + filename, folderPath + "\\" + i + str(fileSequence) + '.wav')
        fileSequence +=1