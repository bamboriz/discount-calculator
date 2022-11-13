from enum import Enum
from typing import Optional

from .promos import BackToTheFuture


class PromoSaga(Enum):
    """
    This is done to enable the addition of future sagas easy. Could be replaced by a database too.
    Also, Every entry value should be a class. Makes the code more generic
    """

    BACK_TO_THE_FUTURE = BackToTheFuture


def calculate_price(movies_bought: Optional[str], promo_saga: PromoSaga) -> float:
    cart = movies_bought.split("\n")
    movies_list = [item.lower() for item in cart if item.strip() != ""]

    if len(movies_list) == 0:
        return "Désolé, votre panier de films est vide. Veuillez ajouter des films au panier."

    saga = promo_saga.value(movies_list)

    # Add 20 to total for every item not BTF = Total Not BTF
    total_price_of_other_movies = 20 * len(saga.other_movies())
    final_price = total_price_of_other_movies + saga.calculate_price()
    return round(final_price, 2)
