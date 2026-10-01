import csv
import random

file_path = 'data/raw/steam_games.csv'

with open(file_path, newline='', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    header = reader[0]
    dados = reader[1:]

amostra = random.sample(dados, 20)

with open('data/sample/steam_games_sample.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(amostra)