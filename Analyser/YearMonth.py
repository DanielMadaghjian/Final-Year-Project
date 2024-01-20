class YearMonth:
    def __init__(self, year,month):
        self.year = year
        self.month = month
    def __eq__(self, other):
        return isinstance(other, YearMonth) and self.year == other.year and self.month == other.month

    def __hash__(self):
        return hash((self.year, self.month))