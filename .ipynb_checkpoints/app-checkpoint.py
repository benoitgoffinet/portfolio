import streamlit as st
from PIL import Image
import base64

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
    

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encoder l'image de fond
presentation = get_base64("benoitgoffinet.png")
presentationdata = get_base64("presentationdata.png")
presentationsport = get_base64("presentationsport.png")
data1 = get_base64("data.png") 
data2 = get_base64("data2.png") 
data3 = get_base64("data3.png") 
data4 = get_base64("data4.png") 




# Configuration de la page
st.set_page_config(page_title="Mon Portfolio de datascientist", layout="wide", page_icon=":computer:")
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Onglets ---
st.markdown("""
    <style>
    /* Réduit la marge au-dessus du contenu principal */
    .block-container {
        padding-top: 0.8rem;  /* valeur par défaut ~6rem */
    }
    </style>
""", unsafe_allow_html=True)
tabs = st.tabs(["Présentation", "Formation", "Compétences", "Projets", "Contact"])

# --- Onglet 1 : Présentation ---
with tabs[0]:
   slides = [
    {"img": "benoitgoffinet.png", "text": "Bonjour, je m'appelle Benoit Goffinet"},
    {"img": "presentationdata.png", "text": "Passionné par la Data Science"},
    {"img": "presentationsport.png", "text": "Passionné par le Sport"}
    ]
   if "current" not in st.session_state:
     st.session_state.current = 0

      # Boutons de navigation
   col1, col2, col3= st.columns([1, 2, 1])
   with col2:
    if st.button("◀️"):
        if st.session_state.current == 0:
           st.session_state.current = 2
        else:
           st.session_state.current -= 1 
   with col3:
    if st.button("▶️"):
        if st.session_state.current == 2:
           st.session_state.current = 0
        else:
           st.session_state.current += 1   
   slide = slides[st.session_state.current]
   bg_img = get_base64(slide["img"])

# Affichage de l'image en background avec overlay texte
   st.markdown(
    f"""
    <div style="
        width: 100%;
        height: 76vh;
        background-image: url('data:image/png;base64,{bg_img}');
        background-size: cover;
        background-position: 50% 20%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <div style="
            background-color: rgba(0,0,0,0.5);
            border-radius: 10px;
        ">
            <h1 style="color:white; text-align:center;">{slide['text']}</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


    
# --- Onglet 2 : Formation ---
with tabs[1]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 85vh;
        background-image: url('data:image/png;base64,{data1}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.4);
            padding: 40px;
            box-sizing: border-box;
            color: white;
        ">
            <!-- Formation -->
            <h1 style="color:white;">Formation</h1>
            <div style="display:flex; justify-content: space-between; flex-wrap: wrap; gap:20px;">
                <ul>
                    <li>Diplôme : Ingénieur en machine learning</li>
                    <li>École : Openclassrooms</li>
                    <li>Date : 2025</li>
                    <li>Niveau : Diplôme de niveau 7 (bac +5)</li>
                </ul>
                <ul>
                    <li>Diplôme : Analyste developpeur AS400</li>
                    <li>Ecole : Notos</li>
                    <li>Date : 2022</li>
                    <li>Niveau : Diplôme de niveau 6 (bac +3)</li>
                </ul>
                <ul>
                    <li>Diplôme : Développeur web junior</li>
                    <li>Ecole : 3WAcademy</li>
                    <li>Date : 2020</li>
                    <li>Niveau : Diplôme de niveau 5 (bac +2)</li>
                </ul>
        </div>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
# --- Onglet 3 : Compétences Techniques ---
with tabs[2]:
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 85vh;
        background-image: url('data:image/png;base64,{data2}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.4);
            padding: 40px;
            box-sizing: border-box;
            color: white;
        ">
            <!-- Formation -->
            <h1 style="color:white; margin:0;">Compétences</h1>
            <div style="display:flex; justify-content: space-between; flex-wrap: wrap; gap:20px;">
              <div>
                <h2 style="color:white;">Compétences Techniques</h2>
              <ul>
                <li><strong>Langages :</strong> Python, SQL</li>
                <li><strong>Environnements :</strong> Jupyter Notebook, Google Colab, VS Code, Anaconda</li>
                <li><strong>Libraries & Frameworks :</strong> NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch</li>
                <li><strong>Visualisation & BI :</strong> Excel, Power BI, Tableau, Matplotlib, Seaborn, Plotly, SHAP, pyLDAvis</li>
                <li><strong>Collaboration & Versioning :</strong> Git / GitHub, JIRA, Slack, Teams</li>
                <li><strong>Cloud & Big Data :</strong> AWS, Azure, Google Cloud, Heroku, Hadoop, PySpark, MongoDB</li>
                <li><strong>MLOps :</strong> MLflow, Docker</li>
            </ul>
           </div>
            <div>
    <h2 style="color:white;">Compétences Analytiques & Transverses</h2>
    <ul>
      <li><strong>Data Science & IA :</strong> Machine Learning, Deep Learning, NLP, Computer Vision</li>
      <li><strong>Analyse de données :</strong> Nettoyage, exploration, modélisation statistique, A/B testing</li>
      <li><strong>Optimisation & Modélisation :</strong> Clustering (K-means, DBSCAN), algorithmes d’optimisation</li>
      <li><strong>Méthodologies :</strong> CRISP-DM, Agile (Scrum, Kanban)</li>
      <li><strong>Communication :</strong> Data storytelling, vulgarisation scientifique, présentation résultats</li>
      <li><strong>Gestion de projet :</strong> Développement de POC, industrialisation de modèles (MLOps)</li>
      <li><strong>Soft Skills :</strong> Esprit critique, résolution de problèmes, travail collaboratif</li>
    </ul>
  </div>
             
        </div>
     </div>   
    </div>
    """,
    unsafe_allow_html=True
)
        
# --- Onglet 4 : Projets Réalisés ---
with tabs[3]:     
    st.markdown(
        f"""
        <div style="
            width: 100%;
            min-height: 100vh;
            background-image: url('data:image/png;base64,{data3}');
            background-size: cover;
            background-position: center;
            position: relative;
          
        ">
           
            <div style="   
                width: 75%;
                background-color: white;
                border: 2px;
            ">
                <h1 style="color:black; text-align:center;">Projets Réalisés</h1>
                
               
                     <div>
                          <h3 style='text-align: center;'>Dashboard</h3>
                          <p>Dashboard permettant de comparer les performances des modèles <b>VIT</b> et <b>VGG16</b> sur un jeu de données contenant des races de chiens.</p>
                          <a href="https://www.example.com">
                           <img src="dashboard.png" alt="Dashboard" width="200">
                          </a>

                     </div>
                     <div>
                          <h3 style='text-align: center;'>Application/sport</h3>
                          <p>Application permettant de soumettre ses performances en course à pied puis grace à ces dernières de faire des prédictions sur d'autres type de course à pied</p>
                          <a href="https://www.example.com">
                           <img src="runappli.png" alt="Application/sport" width="200">
                          </a>

                     </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True
    )

# --- Onglet 5 : Contact ---
with tabs[4]:
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 85vh;
        background-image: url('data:image/png;base64,{data4}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.4);
            padding: 40px;
            box-sizing: border-box;
            color: white;
        ">
            <!-- Formation -->
            <h1 style="color:white;">Contact</h1>
            <p>Vous pouvez me contacter via :</p>          
            <p>Email : benoitgoffinet@live.fr</p>
            <p>LinkedIn : <a href="https://www.linkedin.com/in/benoit-goffinet-devweb/" target="_blank" style="color:white; text-decoration:none;">linkedin.com/in/benoit-goffinet</a></p>
            <p>GitHub : <a href="https://github.com/benoitgoffinet" target="_blank" style="color:white; text-decoration:none;">github.com/benoitgoffinet</a></p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    