from steam_analysis.load_csv import read_csv_path
from steam_analysis.insert_df_class import parse_games
from steam_analysis.calculate_questions import CalculateQuestions

calculates = CalculateQuestions()

# Import CSV AND Apply dataframe in Class Games

steam_games = read_csv_path("data/raw/steam_games.csv")
games = parse_games(steam_games)

for g in games:
    calculates.add_game(g)

# Answer the question 1)

print(f"Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?")

free_games, paid_games = calculates.perc_paid_vs_free()
print(f"Quantidade de jogos gratuitos: {free_games:.2f}%")
print(f"Quantidade de jogos pagos: {paid_games:.2f}%")


# Answer the question 2)

print(f"Pergunta 2: Qual o ano com o maior número de novos jogos?")

top_year_release = calculates.year_with_most_releases()
print(f"Ano com mais lançamentos: {top_year_release}")


# Answer the question 3)

print(f"Pergunta 3: Qual o gênero mais popular?")

genres_most_popular = calculates.most_common_genre()
print(f"Gênero mais popular: {genres_most_popular }")