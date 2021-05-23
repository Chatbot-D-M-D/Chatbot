
#Crearea GUI-ului cu Tkinter (Interfata)
import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Crearea ecranului de chat
ChatLog = Text(base, bd=0, bg="#48bda3", height="8", width="50", font="Arial")

ChatLog.config(state=DISABLED)

#Punem scrollbar-ul in ecranul de chat
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="dot")
ChatLog['yscrollcommand'] = scrollbar.set

#Crearea butonului de send
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="10", height=5,
                    bd=0, bg="#3c9d9b", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Crearea ecranului de mesaj
EntryBox = Text(base, bd=0, bg="#ffffff",width="29", height="5", font="Arial")

#Plasarea tuturor componentelor pe ecran
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()