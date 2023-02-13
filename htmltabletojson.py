from bs4 import BeautifulSoup as bs
import sys
import mimetypes
import json

def table(table):
    soup = bs(table,'lxml')

    table = soup.find('table')
    if not table:
        print("No tables found! ")
        return

    tablejs = []

    cols = [th.text.strip() for th in table.find('thead').find_all('tr')]
    rows = []
    for th in table.find('tbody').find_all('tr'):
        r = [t.text().strip() for t in  th.find_all('td')]
        tablejs.append(dict(zip(cols,r)))

    return json.loads(tablejs, indent=4)

def mime(url):
    return mimetypes.guess_type(url)[0]

if len(sys.argv) > 1 and mime(sys.argv[-1]) == 'text/html':
    with open(sys.argv[-1].strip('"'),'r') as r:
        table(r.read())