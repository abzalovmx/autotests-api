from typing import TypedDict, List
from httpx import Response
from clients.api_client import APIClient
from clients.privet_http_builder import get_private_http_client, AuthenticationUserSchema


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


class Exercise(TypedDict):
    """
    Описание структуры объекта упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при получении списка упражнений.
    """
    exercises: List[Exercise]


class ExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при получении одного упражнения.
    """
    exercise: Exercise


class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при создании упражнения.
    """
    exercise: Exercise


class UpdateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при обновлении упражнения.
    """
    exercise: Exercise


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
    Клиент для взаимодействия с API упражнений (/api/v1/exercises).
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с параметром courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод возвращает список упражнений в виде словаря.

        :param query: Словарь с параметром courseId.
        :return: Словарь формата GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> ExerciseResponseDict:
        """
        Метод возвращает данные упражнения в виде словаря.

        :param exercise_id: Идентификатор упражнения.
        :return: Словарь формата ExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания нового упражнения.

        :param
            request: Словарь с параметрами title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExercisesResponseDict:
        """
        Метод создаёт упражнение и возвращает результат в виде словаря.

        :param request: Словарь с параметрами нового упражнения.
        :return: Словарь формата CreateExercisesResponseDict.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления существующего упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с параметрами обновления (title, maxScore, minScore, description, estimatedTime).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExercisesResponseDict:
        """
        Метод обновления упражнения с возвратом результата в виде словаря.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с параметрами обновления.
        :return: Словарь формата UpdateExercisesResponseDict.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Словарь с данными аутентификации пользователя.
    :return: Готовый к использованию экземпляр ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
