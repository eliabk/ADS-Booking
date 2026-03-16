import streamlit as st
import pandas as pd
import json
import os
import base64

# --- Page Configuration ---
st.set_page_config(
    page_title="ADS Booking — Plugin WordPress de Formations",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Files Paths ---
DATA_FILE = "data.json"
STATIC_DIR = "static"

# --- Data Management ---
def load_data():
    default_data = {
        "hero_title": "Propulsez vos Formations WordPress vers l'Excellence.",
        "hero_subtitle": "Le plugin tout-en-un pour gérer vos inscriptions, générer des factures PDF et contrôler vos licences.",
        "features": [
            {"icon": "🛡️", "title": "Licence & Sécurité", "desc": "Système de licence centralisé."},
            {"icon": "📄", "title": "Facturation Automatique", "desc": "Générez des factures PDF."},
            {"icon": "🎨", "title": "Design Personnalisable", "desc": "Adaptez les styles."},
            {"icon": "🔄", "title": "Sauvegarde & Restauration", "desc": "Ne perdez jamais vos données."}
        ],
        "pricing": [
            {"label": "Gestion des Formations & Événements", "free": "✅", "pro": "✅"},
            {"label": "Inscriptions en ligne & Shortcodes", "free": "✅", "pro": "✅"},
            {"label": "Tableau de bord des inscriptions", "free": "✅", "pro": "✅"},
            {"label": "Export CSV des Inscriptions", "free": "✅", "pro": "✅"},
            {"label": "Styles & Couleurs personnalisables", "free": "❌", "pro": "✅"},
            {"label": "Génération de Facture / Reçu PDF", "free": "❌", "pro": "✅"},
            {"label": "Export en masse des Factures (ZIP)", "free": "❌", "pro": "✅"},
            {"label": "Sauvegarde & Restauration (Export JSON / Media)", "free": "❌", "pro": "✅"}
        ]
    }
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                content = json.load(f)
                # Merge with default to ensure all keys exist
                return {**default_data, **content}
        except:
            return default_data
    return default_data

if "data" not in st.session_state:
    st.session_state.data = load_data()

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.data, f)

# --- Secret Admin Access ---
is_admin = st.query_params.get("manage") == "ads_secret_2026"

# --- Custom Styling (V3 Landing Design) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    * { font-family: 'Outfit', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a2a44 0%, #0a0f18 100%);
        color: #ffffff;
    }

    .section-padding { padding: 80px 0; }

    .hero-title {
        font-size: 5rem;
        font-weight: 900;
        line-height: 1;
        background: linear-gradient(135deg, #ffffff 30%, #00f2ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 25px;
        text-align: center;
    }

    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255,255,255,0.7);
        max-width: 900px;
        margin: 0 auto 40px auto;
        text-align: center;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        border-radius: 35px;
        height: 100%;
        transition: 0.4s;
        text-align: center;
    }

    .glass-card:hover {
        transform: translateY(-10px);
        border-color: #00f2ff;
        background: rgba(0, 242, 255, 0.05);
    }

    .cta-button div > button {
        background: linear-gradient(90deg, #ff4b2b, #ff416c) !important;
        color: white !important;
        padding: 20px 60px !important;
        border-radius: 50px !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(255, 75, 43, 0.3) !important;
    }

    .donate-card {
        background: linear-gradient(135deg, rgba(26, 115, 232, 0.1), rgba(0, 242, 255, 0.1));
        border: 2px solid #00f2ff;
        padding: 50px;
        border-radius: 40px;
        text-align: center;
        margin-top: 50px;
    }

    /* Hide standard Streamlit header */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- ADMIN VIEW ---
if is_admin:
    st.markdown('<h1 style="color: #00f2ff;">🔒 Administration Secrète</h1>', unsafe_allow_html=True)
    st.info("Vous êtes dans la zone d'édition. Les modifications impactent directement la landing page.")
    
    with st.expander("📝 Contenu Hero"):
        st.session_state.data["hero_title"] = st.text_input("Titre", st.session_state.data["hero_title"])
        st.session_state.data["hero_subtitle"] = st.text_area("Sous-titre", st.session_state.data["hero_subtitle"])
    
    if st.button("Sauvegarder les modifications"):
        save_data()
        st.success("Modifications enregistrées ! Retirez '?manage=...' pour voir le site.")
    st.stop()

# --- LANDING PAGE VIEW ---

# 1. Hero Section
st.markdown('<div class="section-padding">', unsafe_allow_html=True)
st.markdown(f'<h1 class="hero-title">{st.session_state.data["hero_title"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-subtitle">{st.session_state.data["hero_subtitle"]}</p>', unsafe_allow_html=True)

col_hero1, col_hero2, col_hero3 = st.columns([1, 1.5, 1])
with col_hero2:
    st.button("TÉLÉCHARGER LE PLUGIN (GRATUIT)", use_container_width=True, key="hero_cta")
st.markdown('</div>', unsafe_allow_html=True)

# 2. Hero Visual
hero_img = os.path.join(STATIC_DIR, "hero.png")
if os.path.exists(hero_img):
    st.image(hero_img, use_container_width=True)

st.divider()

# 3. Features Section
st.markdown('<h2 style="text-align: center; font-size: 3rem; margin: 40px 0;">Pourquoi ADS Booking ?</h2>', unsafe_allow_html=True)
cols = st.columns(len(st.session_state.data["features"]))
for i, feature in enumerate(st.session_state.data["features"]):
    with cols[i]:
        st.markdown(f"""
            <div class="glass-card">
                <div style="font-size: 3.5rem; margin-bottom: 20px;">{feature['icon']}</div>
                <h3 style="font-size: 1.5rem; margin-bottom: 15px;">{feature['title']}</h3>
                <p style="color: rgba(255,255,255,0.6);">{feature['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 4. Comparison Table Section
st.markdown('<h2 style="text-align: center; font-size: 3rem; margin: 40px 0;">Version Gratuite vs Version PRO</h2>', unsafe_allow_html=True)
df_comp = pd.DataFrame(st.session_state.data["pricing"])
df_comp.columns = ["Fonctionnalité", "Gratuit", "PRO"]
st.table(df_comp)

# 5. Donation / Pro Section
st.markdown('<div class="donate-card">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 2.5rem;">Soutenez le Développement</h2>', unsafe_allow_html=True)
st.markdown("""
    <p style="font-size: 1.2rem; color: rgba(255,255,255,0.8); max-width: 700px; margin: 20px auto;">
        ADS Booking est un projet passionné. En faisant un don, vous soutenez l'évolution du plugin 
        et débloquez l'accès à toutes les <b>Fonctionnalités PRO</b> (Factures PDF, Styles personnalisés, Sauvegardes).
    </p>
""", unsafe_allow_html=True)

col_don1, col_don2, col_don3 = st.columns([1, 1.2, 1])
with col_don2:
    st.markdown('<div class="cta-button">', unsafe_allow_html=True)
    st.button("FAIRE UN DON & PASSER PRO ❤️")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 6. Footer
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.3); font-size: 0.9rem; padding: 40px 0; border-top: 1px solid rgba(255,255,255,0.05);">
        © 2026 ADS Booking. Propulsé par Python & Passion.
    </div>
""", unsafe_allow_html=True)
