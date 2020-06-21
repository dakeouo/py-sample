import tkinter as tk

CurrentRange = [0, 999]

window = tk.Tk() #窗口物件
window.title('終極密碼猜數字(000~999)') #窗口名字
window.geometry('360x480') #窗口大小(寬X高)
window.resizable(False, False) #禁止變更視窗大小

tk.Label(window,text = "CurrentRange", font=('Arial', 12)).place(x=180,y=15,anchor="n")
SHOW_CRange = tk.Label(window,text = "%03d~%03d" %(CurrentRange[0], CurrentRange[1]), font=('Arial', 60))
SHOW_CRange.place(x=180,y=40,anchor="n")

window.mainloop()