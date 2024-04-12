import psycopg2
import streamlit as st
from services.get_city_names import city_names
try:
    conn = psycopg2.connect(
        dbname = st.secrets['database']['dbname'],
        user =st.secrets['database']['user'],
        password = st.secrets['database']['password'],
        host=st.secrets['database']['host'],
        port=5432

    )
    cursor = conn.cursor()
    print("connection successfull")
except  psycopg2.Error as e:
    print(f"unable to connect {e}")

st.title("encyclopida of city")

city_names_list=city_names(cursor)
selected_city=st.selectbox('Select a city from the list',city_names_list)
st.write('you have selected ',selected_city)