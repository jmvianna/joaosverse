import streamlit as st

st.title("joaosverse version 1")

st.image("https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2808031_bx.webp?w=760&h=434")

if st.button("quem é joão vianna?"):
    st.switch_page("2.py")

if st.button("interesses"):
    st.switch_page("3.py")
