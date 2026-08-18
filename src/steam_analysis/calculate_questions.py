class CalculateQuestions:
    """
    Class to perform calculations and answer questions about a collection of games.

    Example:
        >>> class Game:
        ...     def __init__(self, is_free, release_date):
        ...         self.is_free = is_free
        ...         self.release_date = release_date
        >>> cq = CalculateQuestions()
        >>> cq.add_game(Game(True, '01-01-2020'))
        >>> cq.add_game(Game(False, '01-01-2021'))
        >>> cq.perc_paid_vs_free()
        (50.0, 50.0)
        >>> cq.year_with_most_releases()
        ['2020', '2021']
    """
    try:
        def __init__(self):
            self.games = []

        def add_game(self, game):
            self.games.append(game)

        def perc_paid_vs_free(self):
            free = sum(1 for g in self.games if g.is_free)
            total = len(self.games)
            return (free / total * 100, (total - free) / total * 100)

        def year_with_most_releases(self):
            years = {}
            for game in self.games:
                year = game.release_date[-4:]
                years[year] = years.get(year, 0) + 1
            max_count = max(years.values())
            return [y for y, c in years.items() if c == max_count]
        
        def most_common_genre(self):
            genres = {}
            for game in self.games:
                if hasattr(game, 'genres') and game.genres:
                    for genre in game.genres.split(','):
                        genre = genre.strip()  # Remove espaços
                        genres[genre] = genres.get(genre, 0) + 1

            if not genres:
                return None

            max_count = max(genres.values())
            return [g for g, c in genres.items() if c == max_count]
            
    except TypeError as e:
        print(f"Error: Invalid data type encountered - {e}")
