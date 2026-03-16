import streamlit as st
import pandas as pd
import json
import os
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="ADS Booking — Gestion de Formations",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Files Paths ---
DATA_FILE = "data.json"
LOGO_PATH = "static/logo.png"
HERO_PATH = "static/hero.png"

# --- Data Management ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "hero_title": "Libérez la puissance de vos Formations.",
        "hero_subtitle": "Le système complet de réservation et de gestion pour WordPress. De la gratuité au contrôle total avec la version Pro.",
        "features": [
            {"icon": "📅", "title": "Gestion Calendrier", "desc": "Créez et gérez vos créneaux en quelques secondes."},
            {"icon": "📄", "title": "Export PDF Pro", "desc": "Générez vos feuilles d'émargement et diplômes automatiquement."},
            {"icon": "🔑", "title": "Licence Centralisée", "desc": "Contrôlez vos activations depuis un seul tableau de bord."}
        ],
        "pricing": [
            {"label": "Gestion des cours", "free": True, "pro": True},
            {"label": "Réservations illimitées", "free": True, "pro": True},
            {"label": "Custom Card Images", "free": False, "pro": True},
            {"label": "API de Licence", "free": False, "pro": True},
            {"label": "Support Prioritaire", "free": False, "pro": True}
        ]
    }

if "data" not in st.session_state:
    st.session_state.data = load_data()

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.data, f)

# --- Custom Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0a0f18;
    }
    
    [data-testid="stSidebar"] {
        background-color: #0d1421;
        border-right: 1px solid rgba(0, 242, 255, 0.2);
    }

    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 1.1;
        background: linear-gradient(90deg, #fff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        border-radius: 30px;
        margin-bottom: 2rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .glass-card:hover {
        border-color: #00f2ff;
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.1);
    }

    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    /* Custom Table Styling */
    .stTable {
        background: rgba(255, 255, 255, 0.02) !important;
        border-radius: 20px !important;
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Header / Logo ---
if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=100)
else:
    st.sidebar.title("ADS BOOKING")

st.sidebar.divider()

# --- Navigation ---
page = st.sidebar.radio("Navigation", ["🌐 Landing Page", "🛠️ Fonctionnalités", "💰 Tarifs", "🔒 Administration"])

# --- Pages Impl ---
if page == "🌐 Landing Page":
    col1, col2 = st.columns([1.2, 0.8], gap="large")
    
    with col1:
        st.markdown(f'<h1 class="hero-title">{st.session_state.data["hero_title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 1.2rem; color: #a0aec0; margin-bottom: 2rem;">{st.session_state.data["hero_subtitle"]}</p>', unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("🚀 Démarrer Gratuitement", type="primary", use_container_width=True)
        with btn_col2:
            st.button("💎 Passer à la version PRO", use_container_width=True)
            
    with col2:
        if os.path.exists(HERO_PATH):
            st.image(HERO_PATH, use_container_width=True)
        else:
            st.markdown('<div style="height: 400px; background: rgba(255,255,255,0.05); border-radius: 30px; display: flex; align-items: center; justify-content: center;">Appperçu Indisponible</div>', unsafe_allow_html=True)

elif page == "🛠️ Fonctionnalités":
    st.markdown('<h2 style="text-align: center; margin-bottom: 3rem;">Pourquoi choisir ADS Booking ?</h2>', unsafe_allow_html=True)
    
    cols = st.columns(len(st.session_state.data["features"]))
    for i, feature in enumerate(st.session_state.data["features"]):
        with cols[i]:
            st.markdown(f"""
            <div class="glass-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h3>{feature['title']}</h3>
                <p style="color: #a0aec0;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "💰 Tarifs":
    st.markdown('<h2 style="text-align: center; margin-bottom: 3rem;">Comparez les versions</h2>', unsafe_allow_html=True)
    
    price_data = []
    for p in st.session_state.data["pricing"]:
        price_data.append({
            "Caractéristique": p["label"],
            "Version Gratuite": "✅" if p["free"] else "❌",
            "Version PRO": "✅" if p["pro"] else "❌"
        })
    
    st.dataframe(pd.DataFrame(price_data), use_container_width=True, hide_index=True)

elif page == "🔒 Administration":
    st.markdown('<h1 style="color: #00f2ff;">Tableau de Bord Python</h1>', unsafe_allow_html=True)
    st.write("Gérez le contenu de votre site web en temps réel grâce au backend Python.")
    
    tab1, tab2 = st.tabs(["📝 Texte Hero", "✨ Fonctionnalités"])
    
    with tab1:
        st.session_state.data["hero_title"] = st.text_area("Titre Principal (Hero)", st.session_state.data["hero_title"])
        st.session_state.data["hero_subtitle"] = st.text_area("Sous-titre (Hero)", st.session_state.data["hero_subtitle"])
        
        if st.button("Sauvegarder les Textes"):
            save_data()
            st.success("Contenu mis à jour avec succès !")
    
    with tab2:
        st.write("Modification des fonctionnalités à venir...")
        # Ici on pourrait ajouter des champs dynamiques pour chaque feature
