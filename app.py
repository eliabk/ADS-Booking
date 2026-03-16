import streamlit as st
import pandas as pd
import json
import os
import base64

# --- Page Configuration ---
st.set_page_config(
    page_title="ADS Booking — L'excellence WordPress",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Files Paths ---
DATA_FILE = "data.json"
ASSETS_DIR = "static" # Using static for better Streamlit compatibility

# --- Helper for Base64 (to ensure icons/images show up globally) ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Data Management ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "hero_title": "Révolutionnez vos Réservations WordPress.",
        "hero_subtitle": "La solution Full-Stack ultime pour gérer vos formations, événements et licences d'activation avec une élégance inédite.",
        "features": [
            {
                "icon": "🛡️", 
                "title": "Licence Centralisée API", 
                "desc": "Système de contrôle via API REST (/activate, /check). Validation quotidienne automatique par WP-Cron pour une sécurité totale."
            },
            {
                "icon": "🎨", 
                "title": "Design Media-First", 
                "desc": "Fini les emojis. Utilisez la puissance de la bibliothèque média WordPress pour des cartes de cours professionnelles et modernes."
            },
            {
                "icon": "🧱", 
                "title": "Widget Elementor Pro", 
                "desc": "Contrôles avancés pour limiter l'affichage, grille adaptative et bouton 'Voir plus' intelligent intégré directement au constructeur."
            },
            {
                "icon": "📊", 
                "title": "Dashboard Key Manager", 
                "desc": "Un addon serveur dédié pour générer vos clés et suivre en temps réel les domaines où votre plugin est actif."
            }
        ],
        "pricing": [
            {"label": "Gestion des cours de base", "free": "✅", "pro": "✅"},
            {"label": "Système de Licence API", "free": "❌", "pro": "✅"},
            {"label": "Images Personnalisées (Thumbnails)", "free": "❌", "pro": "✅"},
            {"label": "Widget Elementor Avancé", "free": "❌", "pro": "✅"},
            {"label": "Contrôle de domaine (One-site)", "free": "❌", "pro": "✅"},
            {"label": "Support Premium 24/7", "free": "❌", "pro": "✅"}
        ]
    }

if "data" not in st.session_state:
    st.session_state.data = load_data()

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.data, f)

# --- Custom Styling (V3 Premium) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    * { font-family: 'Outfit', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a2a44 0%, #0a0f18 100%);
        color: #ffffff;
    }
    
    /* Smooth Navigation */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre;
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: 25px;
        color: white;
        padding: 0 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: 0.3s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #00f2ff;
        background-color: rgba(0, 242, 255, 0.05);
    }

    .hero-container {
        padding: 100px 0 50px 0;
        text-align: center;
    }

    .hero-title {
        font-size: 5rem;
        font-weight: 900;
        line-height: 1;
        background: linear-gradient(135deg, #ffffff 30%, #00f2ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 25px;
        filter: drop-shadow(0 10px 20px rgba(0, 242, 255, 0.2));
    }

    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255,255,255,0.7);
        max-width: 800px;
        margin: 0 auto 40px auto;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 35px;
        height: 100%;
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        overflow: hidden;
    }

    .glass-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 50% 50%, rgba(0, 242, 255, 0.05) 0%, transparent 50%);
        opacity: 0;
        transition: 0.5s;
    }

    .glass-card:hover::before { opacity: 1; }

    .glass-card:hover {
        transform: translateY(-15px) scale(1.02);
        border-color: rgba(0, 242, 255, 0.3);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
    }

    .feature-icon {
        font-size: 3.5rem;
        background: linear-gradient(135deg, #fff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Primary Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00f2ff, #1a73e8);
        color: white;
        border: none;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 10px 20px rgba(0, 242, 255, 0.2);
        transition: 0.4s;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(0, 242, 255, 0.4);
        color: white !important;
    }

    /* Secondary Button */
    div.stButton > button:nth-child(2) {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        padding: 15px 40px;
        border-radius: 50px;
    }

    /* Pricing Table */
    .pricing-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 10px;
    }
    
    .pricing-table tr {
        background: rgba(255,255,255,0.02);
        border-radius: 15px;
    }
    
    .pricing-table td {
        padding: 20px;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Navigation Architecture ---
tab_landing, tab_features, tab_prices, tab_admin = st.tabs(["🚀 DÉCOUVRIR", "🛠️ TECHNOLOGIE", "💰 OFFRES", "🔒 ADMIN"])

# --- Tab 1: Landing ---
with tab_landing:
    st.markdown(f"""
        <div class="hero-container">
            <h1 class="hero-title">{st.session_state.data["hero_title"]}</h1>
            <p class="hero-subtitle">{st.session_state.data["hero_subtitle"]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        st.button("TÉLÉCHARGER MAINTENANT (Gratuit)", use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Hero Image Display
    hero_img_path = os.path.join(ASSETS_DIR, "hero.png")
    if os.path.exists(hero_img_path):
        st.image(hero_img_path, use_container_width=True)
    else:
        st.markdown('<div style="height: 400px; background: rgba(255,255,255,0.05); border-radius: 30px; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.2);">Aperçu Visuel à venir</div>', unsafe_allow_html=True)

# --- Tab 2: Technology ---
with tab_features:
    st.markdown('<h2 style="text-align: center; font-size: 3rem; margin: 50px 0;">Puissance & Flexibilité</h2>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, feature in enumerate(st.session_state.data["features"]):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="glass-card">
                    <div class="feature-icon">{feature['icon']}</div>
                    <h3 style="font-size: 1.8rem; margin-bottom: 15px;">{feature['title']}</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.6; font-size: 1.1rem;">{feature['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# --- Tab 3: Prices ---
with tab_prices:
    st.markdown('<h2 style="text-align: center; font-size: 3rem; margin: 50px 0;">Choisissez votre plan</h2>', unsafe_allow_html=True)
    
    col_price1, col_price2, col_price3 = st.columns([1, 2, 1])
    with col_price2:
        df_pricing = pd.DataFrame(st.session_state.data["pricing"])
        df_pricing.columns = ["Fonctionnalité", "Version GRATUITE", "Version PRO"]
        st.dataframe(
            df_pricing, 
            use_container_width=True, 
            hide_index=True
        )

# --- Tab 4: Admin ---
with tab_admin:
    st.markdown('<h1 style="color: #00f2ff;">Panneau de Contrôle Python</h1>', unsafe_allow_html=True)
    
    with st.expander("📝 Éditer le contenu principal", expanded=True):
        st.session_state.data["hero_title"] = st.text_input("Titre Accrocheur", st.session_state.data["hero_title"])
        st.session_state.data["hero_subtitle"] = st.text_area("Sous-titre descriptif", st.session_state.data["hero_subtitle"])
        
        if st.button("🚀 Appliquer les changements"):
            save_data()
            st.success("Mise à jour effectuée ! Rafraîchissez pour voir.")

    with st.expander("🛠️ Gérer les caractéristiques Tech"):
        for i, feature in enumerate(st.session_state.data["features"]):
            st.write(f"--- Feature {i+1} ---")
            st.session_state.data["features"][i]["title"] = st.text_input(f"Titre {i}", feature["title"], key=f"title_{i}")
            st.session_state.data["features"][i]["desc"] = st.text_area(f"Description {i}", feature["desc"], key=f"desc_{i}")
        
        if st.button("✨ Mettre à jour la Technologie"):
            save_data()
            st.balloons()
