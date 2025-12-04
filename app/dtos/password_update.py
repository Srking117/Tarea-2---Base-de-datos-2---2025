from pydantic import BaseModel, Field

class PasswordUpdateDTO(BaseModel):
    current_password: str = Field(..., min_length=3)
    new_password: str = Field(..., min_length=3)
