import random as rand
import tkinter as tk
import tkinter.messagebox as msgbox

# UI要用的參數
SHOW_CRange = ""
SHOW_Times = ""
SHOW_GuessNumber = ["", "", ""]

# 主要程式要用的參數
sysRange = (0, 999) #終極數字範圍
currentRange = [sysRange[0], sysRange[1]] #目前的猜測範圍
ans = 0 #存放終極數字
guess = 0 #猜測數字
guessTimes = 0 #猜測次數

def guessNumber(ans, guess, nowRange): #判斷猜測數字(答案, 猜的數字, 目前猜測範圍)
	if guess <= ans:
		nowRange[0] = guess
	else:
		nowRange[1] = guess

	return nowRange

def newAnsNumber(_min, _max): #取得終極數字(最小值, 最大值)
	return rand.randint(_min, _max)

def updateGuessNumber(guess):
	newGuess = guess
	for i in range(3):
		SHOW_GuessNumber[i].config(text=str(int(newGuess/pow(10,2-i))))
		newGuess = newGuess%pow(10,2-i)

def TK_GuessNumber(btnType, digits):
	global sysRange, currentRange, guess
	global SHOW_GuessNumber
	
	if not btnType:
		if (guess + pow(10, digits) <= currentRange[1]):
			guess = guess + pow(10, digits)
	else:
		if (guess - pow(10, digits) >= currentRange[0]):
			guess = guess - pow(10, digits)

	updateGuessNumber(guess)

def TK_ConfirmNumber():
	global ans, guess, currentRange, guessTimes, sysRange

	if guess == ans:
		playagain = msgbox.askyesno(title='恭喜猜到了!',message='終極密碼的數字為 %d \n要再玩一次嗎?' %(ans))
		if playagain:
			ans = newAnsNumber(sysRange[0], sysRange[1])
			guess = 0
			guessTimes = 0
			currentRange = [sysRange[0], sysRange[1]]
			updateGuessNumber(guess)
			SHOW_Times.config(text = "猜測次數: %d" %(guessTimes))
			SHOW_CRange.config(text = "%03d~%03d" %(currentRange[0], currentRange[1]))
		else:
			window.destroy()
	else:
		if guess != currentRange[0] and guess != currentRange[1]:
			guessTimes = guessTimes + 1
		currentRange = guessNumber(ans, guess, currentRange)
		SHOW_Times.config(text = "猜測次數: %d" %(guessTimes))
		SHOW_CRange.config(text = "%03d~%03d" %(currentRange[0], currentRange[1]))

ans = newAnsNumber(sysRange[0], sysRange[1])

window = tk.Tk() #窗口物件
window.title('終極密碼猜數字(000~999)') #窗口名字
window.geometry('360x480') #窗口大小(寬X高)
window.resizable(False, False) #禁止變更視窗大小

# 顯示目前可猜測範圍
tk.Label(window,text = "目前範圍", font=('Arial', 12)).place(x=180,y=15,anchor="n")
SHOW_CRange = tk.Label(window,text = "%03d~%03d" %(currentRange[0], currentRange[1]), font=('Arial', 60))
SHOW_CRange.place(x=180,y=40,anchor="n")

# 猜測次數
SHOW_Times = tk.Label(window,text = "猜測次數: %d" %(guessTimes), font=('Arial', 14))
SHOW_Times.place(x=180,y=130,anchor="n")

NumDis = 70
NumColBasic = 200
for i in range(3):
	SHOW_GuessNumber[i] = tk.Label(window,text = "0", font=('Arial', 70))
	SHOW_GuessNumber[i].place(x=180 + NumDis*(i - 1), y=NumColBasic + 30,anchor="n")

i = 0
SHOW_Guess_Btn = tk.Button(window, text='▲', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(False, 2))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic, anchor="n")
SHOW_Guess_Btn = tk.Button(window, text='▼', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(True, 2))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic + 130, anchor="n")
i = 1
SHOW_Guess_Btn = tk.Button(window, text='▲', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(False, 1))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic, anchor="n")
SHOW_Guess_Btn = tk.Button(window, text='▼', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(True, 1))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic + 130, anchor="n")
i = 2
SHOW_Guess_Btn = tk.Button(window, text='▲', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(False, 0))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic, anchor="n")
SHOW_Guess_Btn = tk.Button(window, text='▼', width=4, font=('Arial', 13), command=lambda: TK_GuessNumber(True, 0))
SHOW_Guess_Btn.place(x=180 + NumDis*(i - 1), y=NumColBasic + 130, anchor="n")

SHOW_Confirm_Btn = tk.Button(window, text='確認送出', width=20, font=('Arial', 14), command=TK_ConfirmNumber)
SHOW_Confirm_Btn.place(x=180, y=400, anchor="n")

window.mainloop()
