import random as rand

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
while guess != ans:
	guess = int(input("Keyin a number(%03d~%03d): " %(nowRange[0], nowRange[1])))
	nowRange = guessNumber(ans, guess, nowRange)
	guessTimes = guessTimes + 1

print("Finish! You guessed %d times in total." %(guessTimes))