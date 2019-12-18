import requests
from bs4 import BeautifulSoup

SCHOOLS = []
SHORTNAME = []
TEAM = []
CONFERENCE = []

URL = "https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions"
RESPONSE = requests.get(URL)

SOUP = BeautifulSoup(RESPONSE.text, "html.parser")

SCHOOLS_TABLE = SOUP.find('table',{'class':'sortable'})

# print(SCHOOLS_TABLE)

for row in SCHOOLS_TABLE.find_all('th'):
    if row.a is not None:
        if row.a.get('title') is not None:
            print(row.a.get('title'))

# soup.findAll('tr')

# for row in SCHOOLS_TABLE.find_all('th'):
#     if row.a is not None:
#         if row.a.get('title') is not None:
#             SCHOOLS.append(row.a.get('title'))