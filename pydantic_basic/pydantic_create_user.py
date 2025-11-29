from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    UserSchema — схема данных пользователя.

    Поля:
    - id: уникальный идентификатор пользователя
    - email: e-mail пользователя
    - last_name: фамилия
    - first_name: имя
    - middle_name: отчество
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    CreateUserRequestSchema — модель запроса на создание пользователя.

    Поля:
    - email: e-mail пользователя
    - password: пароль
    - last_name: фамилия
    - first_name: имя
    - middle_name: отчество
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    CreateUserResponseSchema — модель ответа на создание пользователя.

    Поля:
    - user: данные созданного пользователя (UserSchema)
    """
    user: UserSchema
