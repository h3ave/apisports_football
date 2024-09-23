# apisports_football
<a href="https://github.com/h3ave/apisports_football/blob/main/README.ru.md">Russian version</a>

It's a handy API wrapper that makes it easy to work with https://www.api-football.com/.

Official documentation: https://www.api-football.com/documentation-v3

### Installing
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
<a href="https://dashboard.api-football.com/register">Register</a> on API-Sports.

Go to <a href="https://dashboard.api-football.com/profile?access">profile</a> and copy key from API-Key field.

### Usage example
```python
import asyncio
from apisports_football.wrapper import Wrapper

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
