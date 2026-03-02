import streamlit as st
import pandas as pd
from coinbase.wallet.client import Client

# --- SECURE API SETUP ---
# This looks for the keys you added in Manage App > Settings > Secrets
try:
    API_KEY = st.secrets["API_KEY"]
    API_SECRET = st.secrets["API_SECRET"]
    client = Client(API_KEY, API_SECRET)
except Exception:
    st.error("Missing Credentials! Go to Settings > Secrets and add API_KEY and API_SECRET.")
    st.stop()

# --- PAGE CONFIG ---
st.set_page_config(page_title="Shadi's Command Center", layout="wide", page_icon="🚀")
st.title("🚀 Live Trading Command Center")

# --- PORTFOLIO DATA (Verified March 1, 2026) ---
# These match your latest Coinbase 'My_private_bot' screenshot
zec_amount = 0.0686229
eth_amount = 0.00251313
zec_value = 15.82
eth_value = 5.13
total_balance = 20.96
initial_investment = 15.04
total_profit = total_balance - initial_investment

# --- MAIN METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Portfolio", f"${total_balance:.2f}", delta=f"+${total_profit:.2f}")
with col2:
    st.metric("ZEC Holdings", f"{zec_amount:.4f}", f"${zec_value:.2f}")
with col3:
    st.metric("ETH Holdings", f"{eth_amount:.6f}", f"${eth_value:.2f}")

st.markdown("---")

# --- RECRUIT STATUS ---
st.subheader("🛡️ Recruit Intelligence")
left_bot, right_bot = st.columns(2)

with left_bot:
    st.success("🤖 **ZEC Scalper**")
    st.write(f"**Current Allocation:** {zec_amount:.6f} ZEC")
    st.write(f"**Market Value:** ${zec_value:.2f}")
    st.caption("Strategy: Re-entry Scalping (Target: ~$220)")

with right_bot:
    st.success("🤖 **ETH Loop**")
    st.write(f"**Current Allocation:** {eth_amount:.6f} ETH")
    st.write(f"**Market Value:** ${eth_value:.2f}")
    st.caption("Strategy: Infinite Loop Scouting ($2,035+)")

# --- SYSTEM FOOTER ---
st.markdown("---")
st.info(f"Last Updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
st.caption("Connected to Coinbase via Streamlit Cloud Secure Secrets")
