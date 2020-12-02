from core.HandWriting_Recognition.src.imageToText import pdfToText
from core.grading.py import answerForSingleQuestion
import re
import bisect

def getWordsFromPdf(imagePath, splitAnswers = False):
       wordList, accuracyList = pdfToText(imagePath)

       if splitAnswers:
              # split by keyword 'answer'
              text = re.split("answer", wordList)
              if len(text) > 1:
                     text = text[1:]
              return text
       return wordList

def seperateQuestionAnswer(words_from_answersheet):
       
       qn = ["answer", "answer2", "answer3"]
       nI = len(qn)
       answerFromStudent = {}
       last = len(words_from_answersheet)
       pos1 = bisect.bisect_right(words_from_answersheet, "answer")
       for i in range(1, nI):
              fullanswer = ""
              if i == nI-1:
                     pos2 =  bisect.bisect_right(words_from_answersheet, qn(i))
                     ans = words_from_answersheet[pos1: pos2]
                     for j in ans:
                            fullanswer += j
                            fullanswer += " "
                     answerFromStudent[qn[i-1]: fullanswer]
                     
                     ans = words_from_answersheet[pos2: last-1]
                     for j in ans:
                            fullanswer += j
                            fullanswer += " "
                     answerFromStudent[qn[i]: fullanswer]
                     
              else:
                     pos2 =  bisect.bisect_right(words_from_answersheet, qn(i))
                     ans = words_from_answersheet[pos1: pos2]
                     for j in ans:
                            fullanswer += j
                            fullanswer += " "
                     answerFromStudent[qn[i-1]: fullanswer]
                     pos1 = pos2
             
       
       return answerFromStudent 

              
              

def decomposeDictionary(answerKey, includeMarks = False):
       words = []
       marks = []
       for i in range(len(answerKey)):
              key = 'Qn'+str(i+1)
              answer_and_mark = answerKey.get(key)
              words.append(answer_and_mark[0])
              marks.append(answer_and_mark[1])

       # convert individual string elements to a single string list
       words = [' '.join(w) for w in words]
       if includeMarks:
              return words, marks
       return words

def calculateMark():
       imagePath = '/home/hari/Downloads/htr_test.pdf'
       words_from_answersheet = getWordsFromPdf(imagePath, splitAnswers = True)

       answerKey = {'Qn1':[("test1", "test1"), 10],
                    'Qn2':[("test2", "test2"), 20],
                    'Qn3':[("test3", "test3"), 30]}
       words_from_answerkey = decomposeDictionary(answerKey)
       
       answerFromStudent = seperateQuestionAnswer(words_from_answersheet) # getting answers of corresponding questions
       length = len(answerFromStudent)
       
       answerFromStudentList = list(answerFromStudent) #converting to list for accessing value by index
       answerKeyList = list(answerKey) #converting to list for accessing value by index
       
       total = 0 # for storing total_marks
       for i in range(length):
              total += answerForSingleQuestion(answerFromStudent[i], answerKeyList[i], 10))
              

       ####### Do similarity checking code here #######

       print("Answer sheet:\n", words_from_answersheet)
       print("Answer key:\n", words_from_answerkey)
       return
