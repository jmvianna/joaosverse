import streamlit as st

st.set_page_config(
    page_title="joaosverse",
    page_icon="🌎",
    layout="centered"
)

st.markdown("""
# 🌎 joaosverse
### welcome to joao's universe

aqui você vai encontrar tudo sobre joão vianna
""")

st.image(
    "https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2808031_bx.webp?w=760&h=434",
    use_container_width=True
)

opcao = st.selectbox(
    "quem é joão vianna?:",
    ["selecione uma opção", "definição", "interesses"]
)

if opcao == "definição":
    st.title("definição")
    st.write("joão vianna é apenas um menino carioca estudante universitário e super legal")
    st.image("https://static.wikia.nocookie.net/pure-good-wiki/images/1/18/SpectacularPeterParker.png/revision/latest?cb=20220821054504")

elif opcao == "interesses":
    st.write("joão tem diversos interesses, qual deles você gostaria de aprofundar?")
    opcao = st.selectbox(
    "interesses especificados:",
    ["selecione uma opção", "cinema", "marketing e tecnologia", "viagens"]
)
        if opcao == "cinema":
            st.title("cinema")
            st.image("https://images.adsttc.com/media/images/58d5/3a58/e58e/ce48/a700/003f/large_jpg/002.jpg?1490369108") 
            st.write("joão é apaixonado por cinema, alguns de seus filmes favoritos são:")
            st.write("# star wars: the empire strikes back, 1980")
            st.image("https://m.media-amazon.com/images/M/MV5BMTkxNGFlNDktZmJkNC00MDdhLTg0MTEtZjZiYWI3MGE5NWIwXkEyXkFqcGc@._V1_.jpg")
    
       if opcao == "marketing e tecnologia":
           st.title("marketing e tecnologia")
           st.image("https://images.adsttc.com/media/images/58d5/3a58/e58e/ce48/a700/003f/large_jpg/002.jpg?1490369108") 
