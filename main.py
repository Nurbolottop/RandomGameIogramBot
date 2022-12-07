from aiogram import Bot, Dispatcher, executor, types

import config
import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','go'])
async def help(message: types.Message):
    await message.answer(f"Здравстуйте,{message.from_user.full_name} .Меня зовут Tolobrun.\nЕсли хотите узнать обо мне больше нажмите: /help ")
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Я могу вам предложить игру << Randomer >>\nПравила игры:\n1) Я угадываю число от 1 до 3 вы должны его отгадать\n2) Писать число только цифрами \n3) Если вы угадываете число вам начисляется по 1 баллу\n4) Не писать текст <<Черный>>\nМои Комманды:\n/start - Запустить бота.\n/help - Помощь.\n/startgame - Начать игру")

@dp.message_handler(commands=['startgame'])
async def startgame(message: types.Message):
    await message.answer("Добро пожаловать в игру. Я загадаю число от 1 до 3, Отгадаешь ? : ")
@dp.message_handler(text = ['Черный','черный','Black', 'black','Негр','негр'])
async def black(message: types.Message):
    await message.answer(f'Да я , {message.text}')    
@dp.message_handler(text=["1","2","3",])
async def hello(message: types.Message):
    user = int(message.text)
    randomer = random.randint(1, 3)

    await message.answer(f"Удачи вам {message.from_user.full_name} : ")

    print(user)
    if user == randomer:
        await message.reply(f"Вы угадали!!! Моё число: {randomer}")
        
    elif user != randomer:
        await message.reply(f"Вы  не угадали!!! Моё число: {randomer} ")
        
        

executor.start_polling(dp)
