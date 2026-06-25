from  pydantic import BaseModel
from typing import Optional
# what the user sends to create
# studentcreate-is the schema for creating a student
# (name, email, course, grade)-these are the fields that the user will send to create a studen



class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    grade: float = 0.0

# what the user sends to update
# studentupdate-is the schema for updating a student
# the key difference between studentcreate and studentupdate is that in studentupdate, all the fields are optional, so the user can update any field they want
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[float] = None
# what the user gets back when they request a student
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str
    grade: float = 0.0

    # from_attributes = True #-is a bridge between the SQLAlchemy model and the Pydantic model. It allows the Pydantic model to be created from the SQLAlchemy model, which is useful when we want to return a student from the database to the user. Without this, the model will not be able to be created from the SQLAlchemy model. This is because the SQLAlchemy model uses attributes to define the columns, while the Pydantic model uses fields. By setting from_attributes to True, we are telling Pydantic to create the model from the attributes of the SQLAlchemy model.
    class Config: # a special class that is used to configure the behavior of the Pydantic model. In this case, it is used to specify that the model should be created from attributes of the SQLAlchemy model.
        from_attributes = True # without this, the model will not be able to be created from the SQLAlchemy model. This is because the SQLAlchemy model uses attributes to define the columns, while the Pydantic model uses fields. By setting from_attributes to True, we are telling Pydantic to create the model from the attributes of the SQLAlchemy model.
        