import pytest
import pydantic

# Skip all tests in this module unless pydantic major version is 2
if not pydantic.__version__.startswith("2."):
    pytest.skip("pydantic v2 not installed; skipping v2 tests", allow_module_level=True)

from src.models_v2 import NameEmail
from pydantic import ValidationError


def test_name_email_normalization_v2():
    obj = NameEmail(name="  john SMITH ", email=" John@Email.COM ")
    assert obj.name == "John Smith"
    assert obj.email == "john@email.com"


def test_name_email_invalid_email_v2():
    with pytest.raises(ValidationError):
        NameEmail(name="Jane", email="not-an-email")
