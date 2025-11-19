from pydantic import BaseModel, Field, ConfigDict
from typing import List


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание нового упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class ExerciseSchema(BaseModel):
    """
    Описание структуры объекта упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении списка упражнений.
    """
    exercises: List[ExerciseSchema]


class ExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении одного упражнения.
    """
    exercise: ExerciseSchema


class CreateExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании упражнения.
    """
    exercise: ExerciseSchema


class UpdateExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа при обновлении упражнения.
    """
    exercise: ExerciseSchema


class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
