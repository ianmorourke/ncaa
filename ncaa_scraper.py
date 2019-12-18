import requests
from bs4 import BeautifulSoup

SCHOOLS = []
SHORTNAME = []
TEAM = []
CONFERENCE = []

URL = "https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions"
RESPONSE = requests.get(URL)

SOUP = BeautifulSoup(RESPONSE.text, "html.parser")

SCHOOLS_TABLE = SOUP.find('table', {'class':'sortable'})

rows = SCHOOLS_TABLE.find_all('tr')

first_columns = []
third_columns = []
for row in rows[1:]:
    first_columns.append(row.find_all('th')[0])
    third_columns.append(row.find_all('td')[2])

for first, third in zip(first_columns, third_columns):
    print(first.text, third.text)

# for row in SCHOOLS_TABLE.tbody.find_all('th'):
#     if row.a is not None:
#         if row.a.get('title') is not None:
#             SCHOOLS.append(row.a.get('title'))

# for row in SCHOOLS_TABLE.tbody.find_all('tr'):
#     first_column = row.find_all('td')[2].contents
#     print(first_column)