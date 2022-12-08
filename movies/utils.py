from enum import Enum
from typing import Optional

from .promos import BackToTheFuture, BackToThePresent


NON_SAGA_PRICE = 20

class PromoSaga(Enum):
    """
    Active Promos:
    This is done to enable the addition of future sagas easy. Could be replaced by a database too.
    Also, Every entry value should be a class. Makes the code more generic
    """

    BACK_TO_THE_FUTURE = BackToTheFuture
    BACK_TO_THE_PRESENT = BackToThePresent

def calculate_price(movies_bought: Optional[str]) -> float:
    cart = movies_bought.split("\n")
    movies_list = [item.lower().strip() for item in cart if item.strip() != ""]

    if len(movies_list) == 0:
        return -1

    # loop over active promos and calculate price
    other_movies = movies_list
    promo_price = 0

    for saga in list(PromoSaga):
        promo_saga = saga.value(other_movies)
        promo_price += promo_saga.calculate_price()
        other_movies = promo_saga.other_movies()

    # Add 20 to total for every item not on promo
    total_price_of_other_movies = NON_SAGA_PRICE * len(other_movies)
    final_price = total_price_of_other_movies + promo_price
    return round(final_price, 2)
