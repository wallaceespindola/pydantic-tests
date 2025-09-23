# Pydantic v1 vs v2 Comparison

This repo demonstrates the same class model implemented for **Pydantic 1.10.23** and **Pydantic 2.11.9**, with unit tests for each. The tests auto-skip the implementation that doesn't match your installed Pydantic version.

## 1) Setup a virtual environment

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

### Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

## 2) Choose your Pydantic version
Open `requirements.txt` and **uncomment exactly one** of the Pydantic lines (v1 or v2), leaving the other commented out. `email-validator` is required for `EmailStr` and is already listed.

## 3) Install dependencies
```bash
pip install -r requirements.txt
or
pip install -e .
```

> If your Windows environment has a private mirror and fails to find `annotated-types` when using Pydantic v2, either ask infra to sync it or install with a public fallback:
>
> ```bash
> pip install -r requirements.txt
> ```

## 4) Run tests
```bash
pytest -q
```

- If you installed **Pydantic v2**, only `tests/test_v2.py` will run; v1 tests are skipped.
- If you installed **Pydantic v1**, only `tests/test_v1.py` will run; v2 tests are skipped.

## 5) Try it interactively
```python
from src.models_v2 import NameEmail  # or models_v1, depending on your installed version
obj = NameEmail(name="  john SMITH ", email=" John@Email.COM ")
print(obj)
```

## Notes
- **Immutability**: v1 uses `Config.allow_mutation = False`; v2 uses `model_config = {"frozen": True}`.
- **Normalization**: both versions trim whitespace; `name` is title-cased; `email` is lowercased.
- **Validation**: `EmailStr` requires the `email-validator` package (already in requirements).

## Author

- Wallace Espindola, Sr. Software Engineer / Solution Architect / Java & Python Dev
- **LinkedIn:** [linkedin.com/in/wallaceespindola/](https://www.linkedin.com/in/wallaceespindola/)
- **GitHub:** [github.com/wallaceespindola](https://github.com/wallaceespindola)
- **E-mail:** [wallace.espindola@gmail.com](mailto:wallace.espindola@gmail.com)
- **Twitter:** [@wsespindola](https://twitter.com/wsespindola)
- **Gravatar:** [gravatar.com/wallacese](https://gravatar.com/wallacese)
- **Dev Community:** [dev.to/wallaceespindola](https://dev.to/wallaceespindola)
- **DZone Articles:** [DZone Profile](https://dzone.com/users/1254611/wallacese.html)
- **Pulse Linkedin:** [LinkedIn Articles](https://www.linkedin.com/in/wallaceespindola/recent-activity/articles/)
- **Website:** [W-Tech IT Solutions](https://www.wtechitsolutions.com/)
- **Substack:** [wallaceespindola.substack.com](https://wallaceespindola.substack.com/)
- **Medium:** [medium.com/@wallaceespindola](https://medium.com/@wallaceespindola) 
- **Slides:** [Speakerdeck](https://speakerdeck.com/wallacese)

## License

- This project is released under the Apache 2.0 License.
- See the [LICENSE](LICENSE) file for details.
- Copyright © 2025 [Wallace Espindola](https://github.com/wallaceespindola/).
