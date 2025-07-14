import os
SHOPIFY_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN")
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
print(f"[✓] Syncing products to {SHOPIFY_DOMAIN}")
