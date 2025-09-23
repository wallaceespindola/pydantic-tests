from pydantic import BaseModel, EmailStr, validator


class NameEmail(BaseModel):
    """Immutable name and email with normalization & validation (Pydantic v1).

    - name: trimmed and title-cased
    - email: trimmed, lowercased, and validated by email-validator
    """

    name: str
    email: EmailStr

    @validator("name", pre=True)
    def _norm_name(cls, v: str) -> str:  # type: ignore[override]
        return v.strip().title()

    @validator("email", pre=True)
    def _norm_email(cls, v: str) -> str:  # type: ignore[override]
        return v.strip().lower()

    class Config:
        allow_mutation = False  # makes the model effectively frozen
