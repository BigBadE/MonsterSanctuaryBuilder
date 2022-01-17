from shift import Shift
import bs4
import urllib.request
import util

url = "https://monster-sanctuary.fandom.com"


# A dictionary of two lists (light and dark), each list contains the abilities
def get_shifts():
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url + "/wiki/Monster_Shifting").read(), features="html.parser")
    table = soup.find_all("table", {"class": "table-whiteborder"})
    return {"light": scrape_shifts(table[0]), "dark": scrape_shifts(table[1])}


def scrape_shifts(table):
    found = []
    for element in table.find_all('tr'):
        link = element.find('a')
        if link is None:
            continue
        found.append(read_shift(url + link['href']))
    return found


def read_shift(url):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
    table = soup.find("table", {"class": "whiteborder"}).find("tbody").find_all("tr")[1]
    name = table.find("td").find("span").text
    description = str(table.find_all("td")[1].find())
    monsters = util.find_monsters(soup)
    return Shift(name, description, monsters)
