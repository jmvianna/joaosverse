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
        st.write("### joão é apaixonado por cinema, alguns de seus filmes favoritos são:")
        st.write("## star wars: the empire strikes back, 1980")
        st.image("https://m.media-amazon.com/images/M/MV5BMTkxNGFlNDktZmJkNC00MDdhLTg0MTEtZjZiYWI3MGE5NWIwXkEyXkFqcGc@._V1_.jpg")
        st.write("## dune, 2021")
        st.image("https://posterspy.com/wp-content/uploads/2024/04/Dune-Finished.jpg")
        st.write("## call me by youor name, 2017")
        st.image("https://media.karousell.com/media/photos/products/2021/4/2/call_me_by_your_name_a4_poster_1617350740_7b5be6d5_progressive.jpg")
    
    if opcao == "marketing e tecnologia":
        st.title("marketing e tecnologia")
        st.image("https://estudenapuc.pucpr.br/pos-graduacao/wp-content/uploads/2024/11/MBA-em-Marketing-Digital-Tecnologia-e-IA.jpg")
        st.write("### joão adora se aventurar em áreas como:")
        st.write("## marketing estratégico")
        st.image("https://media.licdn.com/dms/image/v2/D4D12AQEfXJMbNh6g3A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1665589480826?e=2147483647&v=beta&t=vsk-vvtmGYGenfW-2XmKAh4DJ2SZPIwj2yVhfv3hnHs"
        st.write("## branding")
        st.image("https://registrodemarca.arenamarcas.com.br/wp-content/uploads/2022/01/Qual-E-o-conceito-de-Branding.jpg"
        st.write("## análise de dados")
        st.image("https://www.comececomopedireito.com.br/blog/wp-content/uploads/2024/02/analise-de-dados-com-power-bi.jpg"

if opcao == "viagens":
        st.title("viagens")
        st.image("https://palacepraia.com.br/wp-content/uploads/2021/10/viajar-de-aviao.jpeg")
        st.write("### joão ama viajar, esses são alguns dos lugares mais legais que ele já foi:")
        st.write("## cusco, peru")
        st.image("https://static.historiadomundo.com.br/2023/11/vista-da-paisagem-de-machu-picchu-cidade-pre-colombiana-construida-pelos-incas.jpg"
        st.write("## ephesus, turquia")
        st.image("https://www.royalcaribbean.com/media-assets/pmc/content/dam/excalibur/digital-destinations/port-destinations/ports-of-call/ephesus-kusadasi-turkey-adb/stock-photo-ADB-ephesus-kusadasi-turkey-port-celsus-library-sunset-167371061.jpg?w=1920"
        st.write("## san pedro de atacama, chile")
        st.image("https://uploads.dicaschile.com.br/sites/13/2019/02/licancabur-vulcao-montanha-chile.jpg"
