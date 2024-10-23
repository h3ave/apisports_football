# apisports_football

[![PyPI version](https://img.shields.io/pypi/v/apisports-football)](https://pypi.org/project/apisports-football)
[![python](https://img.shields.io/pypi/pyversions/apisports-football)](https://pypi.org/project/apisports-football)

[Russian version](https://github.com/h3ave/apisports_football/blob/main/README.ru.md)

It's a handy API wrapper that makes it easy to work with <https://www.api-football.com/>.

Official documentation: <https://www.api-football.com/documentation-v3>

## Installing

* With git

```console
git clone https://github.com/h3ave/apisports_football
cd apisports_football
pip install -r requirements.txt
```

* With pip

```console
pip install apisports-football
```

### Dependencies

* Python >= 3.7
* aiohttp
* pydantic
* typing-extensions

### Getting API Key

[Register](https://dashboard.api-football.com/register) on API-Sports.

Go to [profile](https://dashboard.api-football.com/profile?access) and copy key from API-Key field.

### Usage example

```python
import asyncio
from apisports_football import Wrapper

api = Wrapper('TOKEN_HERE')

async def main() -> None:
    data = await api.leagues().get(
        country = 'Spain',
        season = 2024
    )
    print(data)

if __name__ == '__main__':
    asyncio.run(main())
```
