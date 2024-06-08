from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.methods.send_photo import SendPhoto
from aiogram.methods import SendPhoto
import random

from kb import mood_kb, back_kb
from text import good, norm, bad
import text

choice=["photo", "message"]

good_list = [text.good_movie, text.good_song, text.good_quote]
norm_list = [text.norm_movie, text.norm_song, text.norm_quote]
bad_list = [text.bad_movie, text.bad_song, text.bad_quote]

good_photo = FSInputFile("1.jpeg")
norm_photo = FSInputFile("2.jpeg")
bad_photo = FSInputFile("3.jpeg")

import states
from states import Question
from aiogram.filters import Command
router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(Question.name)

@router.message(Question.name)
async def name(message: Message, state: FSMContext):
    if message.text == None:
        await message.answer("Как тебя зовут?")
    else:
        await state.update_data(name=message.text)
        data = await state.get_data()
        name = data["name"]
        await state.set_state(Question.mood)
        await message.answer(f"{name}, как Ваше настроение?", reply_markup=mood_kb)

@router.message(Question.mood)
async def mood(message: Message, state: FSMContext):
    if message.text == None:
        await message.answer("Нажми на кнопку!)", reply_markup=mood_kb)
    elif message.text == good:
        res = random.choice(choice)
        if res == "photo":
            await message.answer_photo(good_photo, reply_markup=back_kb)
        else:
            await message.answer(random.choice(good_list), reply_markup=back_kb)
        await state.clear()
    elif message.text == norm:
        res = random.choice(norm_list)
        if res == "photo":
            await message.answer_photo(norm_photo, reply_markup=back_kb)
        else:
            await message.answer(random.choice(norm_list), reply_markup=back_kb)
        await state.clear()
    elif message.text == bad:
        res = random.choice(bad_list)
        if res == "photo":
            await message.answer_photo(bad_photo, reply_markup=back_kb)
        else:
            await message.answer(random.choice(bad_list), reply_markup=back_kb)
        await state.clear()
    else:
        await message.answer("Нажми на кнопку!)", reply_markup=mood_kb)

@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Как Ваше настроение?", reply_markup=mood_kb)
    await state.set_state(Question.mood)
