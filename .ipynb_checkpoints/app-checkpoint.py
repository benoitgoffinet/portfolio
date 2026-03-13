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
presentation = get_base64("images/presentation.jpg")
solution = get_base64("images/solution.jpg")
dashboard = get_base64("images/dashboardanalysegenerale.png")
apropos = get_base64("images/apropos.jpg")
presentationsport = get_base64("presentationsport.png")
formation = get_base64("formation.jpg") 
competence = get_base64("competence.jpg") 
projet = get_base64("projet.jpg") 
contact = get_base64("contact.jpg") 
benoit = get_base64("images/benoit.png")



# Configuration de la page
st.set_page_config(
    page_title="BenIA.solutions",
    layout="wide",
    page_icon=":computer:"
)
st.markdown(
    """
    <style>
        /* cache la barre du haut (deploy + menu) */
[data-testid="stToolbar"] {
    display: none;
}

/* cache le bouton menu */
#MainMenu {
    visibility: hidden;
}

/* cache le footer Streamlit */
footer {
    visibility: hidden;
}

/* enlève la marge du haut */
header {
    visibility: hidden;
}

        .block-container {
            padding-top: 0.01rem;
            padding-bottom: 0.01rem;
            padding-left: 0.1rem;
            padding-right: 0.1rem;
            background-color: #B8C1CC;

        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    /* Masque tout ce qui est SVG dans les headers */
    div.element-container h1 svg,
    div.element-container h2 svg,
    div.element-container h3 svg,
    div.element-container h4 svg,
    div.element-container h5 svg,
    div.element-container h6 svg {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Onglets ---
st.markdown("""
    <style>
    /* Supprimer les marges internes du conteneur principal */
    .block-container {
        padding-top: 0;
        padding-bottom: 0;
    }
    
    /* Supprime les marges automatiques autour de la barre d'onglets */
    div[data-baseweb="tab-list"] {
        height: 5vh;                  
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-bottom: 0;               /* ❌ aucune marge en dessous */
        padding-bottom: 0;              /* ❌ aucune marge interne */
    }

    /* Style optionnel des onglets */
    div[data-baseweb="tab"] {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem;
    }

    /* Supprime les espaces résiduels éventuels */
    [data-testid="stVerticalBlock"] {
        margin-bottom: 0;
        padding-bottom: 0;
    }

    </style>
""", unsafe_allow_html=True)

tabs = st.tabs(["Présentation", "Solution / Dashboard interactif", "Accéder au Dashboard", "A propos", "Contact"])
# --- Onglet 1 : Présentation ---
with tabs[0]:
   
   


# Affichage de l'image en background avec overlay texte
   st.markdown(
    f"""
    <div style="
        width: 100%;
        fontsize: 14px;
        min-height: 92vh;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{presentation}');
        background-size: cover;
        background-position: 50% 20%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <div style="
            background-color: rgba(0,0,0,0.8);
            border-radius: 2rem;
        ">
            <h1 style="color:#B8C1CC; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.5rem, 7vw + 1rem, 5rem);">{'BenIA.solutions<br> Data Consultant spécialisé dans les structures culturelles'}</h1>
         <p style="color:#B8C1CC; text-align:center; font-family: 'Times New Roman', Times, serif; font-size: clamp(0.3rem, 4vw + 1rem, 3rem);">Anticipez le remplissage de vos spectacles et pilotez votre programmation grâce à l’analyse de vos propres données.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


    
# --- Onglet 2 : Offre
with tabs[1]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;eight: 100%;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{solution}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">L'Offre de BenIA.solutions</h1>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Problème</h2>
            <p style="font-size:18px; line-height:1.6;">
De nombreuses <strong>structures culturelles</strong> disposent de données historiques, mais celles-ci sont rarement utilisées pour piloter l’organisation des événements.
Il devient alors difficile d’<strong>anticiper l’affluence</strong> des spectacles et d’optimiser le remplissage des représentations.

</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Solution</h2>
            <p style="font-size:18px; line-height:1.6;">Pour répondre à cette problématique, BenIA.solutions propose d’exploiter et d’analyser vos données historiques de fréquentation afin d’identifier les tendances observées au fil du temps.<br>
Grâce à un <strong>dashboard interactif</strong>, vous pourrez visualiser et <strong>anticiper l’affluence</strong> des spectacles et mieux préparer l’organisation de vos représentations.<p/>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Bénéfices</h2>
            <ul style="font-size:18px; line-height:1.6;">
            <li>✔ anticipation de la fréquentation</li>
            <li>✔ meilleure organisation des représentations</li>
            <li>✔ optimisation du remplissage des salles</li>
            <li>✔ aide à la prise de décision pour la programmation
</li>
            <ul/>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Le Dashboard</h2>
            <p style="font-size:18px; line-height:1.6;">
            Le dashboard est composé de quatre sections principales permettant d’analyser les <strong>données de fréquentation</strong> des spectacles et d’<strong>anticiper l’affluence</strong> des représentations.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">1️⃣ Analyse globale</h3>
            <p style="font-size:18px; line-height:1.6;">Cette section permet d’avoir une vue d’ensemble de l’activité du théâtre.<br>Elle présente les indicateurs principaux comme :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>l’affluence moyenne</li>
            <li>le taux de remplissage</li>
            <li>le chiffre d’affaires</li>
            <li>l’évolution de l'affluence dans le temps</li>
            <li>l'affluence par genre</li>
            <ul/>
            <p style="font-size:18px; line-height:1.6;">Elle permet de comprendre rapidement les tendances générales de fréquentation.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">2️⃣ Analyse par variable</h3>
            <p>Cette partie permet d’explorer les données selon différentes variables comme :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>genre</li>
            <li>jour</li>
            <li>saison</li>
            <ul/>
            <p style="font-size:18px; line-height:1.6;">L’objectif est d’identifier les facteurs qui influencent le plus la fréquentation des spectacles.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">3️⃣ Prédicteur</h3>
            <p style="font-size:18px; line-height:1.6;">Le prédicteur utilise les données historiques pour estimer l’affluence future d’une représentation.<br>
            En fonction des caractéristiques du spectacle, il devient possible de :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>prévoir le niveau de fréquentation attendu</li>
            <li>anticiper le taux de remplissage</li>
            <li>adapter l’organisation ou la communication</li>
            <ul/>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">4️⃣ Données</h3>
            <p style="font-size:18px; line-height:1.6;">Cette section permet d’accéder aux données utilisées dans le dashboard.<br>
            Elle offre une vision détaillée des informations disponibles et permet de mieux comprendre les analyses réalisées dans les autres sections.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Exemple d’utilisation</h3>
             <p style="font-size:18px; line-height:1.6;">Par exemple, un théâtre souhaitant programmer une nouvelle pièce peut utiliser le dashboard pour analyser les tendances de fréquentation observées dans les données passées.<br>
            L’analyse peut montrer que certains genres de spectacles attirent davantage de public certains jours de la semaine ou à certaines périodes de l’année.<br>
            Ces informations permettent d’anticiper l’affluence attendue pour la représentation et d’adapter la programmation, l’organisation ou la communication autour de la pièce.</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Déroulement du projet</h2>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">1️⃣ Échange sur vos besoins</h3>
            <p style="font-size:18px; line-height:1.6;">La première étape consiste à échanger sur votre activité, vos données et vos besoins.<br>
            Cet échange permet de comprendre :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>les données disponibles au sein de votre structure</li>
            <li>vos problématiques liées à la fréquentation des spectacles</li>
            <li>vos objectifs d’analyse</li>
            <li>les indicateurs et les variables qui vous intéressent.</li>
            <ul/>
            <p style="font-size:18px; line-height:1.6;">Cet échange permet également de définir les visualisations les plus pertinentes pour le dashboard (types de graphiques, filtres, indicateurs, etc.).</p>
               <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">2️⃣ Analyse des données</h3>
            <p style="font-size:18px; line-height:1.6;">Les données disponibles sont ensuite analysées afin d’identifier les tendances de fréquentation et les facteurs pouvant influencer l’affluence des spectacles.<br>
            Cette étape permet notamment de :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>sélectionner la période d’analyse la plus pertinente</li>
            <li>préparer les données</li>
            <li>identifier les tendances importantes.</li>
            <ul/>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">3️⃣ Développement du dashboard</h3>
            <p style="font-size:18px; line-height:1.6;">Un dashboard interactif est développé afin de permettre l’exploration des données et la visualisation des tendances observées.<br>
            Le dashboard est adapté aux besoins de chaque structure culturelle.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">4️⃣ Présentation de l’analyse et prise en main</h3>
            <p style="font-size:18px; line-height:1.6;">
            Une session est organisée afin de :</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>présenter les principales tendances observées dans les données</li>
            <li>expliquer le fonctionnement du dashboard</li>
            <li>accompagner les équipes dans la prise en main de l’outil.</li>
            <ul/>
            <p style="font-size:18px; line-height:1.6;">Cette session permet également de montrer comment retrouver les analyses directement dans le dashboard.</p>
            <h3 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">5️⃣ Hébergement, accès et évolutions possibles</h3>
            <p style="font-size:18px; line-height:1.6;"Le dashboard est hébergé en ligne afin de permettre un accès simple et rapide à l’outil.<br>
            L’accès au dashboard est sécurisé et réservé à la structure. Un code d’accès privé est fourni afin de garantir la confidentialité des données et de permettre aux membres de l’équipe autorisés de consulter les analyses.<br>
            L’hébergement et la maintenance technique sont assurés pendant 6 mois, afin de garantir le bon fonctionnement du dashboard et de corriger d’éventuels problèmes techniques.<br>
            À l’issue de cette période, il est possible de poursuivre l’hébergement et la maintenance du dashboard. Les analyses peuvent alors être mises à jour afin d’intégrer les nouvelles données disponibles.<br>
            Il est également possible de faire évoluer le dashboard dans le temps, notamment en ajoutant de nouvelles variables afin d’enrichir les analyses et d’adapter l’outil aux nouveaux besoins de la structure culturelle.</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Contact</h2>
            <p style="font-size:18px; line-height:1.6;">N’hésitez pas à me contacter pour discuter de votre projet ou simplement échanger autour de vos données.<br>
            Je réponds généralement sous 24 à 48 heures.<br>
            Email : benoit@benia.solutions<br>
            Téléphone : 06 08 90 02 85</p>
           
            </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Onglet 2 : dash
with tabs[2]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        min-height: 92vh;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{dashboard}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Démonstration du dashboard</h1>
            <p style="font-size:18px; line-height:1.6;">
Cette démonstration permet d'explorer un exemple de dashboard interactif
    dédié à l'analyse de la fréquentation des événements culturels.<br>
Le dashboard permet notamment de :
</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>analyser les tendances de fréquentation</li>
            <li>explorer les données selon différentes variables</li>
            <li>utiliser un prédicteur pour estimer l'affluence</li>
            </ul>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Accéder à la démonstration interactive</h2>
            <p>Les données utilisées dans cette démonstration sont fictives et présentées uniquement à des fins d’illustration.<br>
            Le dashboard peut être adapté aux données propres à chaque structure culturelle et enrichi avec différentes variables selon les besoins d’analyse.</p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <a href="https://web-production-269e5.up.railway.app/" target="_blank"
style="
position:fixed;
bottom:0;
left:0;
width:100%;
padding:24px;
background-color:#FACC15;
color:black;
text-decoration:none;
font-size:24px;
font-weight:700;
text-align:center;
z-index:999;
">
🚀 Tester la démo interactive
</a>
    """,
    unsafe_allow_html=True
)

# --- Onglet 3 : A propos
with tabs[3]: 
    st.markdown(
    f"""
    <div style="
        width: 100%;
        font-size: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{apropos}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <!-- Overlay semi-transparent pour le texte -->
        <div style="
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.8);
            padding: 4rem;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <!-- Offre -->
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">BenIA.solutions</h1>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Le projet</h2>
            <p style="font-size:18px; line-height:1.6;">
BenIA.solutions est un projet dédié à l’analyse et à la valorisation des données dans le secteur culturel.
L’objectif est d’aider les <strong>structures culturelles</strong> à mieux comprendre la fréquentation de leurs événements et à piloter leur programmation grâce à l’analyse de leurs données.
</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Le fondateur</h2>
            <p style="font-size:18px; line-height:1.6;">
Je suis Benoît Goffinet, fondateur de BenIA.solutions et consultant en analyse de données.
Je mets mes compétences en data, en intelligence artificielle et en visualisation de données au service des <strong>structures culturelles</strong> afin de transformer leurs données en outils d’aide à la décision et d’anticiper la fréquentation des spectacles.<br>
Mon travail repose sur une combinaison de rigueur analytique, de créativité et de pédagogie, afin de proposer des outils clairs, utiles et adaptés aux besoins des équipes. Passionné par les événements culturels et le spectacle vivant, je m’attache également à comprendre les enjeux spécifiques des structures que j’accompagne.
</p>
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Formation</h2>
            <p style="font-size:18px; line-height:1.6;">
Je suis diplômé d’une formation diplômante d’ingénieur en Machine Learning, centrée sur l’analyse de données et les techniques de modélisation.<br>
Cette formation m’a permis d’acquérir des compétences en :
</p>
            <ul style="font-size:18px; line-height:1.6;">
            <li>analyse de données</li>
            <li>visualisation de données</li>
            <li>modélisation statistique</li>
            <li>machine learning</li>
            </ul>
            <p>
Ces compétences sont aujourd’hui mobilisées dans le développement de BenIA.solutions.
</p>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Mon approche</h2>
            <p style="font-size:18px; line-height:1.6;">
Mon approche consiste à transformer les données existantes en outils d’aide à la décision accessibles et interactifs.<br>
Grâce à l’analyse des données, à la visualisation et à la modélisation, il devient possible de mieux comprendre les comportements de fréquentation et d’accompagner les équipes dans leurs décisions.
</p>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Mes compétences</h2>
            <p style="font-size:18px; line-height:1.6;">
Au-delà des compétences techniques, mon travail repose également sur plusieurs qualités essentielles :
</p>    
 <ul style="font-size:18px; line-height:1.6;">
            <li>capacité d’analyse pour comprendre les problématiques et les données</li>
            <li>pédagogie afin de rendre les analyses accessibles aux équipes</li>
            <li>écoute des besoins pour adapter les outils aux réalités des <strong>structures culturelles</strong></li>
            <li>compréhension des besoins des <strong>structures culturelles</strong></li>
            </ul>
<h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Pourquoi ce projet</h2>
            <p style="font-size:18px; line-height:1.6;">
Le secteur culturel produit aujourd’hui de nombreuses données (billetterie, fréquentation, programmation), mais ces informations sont rarement exploitées de manière approfondie.<br>
BenIA.solutions vise à valoriser ces données et à les rendre utiles pour le pilotage des activités culturelles.
</p>
           <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Traitement des données</h2>
            <p style="font-size:18px; line-height:1.6;">
Les données utilisées dans le cadre des analyses restent la propriété de la structure culturelle.<br>
Les informations fournies sont utilisées uniquement dans le but de réaliser les analyses nécessaires au fonctionnement du dashboard et à l’accompagnement proposé.<br>
Aucune donnée n’est transmise à des tiers.<br>
Lorsque cela est nécessaire, les données peuvent être anonymisées ou agrégées afin de garantir la confidentialité des informations.
</p>    
            <h2 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Discutons de votre projet </h2>
            <p style="font-size:18px; line-height:1.6;">Vous souhaitez explorer vos <strong>données de fréquentation</strong> et mieux <strong>anticiper l’affluence</strong> de vos spectacles ?
N’hésitez pas à me contacter pour échanger sur votre projet.</p>
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 06 08 90 02 85</p>
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
        min-height: 92vh;
        fontsize: 16px;
        font-family: 'Roboto', sans-serif;
        background-image: url('data:image/png;base64,{contact}');
        background-size: cover;
        background-position: center;
        position: relative;
    ">
        <div style="
            position: absolute;
            top: 0; left: 0;
            width: 100%; 
            background-color: rgba(0,0,0,0.4);
            padding: 40px;
            box-sizing: border-box;
            color: #B8C1CC;
        ">
            <h1 style="color:#B8C1CC; font-family: 'Times New Roman', Times, serif;">Contact</h1>
            <p style="font-size:18px; line-height:1.6;">Vous pouvez me contacter via :</p>          
            <p style="font-size:18px; line-height:1.6;">Email : benoit@benia.solutions</p>
            <p style="font-size:18px; line-height:1.6;">Téléphone : 0608900285</p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://www.linkedin.com/in/benoit-goffinet-devweb/" target="_blank" style="color:#B8C1CC; text-decoration:none;">LinkedIn</a></p>
            <p style="font-size:18px; line-height:1.6;"><a href="https://github.com/benoitgoffinet" target="_blank" style="color:#B8C1CC; text-decoration:none;">GitHub</a></p>
            </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
    