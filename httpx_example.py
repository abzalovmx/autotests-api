import httpx


# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1", verify=False)
#
# print(response.status_code)
# print(response.json())
#
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data, verify=False)
#
# print(response.status_code)
# print(response.json())
#
#
# data = {
#     "username": "test_user",
#     "password": "123456"
# }
#
# response = httpx.post("https://httpbin.org/post", data=data, verify=False)
#
# pprint(response.status_code)
# pprint(response.json())

# headers = {"Authorization": "Bearer test_token"}
#
# response = httpx.get("https://httpbin.org/get", headers=headers, verify=False)
#
# pprint(response.request.headers)
# pprint(response.json())

# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params, verify=False)
# pprint(response.url)
# pprint(response.json())


# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files, verify=False)
#
#
# pprint(response.json())


# with httpx.Client(verify=False) as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# pprint(response1.json())
# pprint(response2.json())


# client = httpx.Client(headers={"Authorization": "Bearer <KEY>"}, verify=False)
# response = client.get("https://httpbin.org/get")
#
# pprint(response.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid", verify=False)
#     response.raise_for_status()
# except httpx.HTTPError as e:
#     print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("https://httpbin.org/get", timeout=2, verify=False)
    response.raise_for_status()
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
