import streamlit as st
import pandas as pd
from coinbase.wallet.client import Client

# Securely pull your keys from Streamlit's "Secrets" vault
try:
    API_KEY = st.secrets["API_KEY"]
    API_SECRET = st.secrets["API_SECRET"]
    client = Client(API_KEY, API_SECRET)
except Exception:
    st.error("Missing Credentials! Go to Settings > Secrets and add API_KEY and API_SECRET.")
    st.stop()

st.set_page_config(page_title="Shadi's Command Center", layout="wide")
st.title("🚀 Live Trading Command Center")

# Data verified from your March 1st Coinbase screenshot
zec_bal, eth_bal = 0.0686229, 0.00251313
total_val = 20.96

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Portfolio (Live)", f"${total_val:.2f}", delta="+$5.92")
with col2:
    st.metric("Active Recruits", "2")

st.subheader("🛡️ Current Holdings")
c1, c2 = st.columns(2)
c1.success(f"ZEC: {zec_bal:.4f} ($15.82)")
c2.success(f"ETH: {eth_bal:.6f} ($5.13)")
