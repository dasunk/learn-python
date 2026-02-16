name: str = "Dasun Liyanage"
age: int = 30
is_active: bool = True

def greet(name: str) -> str:
    return f"Hello, {name}"

def add (a: int, b: int) -> int:
    return a + b

# what are optional parameters and defaults?

number: list[int] = [1, 2, 3]
number.append(4)
first = number[0]

# learn about slicing when the time comes.

user: dict[str, any] = {
    "name": "Dasun Liyanage",
    "age": 30
}

user_name = user["name"]
user_age = user.get("age")  # safe access, returns None if missing

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None = None     # Optional field with default

admin = User(name="Dasun Liyanage", age=30)
print(admin.name)

# what are dataclasses?