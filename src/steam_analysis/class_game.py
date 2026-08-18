class Games:
    """
    Represents a game with its basic attributes.

    Examples:
        >>> g = Games("Chess", "2020-01-01", 0.0, True)
        >>> g.is_paid()
        False
    """
    try:
        def __init__(self, name, release_date, price, is_free, genres):
            self.name = name
            self.release_date = release_date
            self.price = price
            self.genres = genres
            self.is_free = is_free

        def is_paid(self):
            return not self.is_free
    except TypeError as e:
        raise ValueError(f"Invalid entryes for some attributes: {e}")
