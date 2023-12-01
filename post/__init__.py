from pydantic import BaseModel


class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str


class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
    user_id: int