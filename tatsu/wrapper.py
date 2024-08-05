import httpx
from ratelimit import limits
import datetime

import tatsu.data_structures as ds


class ApiWrapper:
    def __init__(self, key):
        self.key = key
        self.base_url = "https://api.tatsu.gg/v1"
        self.headers = {"Authorization": key}

    @limits(calls=60, period=60)
    async def request(self, url, method="GET", data=None):
        """Directly interact with the API to get the unfiltered results."""
        if method == "GET":
            result = httpx.get(f"{self.base_url}{url}", headers=self.headers)
        elif method == "PUT":
            result = httpx.put(f"{self.base_url}{url}", headers=self.headers, json=data)
        elif method == "PATCH":
            result = httpx.patch(
                f"{self.base_url}{url}", headers=self.headers, json=data
            )
        else:
            raise ValueError("Unsupported HTTP method")

        if result.status_code != 200:
            if result.status_code == 429:
                raise Exception("You are being rate limited.")
            if result.status_code == 401:
                raise Exception("Invalid API key.")
            if result.status_code == 404:
                raise Exception("Invalid endpoint.")
            raise Exception(
                f"Failed to get data from the API. Status code: {result.status_code}"
            )
        return result.json()

    async def get(self, url):
        return await self.request(url, method="GET")

    async def put(self, url, data):
        return await self.request(url, method="PUT", data=data)

    async def patch(self, url, data):
        return await self.request(url, method="PATCH", data=data)

    async def get_profile(self, user_id: int) -> ds.UserProfile:
        """Gets a user's profile. Returns a user object on success."""
        try:
            result = await self.get(f"/users/{user_id}/profile")
        except Exception as e:
            raise e
        subscription_renewal_str = result.get("subscription_renewal")
        subscription_renewal = (
            datetime.datetime.strptime(subscription_renewal_str, "%Y-%m-%dT%H:%M:%SZ")
            if subscription_renewal_str
            else None
        )

        # Map the subscription type to the subscription type object
        subscription_type = result.get("subscription_type", 0)
        subscription_type = ds.SubscriptionType(subscription_type)

        user_profile_data = {
            "avatar_hash": result.get("avatar_hash", None),
            "avatar_url": result.get("avatar_url", None),
            "credits_": result.get("credits", None),
            "discriminator": result.get("discriminator", None),
            "user_id": result.get("id", None),
            "info_box": result.get("info_box", None),
            "reputation": result.get("reputation", None),
            "subscription_type": subscription_type,
            "subscription_renewal": subscription_renewal,
            "title": result.get("title", None),
            "tokens": result.get("tokens", None),
            "username": result.get("username", None),
            "xp": result.get("xp", None),
        }

        user = ds.UserProfile(**user_profile_data)
        return user

    async def get_member_ranking(
        self, guild_id: int, user_id: int, timeframe="all"
    ) -> ds.MemberRanking:
        """Gets the all-time ranking for a guild member. Returns a guild member ranking object on success.
        :param guild_id: The ID of the guild
        :param user_id: The user id
        :param timeframe: Can be all, month or week
        """
        try:
            result = await self.get(
                f"/guilds/{guild_id}/rankings/members/{user_id}/{timeframe}"
            )
        except Exception as e:
            raise e
        rank = self.ranking_object(result)
        return rank

    async def get_guild_rankings(
        self, guild_id, timeframe="all", offset=0
    ) -> ds.GuildRankings:
        """Gets all-time rankings for a guild. Returns a guild rankings object on success.
        :param guild_id: The ID of the guild
        :param timeframe: Can be all, month or week
        :param offset: The guild rank offset
        """
        try:
            result = await self.get(
                f"/guilds/{guild_id}/rankings/{timeframe}?offset={offset}"
            )
        except Exception as e:
            raise e
        rankings = ds.GuildRankings(
            guild_id=result.get("guild_id", None),
            rankings=[self.ranking_object(i) for i in result.get("rankings", [])],
        )
        return rankings

    async def get_guild_member_points(self, guild_id, user_id) -> ds.MemberGuildPoints:
        """Gets a guild member's points. Returns a guild member object on success.
        :param guild_id: The ID of the guild
        :param user_id: The ID of the user
        """
        try:
            result = await self.get(f"/guilds/{guild_id}/members/{user_id}/points")
        except Exception as e:
            raise e
        member = ds.MemberGuildPoints(
            rank=result.get("rank", None),
            points=result.get("points", None),
            user_id=result.get("user_id", None),
            guild_id=result.get("guild_id", None),
        )
        return member

    async def modify_guild_member_points(
        self, guild_id, user_id, amount, action=0
    ) -> ds.MemberGuildPoints:
        """Modifies a guild member's points. Returns the modified guild member object on success.
        :param guild_id: The ID of the guild
        :param user_id: The ID of the user
        :param amount: The amount of points to add or remove
        :param action: The action to take. 0 for add, 1 for remove
        """
        data = {"amount": amount, "action": action}
        try:
            result = await self.patch(
                f"/guilds/{guild_id}/members/{user_id}/points", data
            )
        except Exception as e:
            raise e
        member = ds.MemberGuildPoints(
            rank=result.get("rank", None),
            points=result.get("points", None),
            user_id=result.get("user_id", None),
            guild_id=result.get("guild_id", None),
        )
        return member

    async def modify_guild_member_score(
        self, guild_id, user_id, amount, action=0
    ) -> ds.MemberRanking:
        """Modifies a guild member's score. Returns the modified guild member object on success.
        :param guild_id: The ID of the guild
        :param user_id: The ID of the user
        :param amount: The amount of points to add or remove
        :param action: The action to take. 0 for add, 1 for remove
        """
        data = {"amount": amount, "action": action}
        try:
            result = await self.patch(
                f"/guilds/{guild_id}/members/{user_id}/score", data
            )
        except Exception as e:
            raise e
        member = ds.MemberRanking(
            rank=result.get("rank", None),
            score=result.get("score", None),
            user_id=result.get("user_id", None),
        )
        return member

    async def get_store_listing(self, listing_id) -> ds.StoreListing:
        """Gets a store listing. Returns a store listing object on success.
        :param listing_id: The ID of the store listing
        """
        try:
            result = await self.get(f"/store/listings/{listing_id}")
        except Exception as e:
            raise e

        # Map the prices to the StorePrice object
        prices = result.get("prices", [])
        prices = [
            ds.StorePrice(
                currency=price.get("currency", None),
                amount=price.get("amount", None),
            )
            for price in prices
        ]

        store_listing_data = {
            "listing_id": result.get("id", None),
            "name": result.get("name", None),
            "summary": result.get("summary", None),
            "description": result.get("description", None),
            "new": result.get("new", False),
            "preview": result.get("preview", None),
            "prices": prices,
            "categories": result.get("categories", None),
            "tags": result.get("tags", None),
        }
        store_listing = ds.StoreListing(**store_listing_data)
        return store_listing

    @staticmethod
    def ranking_object(result) -> ds.MemberRanking:
        """Initiate the rank profile"""
        rank = ds.MemberRanking(
            rank=result.get("rank", None),
            score=result.get("score", None),
            user_id=result.get("user_id", None),
        )
        return rank
