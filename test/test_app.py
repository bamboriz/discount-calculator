import pytest
from movies.utils import PromoSaga, calculate_price


test_data = [
    (
        """
                Back to the Future 1
                Back to the Future 2
                Back to the Future 3
                La chèvre
                """,
        56.00,
    ),
    (
        """
                Back to the Future 1
                Back to the Future 3
                """,
        27.00,
    ),
    ("""Back to the Future 1""", 15.00),
    (
        """Back to the Future 1
                Back to the Future 2
                Back to the Future 3
                Back to the Future 2""",
        48.00,
    ),
    (
        """
                Back to the Future 1
                Back to the Future 2
                Back to the Future 3""",
        36.00,
    ),
]


@pytest.mark.parametrize("cart, expected_price", test_data)
def test_calculate_price(cart, expected_price):
    assert calculate_price(cart, PromoSaga.BACK_TO_THE_FUTURE) == expected_price
