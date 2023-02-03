
bot =Bot(token="5965072095:AAEcyJg_Kg9FWIguWVQ1ZHulhjJEB4jiv04")
dp = Dispatcher(bot)

# Initialize states
# Create a State class and inherit the 'StatesGroup'
class Form(StatesGroup):
    # Setup state
    mute_time = State()
    mute_reason = State()

@bot.message_handler(commands=['mute'], state='*')
async def start_mute_process(message: Message):
    # Initialize state
    await Form.mute_time.set()
    await message.reply("Введите время мута, например 30 минут")
    
@bot.message_handler(state=Form.mute_time)
async def process_mute_time(message: Message, state: FSMContext):
    # Get the mute time
    mute_time = message.text
    # Save the mute time
    await state.update_data(mute_time=mute_time)
    # Go to the next stage
    await Form.next()
    await message.reply("Введите причину мута")
    
@bot.message_handler(state=Form.mute_reason)
async def process_mute_reason(message: Message, state: FSMContext):
    # Get the reason 
    mute_reason = message.text
    # Save the reason
    await state.update_data(mute_reason=mute_reason)
    # Get data from storage
    data = await state.get_data()
    # Do something with data
    # ...
    # Finish conversation
    await state.finish()
    await message.reply(f"Мут на {data['mute_time']} по причине: {data['mute_reason']}")