from tkinter import *
from PIL import ImageTk,Image

asd = Tk()
asd.title("Kenny World")
# asd.iconbitmap(r'C:\Users\USER\Desktop\TKpy\Icon1.ico')
x = asd.winfo_screenwidth() // 3
y = int(asd.winfo_screenheight() * 0.2)
asd.geometry('500x500+' + str(x) + '+' + str(y))
asd.resizable(False, False)

# bg_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\Desktop\TKpy\Icon1.png"))
#
# label1 = Label(image=bg_img1)
# label1.pack()

# x1 = label1.winfo_screenwidth() // 4

def start1():
    return



b1 = Button(asd, text="Exit", padx=80, pady=10, command=asd.quit, bg="#ff0000")

b1.pack()

asd.mainloop()