import tkinter as tk
win = tk.Tk()
win.geometry('400x300')
win.title('分析程式')
text1 = tk.StringVar(value='GUI-1')
ent1 = tk.Entry(win,textvariable=text1,width=15,justify=tk.CENTER)
ent1.place(relx=0.1,rely=0.5,anchor='center')
text2 = tk.StringVar(value='GUI-2')
ent2 = tk.Entry(win,textvariable=text2,width=15,justify=tk.CENTER)
ent2.place(relx=0.1,rely=0.2,anchor='nw')
text3 = tk.StringVar(value='GUI-3')
ent3 = tk.Entry(win,textvariable=text3,width=15,justify=tk.CENTER)
ent3.place(relx=0.1,rely=0.7,anchor='w')
win.mainloop()