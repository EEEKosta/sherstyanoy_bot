import asyncio, os, aiogram, random
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, PHOTO_DIR


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# COMMANDS
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.answer(
		'Привет, я Шерстяной 😸. Я здесь что бы дарить улыбку! Но все не так просто, что бы получить картинку с котейкой продолжи фразу "Три кота - ... ..."'
	)

@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
	await message.answer(
		'Если хочешь котейку, продолжи фразу "Три кота - ... ...". Или напиши моему хозяину @E_Kostya'
	)

# MESSAGES
@dp.message_handler()#content_types=[types.ContentType.ANY])
async def get_messages(message: types.Message):
	# игнорируем регистр в котором написано сообщение
    if message.text.lower() == "три хвоста":
    	
    	# получаем список картинок из нужной папки
    	photos = os.listdir(PHOTO_DIR)

    	# выбираем случайную картнку из списка
    	random_photo = random.choice(photos)

    	# указываем путь к нашей картинке
    	photo_path = f"{PHOTO_DIR}{os.sep}{random_photo}"

    	# Отправляем картинку пользователю
    	with open(photo_path, 'rb') as photo:
    		await bot.send_photo(
    			chat_id=message['from']['id'],
    			photo=photo
    		)

    else:
    	await message.answer("Не угадал, попробуй еще")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


