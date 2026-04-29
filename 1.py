import streamlit as st

st.title("joaosverse version 1")

st.image("https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2808031_bx.webp?w=760&h=434")
    
opcao = st.selectbox("quem é joão vianna?:", ["definição", "interesses"])

if opcao == "definição":
     st.write("st.title("definição")
    st.write("joão vianna é apenas um menino carioca estudante universitário e super legal")
    st.image("https://static.wikia.nocookie.net/pure-good-wiki/images/1/18/SpectacularPeterParker.png/revision/latest?cb=20220821054504")

if opcao == "interesses":
    st.write("st.title("interesses")

    st.write("cinema")

    st.image("https://images.adsttc.com/media/images/58d5/3a58/e58e/ce48/a700/003f/large_jpg/002.jpg?1490369108") 

    st.write("marketing e tecnologia")

    st.image("https://estudenapuc.pucpr.br/pos-graduacao/wp-content/uploads/2024/11/MBA-em-Marketing-Digital-Tecnologia-e-IA.jpg")

    st.write("viagens")

    st.image("https://palacepraia.com.br/wp-content/uploads/2021/10/viajar-de-aviao.jpeg")")
