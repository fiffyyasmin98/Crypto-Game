import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

LARGEFONT = 'Verdana 35 '
SMALLFONT = 'Verdana 20 '
MEDIUMFONT = 'Verdana 25 '
BUTTONFONT ='SlabSerif 20 bold'
BUTTONSMALLFONT ='SlabSerif 15 bold'
bg = "bg.jpg"
title1 = "title1.png"
title2 = "title2.png"
encrypt = "encrypt.png"
decrypt = "decrypt.png"
level1 = "level1.png"
level2 = "level2.png"
enlevel1ques = "enlevel1ques.png"
enlevel2ques = "enlevel2ques.png"
delevel1ques = "delevel1ques.png"
delevel2ques = "delevel2ques.png"

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Cryptography Game")
        self.iconphoto(False, tk.PhotoImage(file='icon.png'))

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(0, minsize=800, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (MainPage, StartPage, Page1,Page1_1, Page1_2, Page2, Page2_1, Page2_2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage

class img():
    def showImg( self,img, x, y):
        load = Image.open(img)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(padx=10, pady=10)
        img.place(relx=x, rely=y, anchor="center")

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self,bg,0.5,0.5)
        img.showImg(self,title1,0.5,0.25)
        img.showImg(self,title2, 0.5, 0.35)
        # label = ttk.Label(self, text="WELCOME TO MYWILRARYASBAL\n ENCRYPT AND DECRYPT GAME", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5,rely=0.3,anchor="center")

        button1 = tk.Button(self, text="Start",bg='#6ac7e6',fg='#000000',relief='raised',width=10, font=BUTTONFONT,
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(padx=10, pady=10)
        button1.place(relx=0.5,rely=0.5,anchor="center")

        button2 = tk.Button(self, text="Details",bg='#6ac7e6',fg='#000000',relief='raised',width=10, font=BUTTONFONT,
                             command=lambda: controller.show_frame(Page3))
        button2.grid(padx=10, pady=10)
        button2.place(relx=0.5,rely=0.6,anchor="center")

        button3 = tk.Button(self, text="Exit", bg='#6ac7e6',fg='#000000',relief='raised',width=10,font=BUTTONFONT,
                             command=lambda: close_window())
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.5,rely=0.7,anchor="center")

        def close_window():
            import sys
            sys.exit()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, title2, 0.5, 0.3)
        # label = tk.Label(self, text="CRYPTOGRAPHY GAME", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5,rely=0.3,anchor="center")

        button1 = tk.Button(self, text="Encrytion",bg='#6ac7e6',fg='#000000',relief='raised',width=17, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(Page1))
        button1.grid(padx=10, pady=10)
        button1.place(relx=0.3,rely=0.5,anchor="center")

        button2 = tk.Button(self, text="Decryption", bg='#6ac7e6',fg='#000000',relief='raised',width=17, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(Page2))
        button2.grid(padx=10, pady=10)
        button2.place(relx=0.7,rely=0.5,anchor="center")

        button4 = tk.Button(self, text="Back", bg='#6ac7e6',fg='#000000',relief='raised',width=12, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(MainPage))
        button4.grid(padx=10, pady=10)
        button4.place(relx=0.5,rely=0.7,anchor="center")

    # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, encrypt, 0.5, 0.3)
        # label = tk.Label(self, text="Encryption", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.3, anchor="center")

        button1 = tk.Button(self, text="Start Encrypt",bg='#6ac7e6',fg='#000000',relief='raised',width=17, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(Page1_1))
        button1.grid(padx=10, pady=10)
        button1.place(relx=0.5, rely=0.5, anchor="center")

        button3 = tk.Button(self, text="Back", bg='#6ac7e6',fg='#000000',relief='raised',width=12, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(StartPage))
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.5, rely=0.7, anchor="center")

class Page1_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, level1, 0.5, 0.1)
        # label = tk.Label(self, text="Substitution Cipher", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.1, anchor="center")

        label = tk.Label(self, text="---Columnar Transposition Cipher---", font=MEDIUMFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.2, anchor="center")

        label = tk.Label(self, text="Encrypt this message by using e=53421.", font=SMALLFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.3, anchor="center")

        img.showImg(self, enlevel1ques, 0.5, 0.45)

        # add a text entry box for
        e = tk.Entry(self, width=15, font=BUTTONSMALLFONT, )

        e.grid(padx=10, pady=10, ipady=3)
        e.place(relx=0.55, rely=0.7, anchor="e")

        # set focus on the entry box
        e.focus_set()

        button3 = tk.Button(self, text="Submit", bg='#6ac7e6', fg='#000000', relief='raised', width=7,
                            font=BUTTONSMALLFONT,
                            command=lambda: check())
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.55, rely=0.7, anchor="w")

        button4 = tk.Button(self, text="Back", bg='#6ac7e6', fg='#000000', relief='raised', width=12,
                            font=BUTTONSMALLFONT,
                            command=lambda: controller.show_frame(Page1))
        button4.grid(padx=10, pady=10)
        button4.place(relx=0.5, rely=0.8, anchor="center")

        def check():
            if e.get() == "tyyysepmrritcos" or e.get() == "TYYYSEPMRRITCOS":
                messagebox.showinfo("CHECK ANSWER", "CONGRATULATION,YOU ARE CORRECT!!!", icon="info")
                controller.show_frame(Page1_2)
            else:
                messagebox.showinfo("CHECK ANSWER", "YOU ARE WRONG,PLEASE TRY AGAIN", icon="info")

            # clear the text entry box.
            e.delete(0, tk.END)

class Page1_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, level2, 0.5, 0.1)
        # label = tk.Label(self, text="Substitution Cipher", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.1, anchor="center")

        label = tk.Label(self, text="---Keyed Transposition Cipher---", font=MEDIUMFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.2, anchor="center")

        label = tk.Label(self, text="Encrypt this message by using e=4625173.", font=SMALLFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.3, anchor="center")

        img.showImg(self,enlevel2ques,0.5,0.45)

        # add a text entry box for
        e = tk.Entry(self,width=15,font=BUTTONSMALLFONT,)

        e.grid(padx=10, pady=10,ipady=3)
        e.place(relx=0.55,rely=0.7,anchor="e")

        # set focus on the entry box
        e.focus_set()

        button3 = tk.Button(self, text="Submit",bg='#6ac7e6',fg='#000000',relief='raised',width=7, font=BUTTONSMALLFONT,
                             command=lambda: check())
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.55, rely=0.7, anchor="w")

        button4 = tk.Button(self, text="Back", bg='#6ac7e6',fg='#000000',relief='raised',width=12, font=BUTTONSMALLFONT,
                             command=lambda: controller.show_frame(Page1))
        button4.grid(padx=10, pady=10)
        button4.place(relx=0.5, rely=0.8, anchor="center")

        def check():
            if e.get() == "ntwtioatoeymue" or e.get() == "NTWTIOATOEYMUE":
                messagebox.showinfo("CHECK ANSWER", "CONGRATULATION,YOU ARE CORRECT!!!", icon="info")
                controller.show_frame(StartPage)
            else:
                messagebox.showinfo("CHECK ANSWER", "YOU ARE WRONG,PLEASE TRY AGAIN", icon="info")

            # clear the text entry box.
            e.delete(0, tk.END)


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, decrypt, 0.5, 0.3)
        # label = tk.Label(self, text="Encryption", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.3, anchor="center")

        button1 = tk.Button(self, text="Start Decrypt", bg='#6ac7e6', fg='#000000', relief='raised', width=17,
                            font=BUTTONSMALLFONT,
                            command=lambda: controller.show_frame(Page2_1))
        button1.grid(padx=10, pady=10)
        button1.place(relx=0.5, rely=0.5, anchor="center")

        button3 = tk.Button(self, text="Back", bg='#6ac7e6', fg='#000000', relief='raised', width=12, font=BUTTONSMALLFONT,command=lambda: controller.show_frame(StartPage))
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.5, rely=0.7, anchor="center")

class Page2_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, level1, 0.5, 0.1)
        # label = tk.Label(self, text="Substitution Cipher", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.1, anchor="center")

        label = tk.Label(self, text="---Vigenere Cipher---", font=MEDIUMFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.2, anchor="center")

        label = tk.Label(self, text="Encrypt this message by using d=sirazlan.", font=SMALLFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.3, anchor="center")

        img.showImg(self, delevel1ques, 0.5, 0.45)

        # add a text entry box for
        e = tk.Entry(self, width=15, font=BUTTONSMALLFONT, )

        e.grid(padx=10, pady=10, ipady=3)
        e.place(relx=0.55, rely=0.7, anchor="e")

        # set focus on the entry box
        e.focus_set()

        button3 = tk.Button(self, text="Submit", bg='#6ac7e6', fg='#000000', relief='raised', width=7,
                            font=BUTTONSMALLFONT,
                            command=lambda: check())
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.55, rely=0.7, anchor="w")

        button4 = tk.Button(self, text="Back", bg='#6ac7e6', fg='#000000', relief='raised', width=12,
                            font=BUTTONSMALLFONT,
                            command=lambda: controller.show_frame(Page2))
        button4.grid(padx=10, pady=10)
        button4.place(relx=0.5, rely=0.8, anchor="center")

        def check():
            if e.get() == "pleasemarryme" or e.get() == "PLEASEMARRYME" or e.get() == "PleaseMarryMe":
                messagebox.showinfo("CHECK ANSWER", "CONGRATULATION,YOU ARE CORRECT!!!", icon="info")
                controller.show_frame(Page2_2)
            else:
                messagebox.showinfo("CHECK ANSWER", "YOU ARE WRONG,PLEASE TRY AGAIN", icon="info")

            # clear the text entry box.
            e.delete(0, tk.END)

class Page2_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img.showImg(self, bg, 0.5, 0.5)
        img.showImg(self, level2, 0.5, 0.1)
        # label = tk.Label(self, text="Substitution Cipher", font=LARGEFONT)
        # label.grid(padx=10, pady=10)
        # label.place(relx=0.5, rely=0.1, anchor="center")

        label = tk.Label(self, text="---Caesar Cipher---", font=MEDIUMFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.2, anchor="center")

        label = tk.Label(self, text="Encrypt this message by using key= shift 5 in clockwise.", font=SMALLFONT)
        label.grid(padx=10, pady=10)
        label.place(relx=0.5, rely=0.3, anchor="center")

        img.showImg(self, delevel2ques, 0.5, 0.45)

        # add a text entry box for
        e = tk.Entry(self, width=15, font=BUTTONSMALLFONT, )

        e.grid(padx=10, pady=10, ipady=3)
        e.place(relx=0.55, rely=0.7, anchor="e")

        # set focus on the entry box
        e.focus_set()

        button3 = tk.Button(self, text="Submit", bg='#6ac7e6', fg='#000000', relief='raised', width=7,
                            font=BUTTONSMALLFONT,
                            command=lambda: check())
        button3.grid(padx=10, pady=10)
        button3.place(relx=0.55, rely=0.7, anchor="w")

        button4 = tk.Button(self, text="Back", bg='#6ac7e6', fg='#000000', relief='raised', width=12,
                            font=BUTTONSMALLFONT,
                            command=lambda: controller.show_frame(Page2))
        button4.grid(padx=10, pady=10)
        button4.place(relx=0.5, rely=0.8, anchor="center")

        def check():
            if e.get() == "imissyou" or e.get() == "IMISSYOU" or e.get() == "IMissYou":
                messagebox.showinfo("CHECK ANSWER", "CONGRATULATION,YOU ARE CORRECT!!!", icon="info")
                controller.show_frame(StartPage)
            else:
                messagebox.showinfo("CHECK ANSWER", "YOU ARE WRONG,PLEASE TRY AGAIN", icon="info")

            # clear the text entry box.
            e.delete(0, tk.END)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = tk.Button(self, text="Page 1",bg='#6ac7e6', fg='#000000', relief='raised', width=10, font=BUTTONFONT,
                             command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = tk.Button(self, text="Startpage",bg='#6ac7e6', fg='#000000', relief='raised', width=10, font=BUTTONFONT,
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
