import os
from tkinter import *
import random

question = ""
answer = ""
correct = 0
incorrect = 0

def choice():
   choice = random.choice(choiceNum)
   indoWordLabel.config(text=indoWord[choice])
   global answer
   answer = englishWord[choice]

def showAnswer():
    indoWordLabel.config(text=answer)

def correctUpdate():
    global correct
    correct = correct+1
    correctLabel.config(text=("Correct: "+str(correct)))

def incorrectUpdate():
    global incorrect
    incorrect = incorrect +1
    incorrectLabel.config(text=("Incorrect: "+str(incorrect)))

def endGame():
    root.destroy()

file = open("wordDict.txt",'r')
listOfWords = file.readlines()

size = range(len(listOfWords))

indoWord = []
englishWord = []

for i in size:
    if i%3 == 0:
        indoWord.append(listOfWords[i].strip('\n'))
    elif i%3 == 1:
        englishWord.append(listOfWords[i].strip('\n'))
    else:
        pass

choiceNum= range(len(indoWord))

root = Tk()
root.title("Indonesian Flash Cards")
root.configure(bg="#1DA1F2")
root.minsize(800, 700)  # width, height
root.maxsize(1000, 1000)
root.geometry("900x700+600+100")  # width x height + x + y

frame = Frame(root,bg="#1DA1F2")
frame.pack(side=TOP,pady=30)


indoWordLabel = Label(frame, text="Click begin to start.", font=("courier", 40), padx=50,pady=50,bg="white",fg="black")
indoWordLabel.pack(pady=10,side=TOP)


beginButton = Button(frame, text="New Word", font=("courier",50),padx=40,pady=40,command=choice)
beginButton.pack(side=RIGHT)

checkButton = Button(frame,text="Flip",font=("courier",50),padx=40,pady=40,command=showAnswer)
checkButton.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(pady=30)
frame2.configure(bg="#1DA1F2")

correctLabel = Label(frame2, text=("Correct: "+str(correct)),font=("times new roman", 30),padx=50,pady=50)
correctLabel.pack(side=RIGHT)

incorrectLabel = Label(frame2, text=("Incorrect: "+ str(incorrect)),font=("times new roman", 30),padx=50,pady=50)
incorrectLabel.pack(side=RIGHT)

correctButton = Button(frame2,text="Correct",font=("courier",50),command=correctUpdate)
correctButton.pack(side=TOP)

incorrectButton = Button(frame2,text="Incorrect",font=("courier",50),command=incorrectUpdate)
incorrectButton.pack(side=BOTTOM)

frame3 = Frame(root,bg="#1DA1F2")
frame3.pack(side=BOTTOM)

endGameButton = Button(frame3,text="END GAME",font=("courier",50), command= endGame)
endGameButton.pack()

root.mainloop()

#saving the score

scoreDataBase = open("scoreDataBase.txt",'a')
scoreDataBase.write("\nCorrect: " + str(correct) + " Incorrect: " + str(incorrect))