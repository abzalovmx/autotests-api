import httpx
from tools.fakers import get_random_email


create_user_payload = {
  "email": get_random_email(),
  "password": "987654",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


update_user_payload = {
  "email": get_random_email(),
  "lastName": "Name",
  "firstName": "Fname",
  "middleName": "Mname"
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"},
    json=update_user_payload
)
