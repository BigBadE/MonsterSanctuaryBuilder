def get_categories(soup):
    category_div = soup.find("div", {"class": "page-header__categories"})
    categories = []
    for element in category_div.find_all("a"):
        if "more" not in element.text:
            categories.append(element.text)
    return categories


def find_monsters(soup):
    table = soup.find_all("table", {"class": "monstertable"})
    found = []
    for element in table[0].find_all('tr'):
        number = element.find('td')
        if number is None:
            continue
        found.append(number.text[:-1])
    return found


def is_element(name):
    return name == "Water" or name == "Wind" or name == "Fire" or name == "Earth" or name == "Neutral"
