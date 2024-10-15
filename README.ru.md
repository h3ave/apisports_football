# apisports_football

[![PyPI version](https://img.shields.io/pypi/v/apisports-football)](https://pypi.org/project/apisports-football)
[![python](https://img.shields.io/pypi/pyversions/apisports-football)](https://pypi.org/project/apisports-football)

Это удобная API-обертка, упрощающая работу с <https://www.api-football.com/>.

Официальная документация: <https://www.api-football.com/documentation-v3>

## Установка

* С помощью git

```console
git clone https://github.com/h3ave/apisports_football
cd apisports_football
pip install -r requirements.txt
```

* С помощью пакетного менеджера pip

```console
pip install apisports-football
```

### Зависимости

* Python >= 3.7
* aiohttp
* pydantic
* typing-extensions

### Получение API ключа

[Зарегистрируйтесь](https://dashboard.api-football.com/register) на API-Sports.

Перейдите в [профиль](https://dashboard.api-football.com/profile?access) и скопируйте ключ из поля API-KEY.

### Пример использования

```python
import asyncio
from apisports_football import Wrapper

api = Wrapper('TOKEN_HERE')

async def main() -> None:
    data = await api.leagues().leagues(
        country = 'Spain',
        season = 2024
    )
    print(data)

if __name__ == '__main__':
    asyncio.run(main())
```
