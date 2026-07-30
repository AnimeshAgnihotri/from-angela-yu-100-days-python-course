import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Suppress self-signed SSL warnings in console
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DNACClient:
    """
    A Python client wrapper for interacting with the Cisco Catalyst Center (DNAC) REST API.
    Handles authentication tokens, headers, and request errors under the hood.
    """

    def __init__(self, host, username, password):
        self.host = host.rstrip('/')  # Removes trailing slash if user enters 'https://host/'
        self.username = username
        self.password = password
        self.token = None  # Will hold our short-lived JWT token

    def authenticate(self):
        """
        Obtains a JWT X-Auth-Token from DNAC using Basic Authentication.
        Stores the token in self.token and returns True if successful.
        """
        auth_url = f"{self.host}/dna/system/api/v1/auth/token"

        try:
            response = requests.post(
                auth_url,
                auth=HTTPBasicAuth(self.username, self.password),
                headers={"Content-Type": "application/json"},
                verify=False,
                timeout=10
            )
            response.raise_for_status()  # Throws error if HTTP code is not 200/201

            # Extract and store the token
            self.token = response.json().get("Token")
            print(f"🔑 [SUCCESS] Authenticated! Token stored: {self.token[:15]}...")
            return True

        except requests.exceptions.RequestException as e:
            print(f"❌ [ERROR] Authentication failed: {e}")
            return False

    def _get_headers(self):
        """
        Helper method to build the standard authorization headers for API calls.
        """
        if not self.token:
            # Auto-authenticate if we don't have a token yet
            self.authenticate()

        return {
            "X-Auth-Token": self.token,
            "Content-Type": "application/json"
        }

    def get_devices(self):
        """
        Fetches the complete inventory list of network devices from DNAC.
        Returns a list of device dictionaries.
        """
        device_url = f"{self.host}/dna/intent/api/v1/network-device"

        try:
            response = requests.get(
                device_url,
                headers=self._get_headers(),
                verify=False,
                timeout=15
            )
            response.raise_for_status()

            # Safely extract the inner response list
            devices = response.json().get("response", [])
            print(f"📡 [SUCCESS] Retreived {len(devices)} devices from inventory.")
            return devices

        except requests.exceptions.RequestException as e:
            print(f"❌ [ERROR] Failed to fetch devices: {e}")
            return []


# -------------------------------------------------------------
# TEST BLOCK: Runs ONLY when executing this script directly
# -------------------------------------------------------------
if __name__ == "__main__":
    print("--- Starting DNACClient Day 2 Test ---")

    # 1. Initialize the client instance with sandbox credentials
    client = DNACClient(
        host="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!"
    )

    # 2. Call our class method to get devices (it auto-authenticates!)
    inventory = client.get_devices()

    # 3. Print out key fields from the first 3 devices
    print("\nSample Inventory Output:")
    for dev in inventory:
        print(f" - Hostname: {dev.get('hostname')}")
        print(f"   IP: {dev.get('managementIpAddress')}")
        print(f"   Family: {dev.get('family')}")
        print(f"   Status: {dev.get('reachabilityStatus')}\n")