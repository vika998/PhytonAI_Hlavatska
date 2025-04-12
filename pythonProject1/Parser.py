# https://web.telegram.org/a/#8167777523
from bs4 import BeautifulSoup
import requests
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

# print(links_list)
f = open('info.txt', 'w', encoding='utf-8')
list_name = []
list_desc = []
for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)

f.close()
command = """/last - останній фільм зі списку
/first - перший фільм зі списку
/search - пошук фільму за назвою
/genre - рекомендація за жанром
/random - 3 випадкових фільмів
/help - список всіх команд бота
/hello - привітання,
/film - список фільмів"""


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)


async def random_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    indices = random.sample(range(len(list_name)), k=min(3, len(list_name)))
    for i in indices:
        await update.message.reply_text(f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}")


async def genre(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        genre_query = ' '.join(context.args).lower()
        for i in range(len(list_desc)):
            if genre_query in list_desc[i].lower():
                await update.message.reply_text(f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}")
    else:
        await update.message.reply_text("Введи жанр після команди. Наприклад: /genre комедія")


async def search_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        search_query = ' '.join(context.args).lower()
        found = False
        for i in range(len(list_name)):
            if search_query in list_name[i].lower():
                await update.message.reply_text(f"Знайдено:\n{list_name[i]}\n{list_desc[i]}\n{links_list[i]}")
                found = True
        if not found:
            await update.message.reply_text(f"Фільм з назвою '{search_query}' не знайдено.")
    else:
        await update.message.reply_text("Введи назву фільму після команди. Наприклад: /search майнкрафт")


async def first_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if list_name:
        await update.message.reply_text(f"Перший фільм у списку:\n{list_name[0]}\n{list_desc[0]}\n{links_list[0]}")


async def last_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if list_name:
        last_index = len(list_name) - 1
        await update.message.reply_text(f"Останній фільм у списку:\n{list_name[last_index]}\n{list_desc[last_index]}\n{links_list[last_index]}")


app = ApplicationBuilder().token("8167777523:AAHFXMOXPeh5FTpxE_ias_HeTnJAPbwMI8U").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help",menu))
app.add_handler(CommandHandler("random", random_film))
app.add_handler(CommandHandler("genre", genre))
app.add_handler(CommandHandler("search", search_film))
app.add_handler(CommandHandler("first", first_film))
app.add_handler(CommandHandler("last", last_film))

app.run_polling()