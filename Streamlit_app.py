import streamlit

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🍵Omega 3 & blueberry oatmeal')
streamlit.text('🌮kale,spinach & rocket smoothie')
streamlit.text('🥚Hard boiled free-range egg')
streamlit.text('🥑🍞 avacado toast')

streamlit.header('🍌🍓 Build your own fruit smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)
