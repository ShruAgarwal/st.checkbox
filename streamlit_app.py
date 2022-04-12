import streamlit as st

st.title('**st.checkbox**')
st.write('*Displays a checkbox widget*')

st.subheader('Which combo would you like to order?')


st.write('Pick your favorite meal!')
option_1 = st.checkbox('Cheeseburger 🍔 + Fries 🍟 + Sprite 🧃')
option_2 = st.checkbox('Sausage Burrito 🌯 + Coca-cola 🥤')
option_3 = st.checkbox('Chicken Sandwich 🥪 + Fanta orange 🍊🧃')
option_4 = st.checkbox('Pasta Pizza 🍕 + Garlic Bread + Mango Pineapple smoothie 🥭🍍🧃')


if option_1:
     st.write('Your order is ready! 🍔🍟🧃')
if option_2:
     st.write('Here you go 🌯🥤😉 ')
if option_3:
     st.write('It is ready! Enjoy 🥪🍊🧃')
if option_4:
     st.write('Enjoy your meal 🍕🥭🍍🧃')
