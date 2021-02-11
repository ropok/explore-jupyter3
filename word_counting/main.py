'''
text-mining: menghitung frekuensi kemunculan kata
'''

import os
from os import system, name
import csv
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

import pandas as pd
from datetime import datetime


# NLTK
class Main():

    # open log to write report process
    def __init__(self, log):
        super(Main, self)
        self.log = open(log+'.txt', "w")
        self.log_output = open('output_'+log+'.txt', "w")

    def logSukses(self, textInfo, textContent):
        self.log.write("SUCCESS: \t {textInfo} \"{textContent}\"\n".format(textInfo=textInfo, textContent=textContent))
        self.log.flush()
        print("SUCCESS: \t {textInfo} \"{textContent}\"\n".format(textInfo=textInfo, textContent=textContent))

    def logError(self, errorId, textInfo, textContent):
        self.log.write("ERROR {errorId}: \t {textInfo} \"{textContent}\"\n".format(errorId=errorId, textInfo=textInfo, textContent=textContent))
        self.log.flush()
        print("ERROR {errorId}: \t {textInfo} \"{textContent}\"\n".format(errorId=errorId, textInfo=textInfo, textContent=textContent))

    # tokenize text, nltk initiation to text
    def tokenize(self, text):
        try:
            self.text = text
            self.token = word_tokenize(self.text)
            self.logSukses('tokenize', self.text)
        except expression as identifier:
            self.logError('101', 'tokenize', self.text)
            
    
    # count frequency of words
    def freqdist(self):
        try:
            self.fdist = FreqDist(self.token)
            self.logSukses('freqdist', self.text)
            return self.fdist
        except expression as identifier:
            self.logError('102', 'freqdist', self.text)
            
    
    # print frequency (key and value), and write txt
    def freqword(self, dictWords):
        try:
            self.dictWords = dictWords
            self.logSukses('writing frequency of words', '')
            self.log_output.seek(0)
            for i in self.dictWords:
                # print(i, self.dictWords[i])
                self.log_output.write(i + " " + str(self.dictWords[i]) + "\n")
            self.log_output.truncate()
            self.log_output.flush()
        except expression as identifier:
            self.logError('103', 'writing frequency of words failed', '')
            
    def closeLog(self):
        self.log.close()
        self.log_output.close()

# Dataframe (read .xlsx)
class readData():
    
    def __init__(self):
        super(readData, self)

    # open file .xlsx
    def open(self, data_file):
        self.data_file = pd.read_excel(data_file)

    def count(self):
        self.count_index = len(self.data_file.index)
        return self.count_index

    # return value of column
    def column(self, column_name):
        # read dataframe with specific column_name
        data = pd.DataFrame(self.data_file, columns=[column_name])
        self.data_value = []
        for i in data.values:
            self.data_value.append(i[0])
        return self.data_value

    def readLastColumn(self):
        kolom = self.data_file.columns
        kolomTerakir = kolom.tolist()[len(kolom)-1]
        return kolomTerakir


if __name__ == '__main__':
    # nltk class
    main = Main(datetime.today().strftime('%Y%m%d'))
    read_data = readData()

    # clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux (here, os.name is 'posix')
        else:
            _ = system('clear')

    # initiation for data collector variable
    main.tokenize("")
    fdist_collect = main.freqdist()
    main.freqword(fdist_collect)

    # path of the .xlsx files
    path = r"C:\Users\jalerse\Documents\dev-jalerse\python-helping-tools\rekaman-stt\text-mining\rekaman-text-tervalidasi\ALL\anggaa"

    # count row total
    index_total = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.startswith("batch") and filename.endswith(".xlsx"):
                input_file = root + "/" + filename
                read_data.open(input_file)
                index_total+=read_data.count()
                print(read_data.count())
    print('index total', index_total)

    # hitung frekuensi Kata
    index_current = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.startswith("batch") and filename.endswith(".xlsx"):
                input_file = root + "/" + filename
                print(input_file)
                read_data.open(input_file)
                data_list = read_data.column('transcript_training')
                for data in data_list:
                    main.tokenize(data)
                    fdist = main.freqdist()
                    fdist_collect.update(fdist)
                    main.freqword(fdist_collect)
                    # print progress
                    index_current+=1
                    clear()
                    print(index_current, 'of', index_total)

    main.closeLog()