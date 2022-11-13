# Contains all the classes for Promos


class BackToTheFuture:
    """
    This contains all the logic for computing the price of the Back to the future promo saga.
    Other promo saga classes can be added easily without many changes to the code base"""

    def __init__(self, items) -> None:
        self.items = items
        self.name = "back to the future"

    def promo_movies(self) -> list:
        # Gets the movies that belong to the promo
        return [item for item in self.items if self.name in item]

    def other_movies(self) -> list:
        # Gets movies that are NOT in the promo
        return [item for item in self.items if self.name not in item]

    def calculate_price(self) -> float:
        # Compute 15 x number of BTF DVDs = Total BTF
        total_price = 15 * len(self.promo_movies())

        distinct_saga_items = list(set(self.promo_movies()))

        discount = 0
        if len(distinct_saga_items) == 3:
            # if 3 different apply 20% discount to Total BTF
            discount = 0.2
        elif len(distinct_saga_items) == 2:
            # if 2 different apply 10% discount to Total BTF
            discount = 0.1

        return total_price * (1 - discount)
