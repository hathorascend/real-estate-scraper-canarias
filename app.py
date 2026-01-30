# Fixed Streamlit Cloud deployment - Dependencies updated
import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import requests
from bs4 import BeautifulSoup
import time
import datetime
import plotly.express as px
# from streamlit_option_menu import option_menu

# Configuración de página
st.set_page_config(page_title="Real Estate Scraper - Canarias", page_icon="🏠", layout="wide")

# Diseño Moderno con CSS (Glassmorphism & Gradients)
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stApp {
        background: transparent;
    }
    div.stButton > button {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        color: white;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        margin-bottom: 20px;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #2575fc;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 700;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2c3e50,#000000);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Conexión Google Sheets ---
def connect_to_gsheet():
    try:
        # Usar secrets de Streamlit para producción
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        # Nota: El usuario debe subir el JSON a Streamlit Secrets como 'google_credentials'
        creds = Credentials.from_service_account_info(st.secrets["google_credentials"], scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key("1QiuJZdA_JzP7TqzvDTK8ZValwFpHP0pcIDnAt0gXwUg").sheet1
        return sheet
    except Exception as e:
        st.error(f"Error conectando a Google Sheets: {e}")
        return None

# --- Lógica de Scraping (Ejemplo simplificado) ---
def scrape_ads(isla, tipo_inmueble, max_precio):
    # Aquí iría la lógica real de requests/soup para Idealista/Fotocasa
    # Por ahora simulamos resultados para la demo
    simulated_data = [
        {
            'ID': f"SIM-{time.time()}",
            'Fecha': datetime.datetime.now().strftime("%Y-%m-%d"),
            'Portal': 'Demo',
            'Título': f"Apartamento en {isla}",
            'Precio': 150000,
            'Ubicación': f"Zona centro, {isla}",
            'Isla': isla,
            'Tipo': tipo_inmueble,
            'Particular': 'Sí',
            'Link': 'https://example.com'
        }
    ]
    return simulated_data

# --- Interfaz Principal ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/609/609803.png", width=100)
    st.title("Hathor Real Estate")
    selected = st.radio(
        "Menú",
        ["Dashboard", "Buscador", "Historial", "Configuración"],
        horizontal=True
    )
if selected == "Dashboard":
    st.markdown("# 📊 Panel de Control")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>1,234</h3><p>Anuncios Totales</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>85</h3><p>Particulares Hoy</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>€1.2M</h3><p>Volumen Mercado</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>-5%</h3><p>Tendencia Precios</p></div>', unsafe_allow_html=True)

    # Gráfico de ejemplo
    df_demo = pd.DataFrame({
        'Isla': ['Tenerife', 'Gran Canaria', 'Lanzarote', 'Fuerteventura', 'La Palma', 'La Gomera', 'El Hierro'],
        'Ads': [450, 420, 120, 100, 50, 30, 20]
    })
    fig = px.bar(df_demo, x='Isla', y='Ads', title="Distribución de Anuncios por Isla", color_discrete_sequence=['#2575fc'])
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Buscador":
    st.markdown("# 🔍 Buscador en Tiempo Real")
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            isla = st.selectbox("Selecciona Isla", ["Tenerife", "Gran Canaria", "Lanzarote", "Fuerteventura", "La Palma", "La Gomera", "El Hierro"])
        with col_f2:
            tipo = st.selectbox("Tipo de Inmueble", ["Piso", "Casa", "Terreno", "Local"])
        with col_f3:
            precio_max = st.number_input("Precio Máximo (€)", value=200000, step=10000)
        
        if st.button("Iniciar Scraping 🚀"):
            with st.spinner("Buscando anuncios de particulares..."):
                results = scrape_ads(isla, tipo, precio_max)
                st.success(f"¡Se han encontrado {len(results)} anuncios nuevos!")
                st.table(pd.DataFrame(results))
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Configuración":
    st.markdown("# ⚙️ Configuración")
    st.info("Configura aquí tus APIs y parámetros del sistema.")
    st.text_input("Google Sheet ID", value="1QiuJZdA_JzP7TqzvDTK8ZValwFpHP0pcIDnAt0gXwUg")
    st.checkbox("Notificaciones por Telegram", value=True)
    st.checkbox("Auto-guardado en Google Sheets", value=True)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ for Canary Islands Real Estate Market")
