from aiogram.fsm.state import StatesGroup, State

class Question(StatesGroup):
    name = State()
    mood = State()