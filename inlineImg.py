import requests
from bs4 import BeautifulSoup
from uuid import uuid4
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_data(num):
    url = "https://dodopizza.uz/tashkent?product=000D3A240C71BE9A11E719C09475693B"

    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    div = soup.findAll("div", attrs={"class":"sc-15fdqut-10 jXeUMg"})[num]
    name = div.find('a', attrs={'class': ["sc-15fdqut-12 jLNDwH"]})
    link = name.attrs['data-src']
    about = "https://dodopizza.uz/" + name.attrs['href']
    # < span

    # class ="sc-15fdqut-12 jLNDwH" > Четыре сезона < / span >

    # div_info = soup.findAll("div", attrs={"class": "proposal-main-info-wrap"})[num]
    # name_href = div.find("a", attrs={"class": "proposal-item-link"})
    # span = name_href.select("span")
    # name = span[0].text
    #
    # div_price = soup.findAll("div", attrs={"class": ["proposal-price_wrap", "text-overflow"]})[num]
    # href = div_price.find("div", attrs={"proposal-main-price"})
    # price = href.select("span.proposal-price-value")[0].text
    # valyuta = href.select("span.proposal-price-currency")[0].text

    data = {
        "name": name,
        "link": link,
        "price": price + " " + valyuta,
        "about": about
    }

    return data


phones = []
for i in range(4, 15):
    phones.append(get_data(i))

data_phones = []
for phone in phones:
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📌 Batafsil", url = phone["about"]),
            InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="phone")
        ]
    ])
    data_phones.append(
        types.InlineQueryResultPhoto(
            id = str(uuid4()),
            photo_url = phone['link'],
            thumb_url = phone['link'],
            title = phone['name'],
            caption = f"<b>{phone['name']}</b>\n<b>Narxi: {phone['price']}</b>",
            parse_mode = "html",
            reply_markup = menu
        ),
    )