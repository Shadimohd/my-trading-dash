import os
from coinbase.wallet.client import Client

# Pulling keys from GitHub Secrets (see Step 3)
api_key = os.getenv('CB_API_KEY')
api_secret = os.getenv('CB_API_SECRET')

try:
    client = Client(api_key, api_secret)
    accounts = client.get_accounts()
    
    # Filter for your specific holdings
    zec = next(a for a in accounts.data if a.currency == 'ZEC')
    eth = next(a for a in accounts.data if a.currency == 'ETH')
    
    zec_bal = float(zec.balance.amount)
    eth_bal = float(eth.balance.amount)
    total_val = float(zec.native_balance.amount) + float(eth.native_balance.amount)
except Exception as e:
    # Fallback to last known good data if API fails
    zec_bal, eth_bal, total_val = 0.0686, 0.0025, 20.96

html_content = f"""
<!DOCTYPE html>
<html>
<head><title>Shadi's Command Center</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"></head>
<body>
    <h1>🚀 Live Portfolio Center</h1>
    <div style="padding: 20px; border: 1px solid #00c853; border-radius: 8px;">
        <h2>Total Balance: <strong>${total_val:.2f}</strong></h2>
        <p>🛡️ <strong>ZEC:</strong> {zec_bal:.4f} units</p>
        <p>🛡️ <strong>ETH:</strong> {eth_bal:.6f} units</p>
    </div>
    <p><small>Last Auto-Update: {os.popen('date').read()}</small></p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
