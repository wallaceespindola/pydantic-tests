import pydantic
import pytest

# Skip all tests in this module unless pydantic major version is 1
if not pydantic.__version__.startswith("1."):
    pytest.skip("pydantic v1 not installed; skipping v1 tests", allow_module_level=True)

from src.models_v1a import NameEmail
from pydantic import ValidationError


def test_name_email_normalization_v1():
    obj = NameEmail(name="  john SMITH ", email=" John@Email.COM ")
    assert obj.name == "John Smith"
    assert obj.email == "john@email.com"


def test_name_email_invalid_email_v1():
    with pytest.raises(ValidationError):
        NameEmail(name="Jane", email="not-an-email")
