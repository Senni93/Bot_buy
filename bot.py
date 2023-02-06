import time
import logging
import tok
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

t = tok.TOKEN

# MSG = 'Программировал ли ты сегодня?, {}' 

bot = Bot(t) # token=TOKEN
dp = Dispatcher(bot) # bot=bot

list ={}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}{time.asctime()}')

    await message.reply(f'Привет, {user_full_name}')


@dp.message_handler(commands=['help'])
async def help_mes(message: types.Message):
    await message.reply("Здесть <b> будут команды для помощи! </b>", parse_mode='HTML')
    await message.answer('Команды для работы с ботом\n/start - Приветсвие\n/help - Какие команды есть \n/cls - Команда очистки списка\n/list -  Показать список\n/sum - Сумма корзины')

@dp.message_handler(commands=['cls'])
async def delete(message: types.Message):
    # link.clear()
    list.clear()
    await message.reply("Очищенно")

@dp.message_handler(commands=['list'])
async def link_show(message: types.Message):
    if not list:
        await message.answer('Список пустой')
    else:
        await message.answer('\n'.join(list)) #'\n'.join(list)

    # await message.reply()

@dp.message_handler(commands=['sum'])
async def summa(message: types.Message):
    sum_list = sum(list.values())
    await message.answer(f'Цена корзины: {sum_list} ')

@dp.message_handler() # Ввод даннх пользователя
async def link_new(message: types.Message):
    n, a = map(str, message.text.split())
    list[n]= int(a)

    # link.append(message.text)

    await message.answer("Добавлено")




# @dp.message_handler()
# async def echo(message: types.Message):
    
#     i = int(message.text)
#     if i < 5:
#         await message.reply("Вы вели цифру меньше 5")
#     else:
#         await message.answer("эта цифра больше 5")
    


    # for i in range(10):
    #     time.sleep(100)

    #     await bot.send_message(user_id, MSG.format(user_name))

# @dp.message_handler(commands=['help'])
# async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
#    await message.answer("Hello")


# @dp.message_sum(commands=[f"{summa}"])
# async def sum(message: types.Message):
#     answer = summa+100
#     await message.reply(answer)


if __name__ == '__main__':
    executor.start_polling(dp)


