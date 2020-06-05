import logging
import time as t

from setup import PROXY, TOKEN
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater, ConversationHandler, CallbackQueryHandler
from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import json

mystem = Mystem()
russian_stopwords = stopwords.words("russian") + ["ко"]

bot = Bot(
        token=TOKEN,
        base_url=PROXY,  # delete it if connection via VPN
    )

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    text = f'Hello, {update.effective_user.first_name}! 👋\nWelcome to the smart bot that is able to detect and extract key words from text!\n Write /help to learn detailes.'
    update.message.reply_text(text)
    return text

def help(update: Update, context: CallbackContext):
    update.message.reply_text("In order to find key words in your document it is required that you send me a message containing document only. Make sure there are no other charachters. Preferred type of doc is .txt. Hope you'll enjoy!")

def get_file(update: Update, context: CallbackContext):
    print("get file function is started")
    overall_start = t.time()
    document = update["message"]["document"]["file_id"]
    file = context.bot.getFile(file_id=document)
    file.download("file.txt")
    key_words, tokens = keywords()
    overall_finish = t.time()
    update.message.reply_text(f"According to my findings, your file containes {len(key_words)} significant words.")
    update.message.reply_text(f"It took {overall_finish - overall_start} seconds.")
    update.message.reply_text(f"The length of your doc is {len(tokens)} words")
    update.message.reply_text(" ".join(key_words[:10]))


def keywords():
    print("key words is started")
    # making a list of all lemmas from the doc
    start = t.time()
    with open("file.txt", encoding="utf8") as doc:
        tokens = mystem.lemmatize(doc.read().lower())
        tokens = [token for token in tokens if token not in russian_stopwords \
                  and token != " " \
                  and token.strip() not in punctuation]
        tokens = [token for token in tokens if token.isalpha() and len(token) > 1]
    finish = t.time()
    print(f"the doc is lemmatized in {start - finish} secs")

    #opening the json with all the frequencies of words from NCRL and counting the length of the corpora
    start = t.time()
    with open("frequencies.json") as doc:
        corpora = json.load(doc)
        corp_total = 0
        for i in corpora:
            corp_total += corpora[i]
    finish = t.time()
    print(f"frequencies.json are open and ready to be used in {start - finish} secs")
    print(corpora["солнце"])

    start = t.time()
    doc_frqn = {}
    corp_frqn = {}

    for token in tokens:
        doc_frqn[token] = tokens.count(token) / len(tokens)
        try:
            corp_frqn[token] = corpora[token] / corp_total
        except KeyError:
            corp_frqn[token] = 0
    finish = t.time()
    print(f"numbers of entrances is calculated succesfully in {finish - start} secs")

    expected = {}
    for token in doc_frqn.keys():
        a = doc_frqn[token]
        b = corp_frqn[token]
        c = 1 - a
        d = 1 - b
        expected[token] = ((a + b) * (a + c)) / (a + b + c + d)

    print("expected frequency is calculated successfully ")

    chi = {}
    for token in expected.keys():
        o = doc_frqn[token]
        e = expected[token]
        chi[token] = ((o - e) ** 2) / e

    l = list(chi.items())
    l.sort(key=lambda i: i[1])
    l = l[::-1]
    print("chi2 value is calculated successfully")
    print(l)

    Q = 0.003932

    kw = []
    for i in l:
        if i[1] <= Q:
            kw.append(i[0])
    print("keywords list is formed")
    print("keywords function is finished")
    print(" ".join(kw))
    return(kw, tokens)


def main():
    bot = Bot(
        token=TOKEN,
        base_url=PROXY,  # delete it if connection via VPN
    )
    updater = Updater(bot=bot, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.document, get_file))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    print("Bot is started")
    main()
