from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания нового пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для публичных операций с пользователями, не требующих авторизации.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Создаёт нового пользователя в системе.

        :param request: Данные нового пользователя в формате CreateUserRequest.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.client.post("/api/v1/users", json=request)
