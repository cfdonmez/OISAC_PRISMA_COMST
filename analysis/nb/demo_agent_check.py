import os
import sys
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

def check_agent_capability():
    print("=== Antigravity Agent Capability Check ===")
    print(f"Python: {sys.version.split()[0]}")
    
    # 1. Check Library
    try:
        import google.generativeai as genai
        print("[OK] Library 'google-generativeai' is installed.")
    except ImportError:
        print("[FAIL] Library 'google-generativeai' is MISSING.")
        print("       Please run: pip install google-generativeai")
        return

    # 2. Check API Key
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    if not api_key:
        print("\n[WARN] Environment variable 'GOOGLE_API_KEY' is NOT set.")
        print("       Expected setup: $env:GOOGLE_API_KEY='your-key'")
        print("       To proceed with a one-time test, you can enter it now.")
        
        try:
            api_key = input("Enter your GOOGLE_API_KEY (hidden input not supported in all terminals): ").strip()
        except EOFError:
            print("\n[FAIL] No input provided.")
            return

        if not api_key:
            print("[FAIL] No API key provided. Exiting.")
            return
    else:
        print(f"[OK] API Key found (starts with: {api_key[:4]}...)")

    # 3. Test Connection
    print("\nAttempting to connect to Gemini API...")
    try:
        genai.configure(api_key=api_key)
        # Use a lightweight model for quick check
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello! Verify you are working correctly as an agent.")
        
        print("\n[SUCCESS] Agent Response:")
        print("-" * 40)
        print(response.text)
        print("-" * 40)
        print("\nYour environment is ready to use agentic features.")
        
    except Exception as e:
        print(f"\n[ERROR] Connection Failed: {e}")
        # print(f"Details: {str(e)}") # Uncomment for debug

if __name__ == "__main__":
    check_agent_capability()
