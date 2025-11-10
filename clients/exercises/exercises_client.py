from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для взаимодействия с API упражнений (exercises).
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получить список упражнений по courseId.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получить задание по exercise_id.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Создать новое упражнение.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Обновить существующее упражнение.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удалить упражнение по ID.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
