import skill
import bs4
import urllib.request
import urllib.parse
import util

url = "https://monster-sanctuary.fandom.com"
links = ["/wiki/Category:Skill", "/wiki/Category:Skill?from=Health+Focus+%28Passive%29",
         "/wiki/Category:Skill?from=Water+Affinity+%28Passive%29", "/wiki/Category:Skills"]


# A list of skills
def get_skills():
    found = []
    for link in links:
        soup = bs4.BeautifulSoup(urllib.request.urlopen(url + link).read(), features="html.parser")
        table = soup.find("div", {"class": "category-page__members"})
        found += table.find_all("a")
    return scrape_shifts(found)


def scrape_shifts(links):
    found = []
    tested = []
    for element in links:
        link = element['href']
        if link is None or link.startswith("#") or link in tested:
            continue
        try:
            skill = read_skill(url + link)
            print(skill.to_dict())
            found.append(skill)
            tested.append(link)
        except:
            print("Failed for: " + url + link)
    return found


def read_skill(skill_url):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(skill_url).read(), features="html.parser")

    name = urllib.parse.unquote(skill_url[len(url)+len("/wiki/"):].replace("_", " ").rsplit(' ', 1)[0])
    categories = util.get_categories(soup)

    if "Ultimate Skill" in categories or "Damage Skills" in categories or "Support Skills" in categories:
        return get_ability_skill(soup, categories, name, "Ultimate Skill" in categories)

    return get_passive_skill(soup, name)


def get_ability_skill(soup, categories, name, ultimate):
    table = soup.find("table", {"class": "blueborder"}).find("tbody")
    if ultimate:
        description = str(table.find_all("tr")[2].find_all("td")[1])
    else:
        description = {}
        i = 1
        for element in table.find_all("tr")[1:-1]:
            description[i] = str(element.find("td", {"align": "left"}))
            i += 1

    image = table.find_all("tr")[1].find("td").find("img")['src']
    monsters = util.find_monsters(soup)
    physical = False
    element = None
    for category in categories:
        if "Physical" in category:
            physical = True
        if util.is_element(category):
            element = category

    return skill.AbilitySkill("Damage Skills" in categories, name,
                              description, monsters, element, physical, image, ultimate)


def get_passive_skill(soup, name):
    monsters = util.find_monsters(soup)
    table = soup.find("table", {"class": "blueborder"}).find("tbody")
    description = str(table.find_all("tr")[1].find_all("td")[1])
    image = table.find_all("tr")[1].find("td").find("img")['src']
    return skill.PassiveSkill(name, description, image, monsters)
