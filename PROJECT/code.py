from random import randint,sample
import telebot
import emoji
from PIL import Image
from telebot.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton
from threading import Thread
import time

token = '977852685:AAGPLbhm9ZGSYKrKBsMrNQ9IChIp3FOOKTI'
bot=telebot.TeleBot(token)

class main():
    """
    Родительский класс для всех других классов. В нем содержаться методы,
    которые можно вызывать в любой момент, и метод, работающий с конпками.
    """
    
    kb=None

    cash=0

    igra=[]
    
    def __init__(self,message):
        self.textuser=message.text
        self.kb=ReplyKeyboardRemove()
        textbot=self.starters()
        
        bot.send_message(message.chat.id,textbot,reply_markup=self.kb)

    def starters(self): 
        textbot='Прости, я тебя не совсем понимаю...\n'+\
                 'Ты уверен, что написал все правильно?'
        
        if self.textuser=='/start' or self.textuser=='Привет':
            textbot=start               #Пока что пременные start т.п. хранятся у меня 
            self.button('start')        #в теле кода, но я подумаю, куда мне их деть
 
        elif self.textuser=='/help' or self.textuser=='Что происходит?':
            textbot=pomosh

        elif self.textuser=='/who' or self.textuser=='А ты кто?':
            textbot=who

        elif self.textuser=='/menu' or self.textuser=='Чем займемся?':
            textbot=menu

        elif self.textuser=='/balance' or self.textuser=='Сколько крышечек?':
            textbot=self.cash

        elif self.textuser=='/newplant' or self.textuser=='Новое растение!': 
            textbot='текст'             #Текст пока не придумала
            main.mclass=tree

        elif self.textuser=='/games' or self.textuser=='Можим поиграть?':
            textbot=games
        
        elif self.textuser=='/letsplay' or self.textuser=='Давай поиграем':      
            textbot='Хорошо, во что?'
            self.button('which')

        elif self.textuser=='/razlog' or self.textuser=='"Что быстрее?"':
            textbot='Супер! Тогда напиши, когда будешь готов!'       
            self.button('game')
            main.mclass=razlog 
            
        elif self.textuser=='/trashcans' or self.textuser=='"В какую из?"':
            textbot='Супер! Тогда напиши, когда будешь готов!'
            self.button('game')
            main.mclass=musorki

        elif self.textuser=='/end' or self.textuser=='Давай закончим':
            textbot='Хорошо)'
            main.igra=[]
            self.kb=ReplyKeyboardRemove()
            main.mclass=main

        elif self.textuser=='/rules' or self.textuser=='А правила?':
            textbot=rules
            
        return textbot
 
    def button(self,tip):
        self.kb=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

        if tip=='start':
            but=KeyboardButton('/help')
            self.kb.add(but)
            
        elif tip=='which':
            but1=KeyboardButton('"Что быстрее?"')
            but2=KeyboardButton('"В какую из?"')
            self.kb.add(but1,but2)
            
        elif tip=='game':
            but=KeyboardButton('Начинаем!')
            self.kb.add(but)
            
        elif tip=='razlog':
            but1=KeyboardButton(raz[self.igra[1]].split(', ')[0])
            but2=KeyboardButton(raz[self.igra[2]].split(', ')[0])
            but3=KeyboardButton('Давай закончим')
            self.kb.add(but1,but2)
            self.kb.add(but3)
            
        elif tip=='musorki':
            b1,b2,b3,b4,b5,b6,b7,b8=map(KeyboardButton,self.igra[2].keys())
            but=KeyboardButton('Давай закончим')
            self.kb.add(b1,b2,b3)
            self.kb.add(b4,b5)
            self.kb.add(b6,b7,b8)
            self.kb.add(but)
            main.igra.append(self.kb)
            
        elif tip=='sin':
            but1=KeyboardButton('Синий')
            but2=KeyboardButton('Серый')
            self.kb.add(but1,but2)
            
        elif tip=='res':
            but1=KeyboardButton('Давай еще раз')
            but2=KeyboardButton('Давай закончим')
            self.kb.add(but1,but2)
            main.igra[3]=self.kb        #В случае ошибки кнопки должны сохраниться
        
if __name__=='__main__':
    main.mclass=main

    @bot.message_handler(content_types=['text'])
    def send(message):
        main.mclass(message)

    bot.polling()

