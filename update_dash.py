import os
# Simple HTML template for your dashboard
html_content = f"""
<!DOCTYPE html>
<html>
<head><title>Shadi's Portfolio</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"></head>
<body>
    <h1>🚀 Live Portfolio Center</h1>
    <div style="padding: 20px; border: 1px solid #ccc; border-radius: 8px;">
        <h2>Total Balance: <strong>$20.96</strong></h2>
        <p style="color: green;">Net Profit: +$5.92 (39%)</p>
        <hr>
        <p>🛡️ <strong>ZEC:</strong> 0.0686 units ($15.82)</p>
        <p>🛡️ <strong>ETH:</strong> 0.0025 units ($5.13)</p>
    </div>
    <p><small>Last Auto-Update: {os.popen('date').read()}</small></p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
