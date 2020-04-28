import glob
import re

data_folder = glob.glob("5-lepes-bigram2/*.txt")
nevek = ''

with open('nevek-linebreaks.txt', 'r') as reader:
    for line in reader:
        nevek+=line.rstrip()+'|'

nevek = nevek[:-1] #az utolsó karaktert, azaz: |-t szedi le, ami már felesleges

regex_names_noncapturing = re.compile(f'[A-ZÁÉÚÖŐÜŰ]{{1}}[a-záéúőóüö]*?_(?:{nevek})')
regex_names_capturing = re.compile(f'([A-ZÁÉÚÖŐÜŰ]{{1}}[a-záéúőóüö]*?)_({nevek})')

for file in data_folder:
    with open(file, 'r') as article:
        article = article.read()
    nevek_listaja = set(regex_names_noncapturing.findall(article))
    for nev in nevek_listaja:
        #a teljes alakos személynevek ragozásait is letisztítjuk
        regex_teljesnev = re.compile(f'{nev}[a-záéúőóüö]+') 
        teljes_nevek = set(regex_teljesnev.findall(article))
        for teljesnev in teljes_nevek:
            article = article.replace(teljesnev, nev)

        #kicseréljük a csaladneveket teljes nevekre
        csaladnev = regex_names_capturing.search(nev).group(1)
        if sum(csaladnev in s for s in nevek_listaja) == 1:
            article = article.replace(csaladnev+" ", nev+" ")
            article = article.replace((csaladnev+" ").lower(), nev+" ")

    with open(file, 'w') as file:
        file.writelines(article)
