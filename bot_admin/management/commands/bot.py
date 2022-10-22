from django.core.management.base import BaseCommand
import telebot
from telebot import types
from bot_admin.models import *


class Command(BaseCommand):
    help = 'Telegram recipe bot'

    def handle(self, *args, **options):

        bot = telebot.TeleBot('5685981684:AAGdEpBPPaGUZ049kowRUITuRhvDOGmWLuU')

        user_name = ''
        user_gender = ''
        @bot.message_handler(commands=['start'])

        def register_name(message):
            #if not User.objects.filter(tg_id=message.chat.id).exists():
            bot.send_message(message.chat.id, f'Hi user {message.chat.id}\nLet`s register')
            user_name_input = bot.send_message(message.chat.id, 'Please enter your name:')
            bot.register_next_step_handler(user_name_input, register_gender)

        def register_gender(message):
            global user_name
            user_name = message.text.capitalize()
            bot.send_message(message.chat.id, f'So, your name is: {user_name}')
            bot.send_message(message.chat.id, 'Let`s finish registration')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            male = types.KeyboardButton('Male')
            female = types.KeyboardButton('Female')
            markup.add(male, female)
            reply = bot.send_message(message.chat.id, 'Choose gender:', reply_markup=markup)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.register_next_step_handler(reply, finish_registration)

        def finish_registration(message):
            global user_gender
            global user_name
            user_gender = message.text
            user = User(tg_id=message.chat.id, name=user_name, gender=user_gender)
            user.save()
            bot.send_message(message.chat.id,
                             f'So, it`s information about you:\n\nName: {user_name}\n\nGender: {user_gender}',
                             reply_markup=types.ReplyKeyboardRemove())


        @bot.message_handler(commands=['menu'])
        def main_menu(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            info = types.KeyboardButton('Info')
            recepie = types.KeyboardButton('Recepies')
            markup.add(info, recepie)
            reply = bot.send_message(message.chat.id, 'Choose your next step', reply_markup=markup)
            bot.register_next_step_handler(reply, menu_choice)

        def menu_choice(reply):
            user = User.objects.get(tg_id=reply.chat.id)
            if reply.text == 'Info':
                bot.send_message(reply.chat.id,
                                 f'So, it`s information about you:\n\nName: {user.name}\n\nGender: {user.gender}')
            elif reply.text == 'Recepies':
                recepies = Recipe.objects.all()
                bot.send_message(reply.chat.id, 'Receepies:', reply_markup=types.ReplyKeyboardRemove())
                markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
                for i in recepies:
                    markup.add(types.KeyboardButton(i.title))
                reply = bot.send_message(reply.chat.id, 'Here is some recepies for you:', reply_markup=markup)
                bot.register_next_step_handler(reply, recepies_list)

        def recepies_list(message):
            if message.text == 'soup':
                bot.send_photo(message.chat.id, photo=open('media/soup.JPG', 'rb'), caption='lorem ipsum')
            elif message.text == 'donner':
                bot.send_photo(message.chat.id, photo=open('media/donner.jpg', 'rb'), caption='lorem ipsum')
            elif message.text == 'pasta':
                bot.send_photo(message.chat.id, photo=open('media/pasta.jpg', 'rb'), caption='lorem ipsum')
            elif message.text == 'tiramisu':
                bot.send_photo(message.chat.id, photo=open('media/tiramisu.jpg', 'rb'), caption='lorem ipsum')

        bot.infinity_polling()
