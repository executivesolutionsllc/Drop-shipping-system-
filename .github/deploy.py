import os, subprocess

print("[✓] Starting deployment...")
os.system("pip install -r requirements.txt")
subprocess.call(["python", "src/automations/shopify_auto_import.py"])
subprocess.call(["python", "src/webhooks/stripe_payout_handler.py"])
subprocess.call(["python", "src/analytics/payout_report.py"])
print("[✓] Deployment complete.")
