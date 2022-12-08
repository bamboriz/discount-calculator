import streamlit as st
from movies.utils import calculate_price

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
    price = calculate_price(movies_bought)
    if price < 0:
        st.write("Désolé, votre panier de films est vide. Veuillez ajouter des films au panier.")
    else:
        st.write("Total Price: {} €".format(price))
