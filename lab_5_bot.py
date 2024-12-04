import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import math
bot = telebot.TeleBot('7677437617:AAGR5BlPo7j0ughOpIlKLSb9COdmoOdpJ68')
@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("регистрация")
    button2 = KeyboardButton("реши биквдратное уравнение")

    markup.add(button1, button2)


    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)



name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def handle(message):
    
    if message.text == 'регистрация':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)#следующий шаг – функция get_name
    elif message.text=='реши биквдратное уравнение':
        bot.send_message(message.from_user.id, 'напиши коэфициенты через пробел')
        bot.register_next_step_handler(message, solve_biquadratic)
    else:
        bot.send_message(message.from_user.id, 'Напиши регистрация')

def get_name(message): 
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: 
        try:
             age = int(message.text) 
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
             
        bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')


def solve_biquadratic(message):
    s=message.text
    a,b,c=s.split()
    a=int(a)
    b=int(b)
    c=int(c)
     
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        bot.send_message(message.from_user.id, "Нет действительных решений") 
        return
    y1 = (-b + math.sqrt(discriminant)) / (2*a)
    y2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    solutions = []
    

    if y1 >= 0:
        solutions.append(math.sqrt(y1))
        solutions.append(-math.sqrt(y1))
    
    if y2 >= 0:
        solutions.append(math.sqrt(y2))
        solutions.append(-math.sqrt(y2))
    
    if not solutions:
        bot.send_message(message.from_user.id, "Нет действительных решений") 
        return
    bot.send_message(message.from_user.id, "вот твои решения")
    bot.send_message(message.from_user.id, f"{solutions}")


bot.polling(none_stop=True, interval=0)