# Case-study #5
# Developers:
# Marinkin O. (37%),
# Seledtsov A. (36%),
# Evdischenko M. (68%)

import urllib.request
from prettytable import PrettyTable

tb = PrettyTable()
a = []
b = []
with open('urls.txt') as urls:
    for i in urls:
        b = []
        url = i
        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find("nfl-c-player-header__title")
        name = text[text.find('>', part_name) + 1:text.find('</h1', part_name)]
        b.append(name)
        text = text.replace(' ','')
        text_find1 = text.find('passingCompletions"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        text_find1 = text.find('passingAttempts"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        text_find1 = text.find('passingYards"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        text_find1 = text.find('passingTouchdowns"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        text_find1 = text.find('passingInterceptions"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        text_find1 = text.find('passingPasserRating"scope="col">')
        text_find2 = text.find('/th', text_find1)
        comp = text[text_find1:text_find2:1]
        comp = comp[(comp.find('>') + 3):(comp.rfind('<') - 2)]
        b.append(comp)
        a.append(b)


with open('output.txt', 'w') as f_out:
    tb.field_names = ['NAME', 'COMP', 'ATT', 'YDS', 'TD', 'INT', 'PR']
    for i in range(len(a)):
        tb.add_row([a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6]])
    print(tb, file=f_out)
