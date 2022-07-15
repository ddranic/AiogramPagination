import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from pagination import InlinePagination

token = ""
bot = Bot(token=token, parse_mode="HTML", disable_web_page_preview=True)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    pagination = InlinePagination(button_datas=[(i, 2) for i in range(1, 100)], width=4)
    kb = pagination.get_page_keyboard(cur_page=1)

    await message.answer("пуперт нуб", reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith("n_"))
async def next(call: types.CallbackQuery):
    pagination = InlinePagination(button_datas=[(i, 2) for i in range(1, 100)], width=4)
    kb = pagination.get_page_keyboard(cur_page=call.data)

    await call.message.edit_reply_markup(reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith("b_"))
async def back(call: types.CallbackQuery):
    pagination = InlinePagination(button_datas=[(i, 2) for i in range(1, 100)], width=4)
    kb = pagination.get_page_keyboard(cur_page=call.data)

    await call.message.edit_reply_markup(reply_markup=kb)


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as err:
        print(err)
