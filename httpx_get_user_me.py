import httpx


login_payload = {
    "email": "abzalovmx@gmail.com",
    "password": "string123"
}


login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]


user_me_response = httpx.get(
    "http://localhost:8000/api/v1/users/me",
    headers={"Authorization": f"Bearer {access_token}"}
)
user_me_response_data = user_me_response.json()
print(user_me_response_data)
print(user_me_response.status_code)
