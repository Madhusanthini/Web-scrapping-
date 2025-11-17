import requests
from bs4 import BeautifulSoup
import csv
import datetime

def get_html(link):
    try:
        r = requests.get(link, timeout=10)
        return r.text
    except:
        return None

def get_titles(page):
    soup = BeautifulSoup(page, "html.parser")
    out = []
    for tag in ["h1", "h2", "h3"]:
        for i in soup.find_all(tag):
            t = i.get_text().strip()
            if len(t) > 5:
                out.append(t)
    out = list(dict.fromkeys(out))
    return out

def save_txt(data, name):
    with open(name, "w", encoding="utf-8") as f:
        for i in data:
            f.write(i + "\n")

def save_csv(data, name):
    with open(name, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["No", "Headline"])
        for n, h in enumerate(data, start=1):
            w.writerow([n, h])

print("News Scraper")
site = input("Enter news link: ")

html = get_html(site)
if not html:
    print("Could not fetch website.")
    exit()

titles = get_titles(html)
if not titles:
    print("No headlines found.")
    exit()

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
txtname = "news_" + time + ".txt"
csvname = "news_" + time + ".csv"

save_txt(titles, txtname)
save_csv(titles, csvname)

print("Saved:", txtname, "and", csvname)