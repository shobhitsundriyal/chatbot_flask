from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot('ChatterBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train('chatterbot.corpus.english')
