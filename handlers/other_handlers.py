from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router: Router = Router()

@router.message()
async def process_answer(message: Message):
    await message.answer(text=LEXICON['other_message'])