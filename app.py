import streamlit as st
from PIL import Image

#fonction
def display_image(image_path, height=300, caption=None):
    """
    Affiche une image dans Streamlit avec une hauteur fixe.
    La largeur est ajustée automatiquement pour garder le ratio.
    """
    img = Image.open(image_path)
    hpercent = height / float(img.size[1])
    wsize = int(float(img.size[0]) * hpercent)
    img_resized = img.resize((wsize, height))
    
    st.image(img_resized, caption=caption)


# Configuration de la page
st.set_page_config(page_title="Mon Portfolio de datascientist", layout="wide")

# --- Onglets ---
tabs = st.tabs(["Présentation", "Formation/Expériences", "Compétences", "Projets", "Contact"])

# --- Onglet 1 : Présentation ---
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bonjour, je m'appelle Benoit Goffinet et je suis Data Scientist</h1>", unsafe_allow_html=True)
    st.image("benoitgoffinet.png", caption='image me représentant', width=200)
    st.markdown("""
    Passionné par le sport et la data science, je souhaite partager mon parcours et mes compétences.
    
    """)
    
# --- Onglet 2 : Formation ---
with tabs[1]:
    st.header("Formation")
    col1, col2, col3 = st.columns(3)
    with col1:
      st.write("""
      - **Diplôme** : Ingénieur en machine learning, Openclassrooms, 2025 
      - **Certifications** : Diplôme de niveau 7 (bac +5)
      """)
    with col2:
      st.write("""
      - **Diplôme** : Analyste developpeur AS400, NOTOS, 2022 
      - **Certifications** : Diplôme de niveau 6 (bac +3)
      """)
    with col3:
      st.write("""
      - **Diplôme** : Développeur web junior, 3WS Academy, 2020 
      - **Certifications** : Diplôme de niveau 5 (bac +2)
      """)

    st.header("Expériences")
    col1, col2 = st.columns(2)
    with col1:
      st.write("""
      - **Poste** : Développeur AS400
      - **Entreprise** : Notos (Montpellier)
      - **Date** : 2022-2024
      - **Langages** : CL, RPGLE, SQL
      """)
    with col2:
      st.write("""
      - **Poste** : Développeur informatique 
      - **Entreprise** : Indépendant
      - **Date** : 2021
      - **Langages** : HTPL, CSS, JAVASCIPT, PHP, MYSQL
      - **Portfolio** : http://portfolio.benoitgoffinetportfolio.fr
      """)
   
    
# --- Onglet 3 : Compétences Techniques ---
with tabs[2]:
    st.header("Compétences Techniques")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Langages & Outils")
        st.write("- Python")   
        st.write("- SQL")  
        st.write("- Excel")
    with col2:
        st.subheader("Visualisation & Web")
        st.write("- Matplotlib, Seaborn, Plotly")  
        st.write("- HTML, CSS, JavaScript, RPGLE, CL")  
        st.write("- Streamlit/Dash")
        
# --- Onglet 4 : Projets Réalisés ---
with tabs[3]:
    st.header("Projets Réalisés")
    st.write("Voici quelques-uns de mes projets :")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center;'>Dashboard</h3>", unsafe_allow_html=True)
        display_image("dashboard.png", height=300, caption="Dashboard comparant les modèles VIT et VGG16")
        st.write(
          "Dashboard permettant de comparer les performances des modèles **VIT** "
          "et **VGG16** sur un jeu de données contenant des races de chiens."
        )
        st.markdown(
        "[🔗 Accéder au dashboard](https://dashboardbenoit-h3grgwekfaa3e2ay.canadacentral-01.azurewebsites.net/)",
        unsafe_allow_html=True
        )
    with col2:
        st.markdown("<h3 style='text-align: center;'>Application/sport</h3>", unsafe_allow_html=True)
        display_image("runappli.png", height=300, caption="Application permettant de faire des prédictions sur des courses")
        st.write("Application permettant de faire des prédictions sur des performances en course à pied")
        st.markdown(
        "[🔗 Accéder à l'application](https://predictioncourse-f2dha0fma0fdazgq.canadacentral-01.azurewebsites.net//)",
         unsafe_allow_html=True
         )
    

# --- Onglet 5 : Contact ---
with tabs[4]:
    st.header("Contact")
    st.write("Vous pouvez me contacter via :")
    st.write("- **Email** : benoitgoffinet@live.fr")
    st.write("- **LinkedIn** : https://www.linkedin.com/in/benoit-goffinet-devweb/")
    st.write("- **GitHub** : [https://github.com/benoitgoffinet")
    
    