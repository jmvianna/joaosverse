import streamlit as st

st.title("interesses")

st.write("cinema")

st.image("https://images.adsttc.com/media/images/58d5/3a58/e58e/ce48/a700/003f/large_jpg/002.jpg?1490369108") 

st.write("marketing e tecnologia")

st.image("https://estudenapuc.pucpr.br/pos-graduacao/wp-content/uploads/2024/11/MBA-em-Marketing-Digital-Tecnologia-e-IA.jpg")

st.write("viagens")

st.image("https://palacepraia.com.br/wp-content/uploads/2021/10/viajar-de-aviao.jpeg")

if st.button("voltar"):
    st.switch_page("1.py")
