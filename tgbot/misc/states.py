from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class getPre(StatesGroup):
    pair = State()
    timeframe = State()
    
class getPre2(StatesGroup):
    pair = State()
    timeframe = State()
    
    