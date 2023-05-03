from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

time.clock = time.time

chatbot = ChatBot('MeuChatBot')

trainer = ListTrainer(chatbot)
trainer.train(['Eai!','Eai!','amo você','Eu também me amo! haha','quero perguntar algo','O que quer saber?','como você está?','Não tenho emoções, sou um robô apenas!','Qual o tamanho da terra?','Se considerarmos a circunferência da Terra, ela tem aproximadamente 40.075 quilômetros','Qual meu nome?','Kaique. Como sei? Não pergunte haha','como sabe?','Um mágico não revela seus segredos.',])



root = Tk()
root.title("ChatBot")
root.geometry("800x500")

chat_area = Text(root, height=25, width=100, bg='white', fg='black')
chat_area.config(state=DISABLED)
chat_area.pack(padx=10, pady=10)

user_input = Entry(root, width=100)
user_input.pack(side=LEFT, padx=10, pady=10)

def send_message(event):
    user_message = user_input.get()
    chat_area.config(state=NORMAL)
    chat_area.insert(END, "Você: " + user_message + '\n')
    chat_area.config(state=DISABLED)
    user_input.delete(0, END)
    response = get_response(user_message)
    chat_area.config(state=NORMAL)
    chat_area.insert(END, "ChatBot: " + response + '\n')
    chat_area.config(state=DISABLED)
    chat_area.yview(END)

user_input.bind("<Return>", send_message)

def get_response(user_message):
    response = chatbot.get_response(user_message)
    return str(response)




root.mainloop()
