import streamlit as st

st.title("joaosverse version 1")

st.image("https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2808031_bx.webp?w=760&h=434")
    
opcao = st.selectbox("quem é joão vianna?:", ["definição", "interesses"])

if opcao == "definição":
    st.write("Informações de contato aqui")

if opcao == "Mais":
    st.write("Mais informações aqui")
