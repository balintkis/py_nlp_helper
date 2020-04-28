import fileinput
import re
import os
import glob
import requests
import sys

data_folder = glob.glob("4-lepes-lemma/*.txt")
compiled_pattern_lemma = re.compile(r'.*?\[{"lemma": "(.*?)".*?')
compiled_pattern_no_lemma = re.compile(r'(.*?)\t"')

for file in data_folder:    
    stringbuilder = []                                   
    lemmatized_result = requests.post('http://127.0.0.1:5000/tok/morph/pos', files={'file': open(file, encoding='UTF-8')})    
    lemmatized_result = lemmatized_result.text.splitlines(True)[1:] #első sort törli (másodiktól sortól az összeset írja be)
    filtered = filter(lambda x: not re.match(r'^\s*$', x), lemmatized_result) #üres sorok törlése

    for lines in filtered:
        if '\"lemma\"' in lines:
            stringbuilder.append(compiled_pattern_lemma.search(lines).group(1))
        else:
            stringbuilder.append(compiled_pattern_no_lemma.search(lines).group(1))
    
    finished_string = " ".join(stringbuilder)
    with open(file, 'w') as feldolgozott_file_ki:
        feldolgozott_file_ki.writelines(finished_string)
