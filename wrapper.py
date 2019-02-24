import aiohttp


class ApiWrapper:
    def __init__(self, key):
        self.key = key
        self.base_url = "https://api.tatsumaki.xyz"
        self.headers = {"Authorization": key}
        self.background_url = "https://www.tatsumaki.xyz/images/backgrounds/profile/{}.png"
        self.badge_url = "https://www.tatsumaki.xyz/images/badges/{}.png"

    async def request(self, url):
        # get request to the tatsu api
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as result:
                if result.status != 200:
                    print(result)
                    return False
                try:
                    return await result.json()
                except aiohttp.client_exceptions.ContentTypeError:
                    return eval(await result.text())

    async def put(self, url, data=None):
        # put api calls
        async with aiohttp.ClientSession() as session:
            async with session.put(url=url, headers=self.headers, json=data) as result:
                if result.status != 200:
                    print(result)
                    return False
                return True

    async def user(self, user_id):
        """Returns the available information about a user. Requires a user id"""
        result = await self.request(url=self.base_url + "/users/{}".format(user_id))
        if not result:
            raise Exception("The API is currently having issues, please try again later")
        badges = result.get("badgeSlots", None)
        if badges is not None:
            result["badgeURLs"] = [self.badge_url.format(i) for i in badges]
        return result

    async def leaderboard(self, server_id, rank=10):
        """Returns 10 ranks, where the rank argument is the last rank. Requires a server id and rank limit (default
        is the first 10 ranks)"""
        if rank < 10:
            rank = 10
        result = await self.request(url=self.base_url + "/guilds/{0}/leaderboard".format(server_id))
        if not result:
            raise Exception("The API is currently having issues, please try again later")
        return result[rank-10:rank]


    def update_key(self, key):
        """Update the API key. Requires a new API key"""
        self.key = key
        return True

    async def update_user_score(self, guild, user, amount, action="set"):
        """Update a users server score. Requires a guild id, user id, amount and an action (add, set, remove)
        default is set. You need the manage channels permission in this server to use this. The API endpoint for this
        is currently not working."""
        if amount > 50000 or amount < 0:
            raise Exception("Make sure that the amount is between 0 and 50.000")
        if not action in ["set", "add", "remove"]:
            raise Exception("Make sure that the action is either 'set', 'add' or 'remove'")
        data = {"amount": amount, "action": action}
        result = await self.put(url=self.base_url + "/guilds/{0}/members/{1}/score".format(guild, user), data=data)
        if not result:
            raise Exception("The API is currently having issues, please try again later")
        return True

    async def update_user_points(self, guild, user, amount, action="set"):
        """Update a users server points. Requires a guild id, user id, amount and an action (add, set, remove)
        default is set. You need the manage channels permission in this server to use this. The API endpoint for this
        is currently not working."""
        if amount > 50000 or amount < 0:
            raise Exception("Make sure that the amount is between 0 and 50.000")
        if not action in ["set", "add", "remove"]:
            raise Exception("Make sure that the action is either 'set', 'add' or 'remove'")
        data = {"amount": amount, "action": action}
        result = await self.put(url=self.base_url + "/guilds/{0}/members/{1}/points".format(guild, user), data=data)
        if not result:
            raise Exception("The API is currently having issues, please try again later")
        return True

    async def get_user_stats(self, guild_id, user_id):
        """Get stats about a user. Requires a guild and user id."""
        result = await self.request(url=self.base_url + "/guilds/{0}/members/{1}/stats".format(guild_id, user_id))
        if not result:
            raise Exception("The API is currently having issues, please try again later")
        else:
            return result
