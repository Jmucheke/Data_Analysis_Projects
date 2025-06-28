import requests

# Path to your text file with comma-separated API keys
api_keys_file = "./keys/keys.txt"

# Replace with the actual API endpoint you want to test
api_url = "https://api.openai.com/v1/models"

# Read and clean API keys from file
with open(api_keys_file, "r") as f:
    content = f.read()
    api_keys = [key.strip() for key in content.split(",") if key.strip()]

# Function to test a single API key
def test_api_key(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",  # Modify this based on how your API expects the key
    }
    try:
        response = requests.get(api_url, headers=headers, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Main logic to test all keys
working_keys = []
non_working_keys = []

for key in api_keys:
    if test_api_key(key):
        print(f"[✔] Working: {key}")
        working_keys.append(key)
    else:
        print(f"[✖] Not Working: {key}")
        non_working_keys.append(key)

# Summary
print("\n=== Test Summary ===")
print(f"Total Keys Tested: {len(api_keys)}")
print(f"Working Keys: {working_keys}")
print(f"Non-Working Keys: {non_working_keys}")
