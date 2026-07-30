import requests
from requests.auth import HTTPBasicAuth

# Step 1: POST request for token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
response = requests.post(
    auth_url,
    auth=HTTPBasicAuth('devnetuser', 'Cisco123!'),
    headers={"Content-Type": "application/json"},
    verify=False
)
print(f"{response.status_code} response code")
print(f"{response.text} .text")
print(f"{response.json()} .json()")
token = response.json().get("Token")
print(f"🔑 Auth Token Acquired: {token[:15]}...")

# Step 2: GET request using token in header
device_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
headers = {
    "X-Auth-Token": token,
    "Content-Type": "application/json"
}

device_response = requests.get(device_url, headers=headers, verify=False)
devices = device_response.json().get("response")
print(device_response.json())
print(devices)

print(f"📡 Found {len(devices)} network devices in DNAC:")
for dev in devices[:2]:  # Print first 2
    print(f" - {dev.get('hostname')} ({dev.get('managementIpAddress')}) -> {dev.get('reachabilityStatus')}")