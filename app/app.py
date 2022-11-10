import streamlit as st
from utils import calculate_price

st.title('Forward to the Past')

txt = st.text_area('Input', height=200, placeholder='''
    Back to the Future 1
    Back to the Future 2
    Back to the Future 3
    ''')
if st.button('Calculate Price'):
    # st.write('Total Price:', calculate_price(txt))
    cart = txt.split("\n")
    cart = [item for item in cart if item.strip() != '']
    print(cart)
    price = calculate_price(cart, promo_saga='Back to the Future')
    st.write('Total Price:', str(price) + ' €')

# order = ['Back to the Future 1', 'Back to the Future 2', 'Back to the Future 3', 'La chèvre']
# calculate_price(order, 'Back to the Future')
