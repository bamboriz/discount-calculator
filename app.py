import streamlit as st
from movies.utils import PromoSaga, calculate_price

st.title("Forward to the Past")

movies_bought = st.text_area(
    "Entrez, un panier sous forme de texte, séparé par des retours à la ligne qui contient le nom des films achetés",
    height=200,
    placeholder="""
    Back to the Future 1
    Back to the Future 2
    Back to the Future 3
    """,
)

if st.button("Calculate"):
    price = calculate_price(movies_bought, PromoSaga.BACK_TO_THE_FUTURE)
    st.write("Total Price: {} €".format(price))
