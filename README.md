# Tatsumaki.py

An async python api wrapper for the [Tatsu API](https://dev.tatsu.gg/).

---

## Set up guide:

1. Download the library with the `pip install tatsumaki.py` command
2. Import the library: `from tatsumaki.wrapper import ApiWrapper`

## Code examples:

- Get the information of a user
```python
from tatsumaki.wrapper import ApiWrapper

async def get_profile():
    wrapper = ApiWrapper(key="API_KEY_HERE")
    user_profile = await wrapper.get_profile(274561812664549376)
    return user_profile.credits
```

- Get the ranking of a user:
```python
from tatsumaki.wrapper import ApiWrapper

async def get_member_ranking():
    wrapper = ApiWrapper(key="API_KEY_HERE")
    result = await wrapper.get_member_ranking(573885009820254239, 274561812664549376)
    return result.rank
```

- Get the rankings of a server with an offset 
```python
from tatsumaki.wrapper import ApiWrapper

async def get_ranks():
    wrapper = ApiWrapper(key="API_KEY_HERE")
    result = await wrapper.get_guild_rankings(573885009820254239, offset=100)
    return result.rankings[0].rank # This will be 101
```




