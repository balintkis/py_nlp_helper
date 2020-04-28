import fileinput
import re
import os
import glob

data_folder = glob.glob("2-lepes-bigram1/*.txt")

count = 0
list_ofnames = []
nevek=''
with open('nevek-linebreaks.txt', 'r') as reader:
    for line in reader:
        list_ofnames.append(line)
        nevek+=line.rstrip()+'|'
        count += 1

nevek = nevek[:-1] #az utolsó karaktert, azaz: |-t szedi le, ami már felesleges

compiled_pattern = re.compile(f'([A-ZÁÉÚÖŐÜŰ]{{1}}[a-záéúőóüö]*?) ({nevek})')

with fileinput.FileInput(data_folder, inplace=1, backup='.bak') as file:
    for line in file:
        print(re.sub(compiled_pattern, r'\1_\2', line), end='')
