import bs4
import urllib.request
import urllib.parse
from monster import *

url = "https://monster-sanctuary.fandom.com"


def get_monsters(shift_skills, skills):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url + "/wiki/Monsters").read(), features="html.parser")
    table = soup.find_all("table", {"class": "monstertable"})
    found = []
    for element in table[0].find_all('tr'):
        link = element.find('a')
        if link is None or link['href'] == "/wiki/Template:Monsters":
            continue
        monster = scrape_monster(url + link['href'], shift_skills, skills)
        print(monster.to_dict())
        found.append(monster)
    return found


def scrape_monster(monster_url, shift_skills, monster_skills):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(monster_url).read(), features="html.parser")
    name = urllib.parse.unquote(monster_url[len(url) + len("/wiki/"):].replace("_", " "))
    table = soup.find("div", {"class": "monsterbox blueborder"}).find("table").find("tbody").find("tr")
    overview = table.find("td")
    image = overview.find_all("div", recursive=False)[2].find("img")['data-src']

    weaknesses = []
    resistances = []
    for element in overview.find_all("table", recursive=False)[1].find("tbody").find("tr").find("td").find(
            "div").find_all("div"):
        found = element.find("a")['title']
        element = found.split(" ")[0]
        if "Weakness" in found:
            weaknesses.append(element)
        else:
            resistances.append(element)

    elements = []
    for element in overview.find_all("table", recursive=False)[2].find("tbody").find("tr").find("td").find(
            "div").find_all("div"):
        elements.append(element['title'])

    dossier = table.find_all("td", recursive=False)[1].find("table").find("tbody").find("tr").find("td").find(
        "table").find("tbody")
    images = dossier.find("tr")

    location = []
    for element in dossier.find_all("tr", recursive=False)[5].find("td").find_all("span"):
        location.append(element.text)

    stat_tables = dossier.find_all("tr", recursive=False)[1].find_all("td", recursive=False)
    ability_light = get_passive(shift_skills["light"], dossier.find_all("tr", recursive=False)[3].find("b").text)
    ability_dark = get_passive(shift_skills["dark"], dossier.find_all("tr", recursive=False)[4].find("b").text)

    skills = get_skills(soup, monster_skills)

    stats = get_stats(stat_tables[0], False)
    stats_light = get_stats(stat_tables[1], True)
    stats_dark = get_stats(stat_tables[2], True)
    return Monster(name,
                   image, images.find_all("td", recursive=False)[1].find("img")['data-src'],
                   images.find_all("td", recursive=False)[2].find("img")['data-src'],
                   location, stats, stats_light, stats_dark,
                   ability_light, ability_dark, skills, weaknesses, resistances, elements)


def get_skills(soup, monster_skills):
    skills = []
    load_skills(skills, soup.find_all("table", {"class": "skilltreesingletable"}), monster_skills)
    load_ultimates(skills, soup.find("table", {"class": "skilltreetable"}).find("tbody").find_all("tr", recursive=False)[1].find_all("td", {"class": "skillcell"}), monster_skills)
    return skills


levels = [1, 1, 10, 20, 30]


def load_skills(skills, elements, monster_skills):
    for skill in elements:
        found = {}
        i = 0
        for row in skill.find_all("td", {"class": "skillrowcell"}):
            found_skills = []
            for element in row.find_all("td", {"class": "skillcell"}):
                found_skills.append(get_passive(monster_skills, urllib.parse.unquote(element.find("a")['title'].rsplit(' ', 1)[0])))

            cell_list = found.get(levels[i], [])
            cell_list.append(found_skills)
            found[levels[i]] = cell_list
            i += 1
        skills.append(found)


def load_ultimates(skills, element, monster_skills):
    ultimates = []
    for skill in element:
        ultimates.append(get_passive(monster_skills, urllib.parse.unquote(skill.find("a")['title'].rsplit(' ', 1)[0])))
    skills.append(ultimates)


def get_stats(parent_element, additional):
    found = []
    for element in parent_element.find_all("tr"):
        if additional:
            found.append(element.find_all("td", recursive=False)[1].find("div").find("span").text.strip())
        else:
            found.append(element.find_all("td", recursive=False)[1].find("div").text.strip())
    stats = Stats(found)
    return stats.to_dict()


def get_passive(choices, name):
    i = 0
    for choice in choices:
        if choice["name"] == name:
            return i
        i += 1
    print("Failed for " + name)