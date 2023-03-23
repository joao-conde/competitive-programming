class FilterStrategy:
    def filter(self, val):
        pass


class FilterPositives(FilterStrategy):
    def filter(self, val):
        return val > 0


class FilterNegatives(FilterStrategy):
    def filter(self, val):
        return val < 0


def filter(values, strategy: FilterStrategy):
    return [x for x in values if strategy.filter(x)]


filter([0, -1, -10, 1, 2, 3], FilterPositives())
filter([0, -1, -10, 1, 2, 3], FilterNegatives())
