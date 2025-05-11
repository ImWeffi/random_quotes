import requests
from bs4 import BeautifulSoup
import random

top_tags = [
    "love", "inspirational", "life", "humor", "books",
    "reading", "friendship", "friends", "truth", "simile"
]

print("pieejamās tēmas:")
for idx, tag in enumerate(top_tags, 1):
    print(f"{idx}. {tag}")

izvele = input("ievadi tēmas numuru (1–10): ")

try:
    izvele = int(izvele)
    if 1 <= izvele <= len(top_tags):
        izveletais_tag = top_tags[izvele - 1]
    else:
        print("nepareizs numurs. izvēlies no 1 līdz 10.")
        exit()
except ValueError:
    print("lūdzu, ievadi skaitli.")
    exit()

adrese = f"https://quotes.toscrape.com/tag/{izveletais_tag}/"
lapa = requests.get(adrese)

if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    citatu_bloki = lapas_saturs.find_all(class_="quote")

    if citatu_bloki:
        citatas = []
        for bloks in citatu_bloki:
            teksts = bloks.find(class_="text").get_text()
            autors = bloks.find(class_="author").get_text()
            citatas.append((teksts, autors))
        citata, autors = random.choice(citatas)
        print(f"\n💬 {citata}\n— {autors}")
    else:
        print("nav atrastas citātes ar šo tēmu.")
else:
    print(f"kļūda: nevar piekļūt lapai. Statusa kods: {lapa.status_code}")