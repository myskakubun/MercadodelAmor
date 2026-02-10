import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# --- CONFIGURACIÓN DE LA PÁGINA (Estética Myska Kubun) ---
st.set_page_config(page_title="Myska Kubun: El Pulso del Amor", layout="wide", page_icon="💔")

# Estilos CSS personalizados para modo oscuro/cyberpunk
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1 {
        color: #00FFFF !important; /* Cian Neón */
    }
    h3 {
        color: #FF00FF !important; /* Magenta Neón */
    }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO Y NARRATIVA ---
st.title("💔 ¿Cupido o Código? El Mercado Habla")
st.markdown("""
**Myska Kubun Data Lab** | *Datos en tiempo real*
¿Dónde están poniendo el dinero los inversores? ¿En las apps de citas tradicionales o en la infraestructura de IA?
Este gráfico monitoriza el rendimiento financiero relativo en el último año.
""")

# --- CONTROLES DE TIEMPO ---
col1, col2 = st.columns(2)
with col1:
    period = st.selectbox("Selecciona Periodo", ['6mo', '1y', '2y', '5y', 'ytd'], index=1)

# --- OBTENCIÓN DE DATOS (YAHOO FINANCE) ---
tickers = ['MTCH', 'NVDA']
data = yf.download(tickers, period=period)['Close']

# Normalización (Base 100) para poder comparar peras con manzanas
# Esto muestra el % de crecimiento relativo, no el precio absoluto
data_normalized = data / data.iloc[0] * 100

# --- GRÁFICO INTERACTIVO ---
st.subheader("📉 La Divergencia: Tinder (Match Group) vs. IA (NVIDIA)")
st.line_chart(data_normalized, color=["#FF00FF", "#00FFFF"]) # Magenta para MTCH, Cian para NVDA

# --- METRICAS CLAVE (KPIs) ---
last_price = data.iloc[-1]
start_price = data.iloc[0]
growth = ((last_price - start_price) / start_price) * 100

c1, c2 = st.columns(2)
c1.metric("Rendimiento Match Group (Tinder)", f"{growth['MTCH']:.2f}%", delta_color="normal")
c2.metric("Rendimiento Infraestructura IA", f"{growth['NVDA']:.2f}%", delta_color="normal")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Fuente de datos: Yahoo Finance API (Live). Análisis generado por el equipo de Myska Kubun.")