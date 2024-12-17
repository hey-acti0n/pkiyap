import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

bot = telebot.TeleBot('7715967994:AAFwur81tcHy2ap9eTh-_RVOA6mT3i7QZq8')
@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("регистрация")
    button2 = KeyboardButton("пришли html файл плейлиста")

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
    elif message.text=='пришли html файл плейлиста':
        bot.send_message(message.from_user.id, 'пришли ссылку на плейлист')
        bot.register_next_step_handler(message, pars)
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

def pars(message):
    url = message.text
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()


    try:
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(3)
        cancel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[22]/div/span").click()



        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        with open("/Users/acti0n/Documents/proga/dz/pars_code_YANDEX_music.html", "w") as file:
            file.write(driver.page_source)
        

    
    
        time.sleep(1)
    except Exception as ex:
        print(ex)
    finally:
            driver.close()
            driver.quit()
            bot.send_document(message.from_user.id, file)



bot.polling(none_stop=True, interval=0)