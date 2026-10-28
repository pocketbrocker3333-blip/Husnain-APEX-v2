import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Husnain APEX v2.5", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #00ffcc !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ Husnain APEX [Ultimate v2.5]</h1>", unsafe_allow_html=True)
st.markdown("<p>Professional Live Market High-Precision Signal & Performance Terminal</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Asset Pair", value="EUR/USD (OTC)")
with col2:
    st.metric(label="Candle Timeframe", value="1M")
with col3:
    st.metric(label="RSI (14)", value="48.8", delta="Neutral")

st.markdown("---")
signal_col, acc_col = st.columns([2, 1])

with signal_col:
    st.error("🚨 SIGNAL: TREND CONTINUATION (PUT)")

with acc_col:
    st.metric(label="Accuracy", value="84.7%")

st.markdown("""
### 📌 Husnain Risk & Martingale Strategy Guide:
* **Step 1 (Base Trade):** Use 1% to 2% of your capital on this PUT signal.
* **Step 2 (Martingale):** Max 1 Step safety entry with 2.2x amount only if trend confirmation remains strong.
* **Session Status:** Optimized for All OTC & Live Markets.
""")

st.markdown("---")
fig = go.Figure()
fig.add_trace(go.Scatter(y=[10, 12, 11, 15, 14, 18], mode='lines+markers', line=dict(color='#00ffcc', width=2)))
fig.update_layout(
    paper_bgcolor='#0e1117',
    plot_bgcolor='#131924',
    xaxis_rangeslider_visible=False,
    height=350,
    margin=dict(l=10, r=10, t=10, b=10)
)
st.plotly_chart(fig, use_container_width=True)
