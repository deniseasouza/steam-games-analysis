from .class_game import Games

def parse_games(rows):
    """
    Parses a list of dictionaries representing game data and returns a list of Games objects.

        >>> rows = [
        ...     {"Name": "Game A", "Release date": "2022-01-01", "Price": "0.0"},
        ...     {"Name": "Game B", "Release date": "2023-05-10", "Price": "19.99"}
        ... ]
        >>> parse_games(rows)
        [Games(name='Game A', release_date='2022-01-01', price=0.0, is_free=True), Games(name='Game B', release_date='2023-05-10', price=19.99, is_free=False)]
    """
    try:
        games = []
        for row in rows:
            game = Games(
                name=row["Name"],
                release_date=row["Release date"],
                price=float(row["Price"]),
                genres=row["Genres"],
                is_free=(row["Price"] == "0.0")
            )
            games.append(game)
        return games
    except KeyError as e:
        raise ValueError(f"Missing key in row data: {e}")