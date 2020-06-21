import random as rand
import tkinter as tk

# UI要用的參數
CurrentRange = [0, 999]

# 主要程式要用的參數
sysRange = (0, 999) #終極數字範圍
nowRange = [sysRange[0], sysRange[1]] #目前的猜測範圍
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

ans = newAnsNumber(sysRange[0], sysRange[1])
# while guess != ans:
# 	guess = int(input("Keyin a number(%03d~%03d): " %(nowRange[0], nowRange[1])))
# 	nowRange = guessNumber(ans, guess, nowRange)
# 	guessTimes = guessTimes + 1

# print("Finish! You guessed %d times in total." %(guessTimes))

window = tk.Tk() #窗口物件
window.title('終極密碼猜數字(000~999)') #窗口名字
window.geometry('360x480') #窗口大小(寬X高)
window.resizable(False, False) #禁止變更視窗大小

tk.Label(window,text = "CurrentRange", font=('Arial', 12)).place(x=180,y=15,anchor="n")
SHOW_CRange = tk.Label(window,text = "%03d~%03d" %(CurrentRange[0], CurrentRange[1]), font=('Arial', 60))
SHOW_CRange.place(x=180,y=40,anchor="n")

window.mainloop()
