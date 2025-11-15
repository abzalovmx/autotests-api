from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True


user = User(id=1, name='<NAME>', email='<EMAIL>')

print(user)
