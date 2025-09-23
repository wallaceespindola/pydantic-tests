from typing import Annotated
from pydantic import BaseModel, EmailStr, BeforeValidator


class NameEmail(BaseModel):
    """Immutable name and email with normalization & validation (Pydantic v2)."""

    name: Annotated[str, BeforeValidator(lambda v: v.strip().title())]
    email: Annotated[EmailStr, BeforeValidator(lambda v: v.strip().lower())]

    model_config = {"frozen": True}
