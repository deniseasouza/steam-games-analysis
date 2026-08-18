import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from steam_analysis.load_csv import read_csv_path
from steam_analysis.insert_df_class import parse_games
from steam_analysis.calculate_questions import CalculateQuestions

calculate = CalculateQuestions()

def test_full():
    def load_csv():
        csv_file = read_csv_path(ROOT / "data" / "sample" / "steam_games_sample.csv")
        assert csv_file is not None
        return csv_file

    def example_parse_games(csv_file):
        games = parse_games(csv_file)
        assert games is not None
        return games

    def calculate_questions_func(games):
        for g in games:
            calculate.add_game(g)

        perc_free, perc_paid, = calculate.perc_paid_vs_free()
        assert perc_paid is not None and perc_free is not None
        # print(f"Quantidade de jogos gratuitos: {perc_free:.2f}%")
        # print(f"Quantidade de jogos pagos: {perc_paid:.2f}%")

        top_year_release = calculate.year_with_most_releases()
        assert top_year_release is not None
        # print(f"Ano com mais lançamentos: {top_year_release}")

    def test_most_common_genre():
        genres = calculate.most_common_genre()
        assert genres is not None
        print(f"Gênero mais comum: {genres}")



    csv_file = load_csv()
    games = example_parse_games(csv_file)
    calculate_questions_func(games)
    test_most_common_genre()

test_full()

