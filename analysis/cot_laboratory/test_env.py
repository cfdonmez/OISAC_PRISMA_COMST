import os
import sys

print("Testing Environment...")

# 1. Check Library
try:
    import groq
    print("[OK] Library 'groq' is installed.")
except ImportError:
    print("[FAIL] Library 'groq' is NOT installed.")

# 2. Check API Key
key = os.getenv("GROQ_API_KEY")
if key:
    print(f"[OK] GROQ_API_KEY is set (Length: {len(key)})")
else:
    print("[FAIL] GROQ_API_KEY is NOT set.")
