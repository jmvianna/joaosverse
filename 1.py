import streamlit as st

st.title("joaosverse version 1")

st.image("https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2808031_bx.webp?w=760&h=434")
    
opcao = st.selectbox("quem é joão vianna?:", ["definição", "interesses"])

if opcao == "definição":
    st.write("joão vianna é apenas um menino carioca estudante universitário e super legal")
    st.image("https://static.wikia.nocookie.net/pure-good-wiki/images/1/18/SpectacularPeterParker.png/revision/latest?cb=20220821054504")

if opcao == "interesses":
    st.write("Mais informações aqui")
