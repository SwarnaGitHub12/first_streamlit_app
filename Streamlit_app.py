import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfasrlt Favorites')
streamlit.text('🍵Omega 3 & blueberry oatmeal')
streamlit.text('🌮kale,spinach & rocket smoothie')
streamlit.text('🥚Hard boiled free range egg')
streamlit.header('🍌🍓 Build your own fruit smoothie 🫐🥝')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
