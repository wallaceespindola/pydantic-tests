from pydantic import EmailStr
from pydantic.dataclasses import dataclass

def _norm_name(v: str) -> str:
    return v.strip().title()

def _norm_email(v: str) -> str:
    return v.strip().lower()

@dataclass(frozen=True)
class NameEmail:
    name: str
    email: EmailStr

    def __post_init_post_parse__(self):  # called after pydantic validation in v1
        object.__setattr__(self, "name", _norm_name(self.name))
        object.__setattr__(self, "email", _norm_email(self.email))