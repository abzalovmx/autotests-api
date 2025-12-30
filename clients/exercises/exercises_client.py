from httpx import Response
from clients.api_client import APIClient
from clients.privet_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    ExerciseResponseSchema,
    CreateExercisesResponseSchema,
    CreateExercisesRequestSchema,
    UpdateExercisesResponseSchema,
    UpdateExercisesRequestSchema
)
import allure
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class ExercisesClient(APIClient):
    """
    Клиент для взаимодействия с API упражнений (/api/v1/exercises).
    """

    @allure.step("Get exercises by course_id {query}")
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с параметром courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод возвращает список упражнений в виде словаря.

        :param query: Словарь с параметром courseId.
        :return: Словарь формата GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Get exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise(self, exercise_id: str) -> ExerciseResponseSchema:
        """
        Метод возвращает данные упражнения в виде словаря.

        :param exercise_id: Идентификатор упражнения.
        :return: Словарь формата ExerciseResponseDict
        """
        response = self.get_exercise_api(exercise_id)
        return ExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Create exercise")
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод создания нового упражнения.

        :param
            request: Словарь с параметрами title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExercisesResponseSchema:
        """
        Метод создаёт упражнение и возвращает результат в виде словаря.

        :param request: Словарь с параметрами нового упражнения.
        :return: Словарь формата CreateExercisesResponseDict.
        """
        response = self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Update exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Метод обновления существующего упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с параметрами обновления (title, maxScore, minScore, description, estimatedTime).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> UpdateExercisesResponseSchema:
        """
        Метод обновления упражнения с возвратом результата в виде словаря.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с параметрами обновления.
        :return: Словарь формата UpdateExercisesResponseDict.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Delete exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом

    :param user: Словарь с данными аутентификации пользователя.
    :return: Готовый к использованию экземпляр ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
