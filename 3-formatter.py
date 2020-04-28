import glob

data_folder = glob.glob("3-lepes-format/*.txt")
print(data_folder)

for file in data_folder:                                       
    with open(file, 'r') as fin:
        article = fin.read().replace(r'\"', r'"') #escaped idézőjelek lecserélése sima idézőjelekre
        data = article.splitlines(True) #cikk sorokra bontása 
        data[-1] = data[-1][:-2]+"\n" #utolsó idézőjelet kiveszi a file végéről (utolsó karakter newline, utolsó előtti ", newlinet visszarakja)
        data[1] = data[1].replace(r'"1" "', '', 1) #első idézőjelet-stb kiveszi a file elejéről
    with open(file, 'w') as fout:
        fout.writelines(data[1:]) #első sort törli (második sortól az összeset írja be)
