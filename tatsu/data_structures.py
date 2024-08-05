import datetime


class UserProfile:
    def __init__(
        self,
        avatar_hash: str,
        avatar_url: str,
        credits_: int,
        discriminator: str,
        user_id: int,
        info_box: str,
        reputation: int,
        subscription_type: int,
        subscription_renewal: datetime.datetime,
        title: str,
        tokens: int,
        username: str,
        xp: int,
        original: dict,
    ):
        self.avatar_hash: str = avatar_hash
        self.avatar_url: str = avatar_url
        self.credits: int = credits_
        self.discriminator: str = discriminator
        self.user_id: int = int(user_id) if user_id else user_id
        self.info_box: str = info_box
        self.reputation: int = reputation
        self.subscription_type: int = subscription_type
        self.subscription_renewal: datetime.datetime = subscription_renewal
        self.title: str = title
        self.tokens: int = tokens
        self.username: str = username
        self.xp: int = xp
        self.original: dict = original

    def __str__(self):
        return (
            f"UserProfile(avatar_hash={self.avatar_hash}, avatar_url={self.avatar_url}, credits={self.credits}, "
            f"discriminator={self.discriminator}, user_id={self.user_id}, info_box={self.info_box}, "
            f"reputation={self.reputation}, subscription_type={self.subscription_type}, "
            f"subscription_renewal={self.subscription_renewal}, title={self.title}, tokens={self.tokens}, "
            f"username={self.username}, xp={self.xp}, original={self.original})"
        )

    def __eq__(self, other):
        if isinstance(other, UserProfile):
            return self.user_id == other.user_id
        return False

    def __repr__(self):
        return (
            f"UserProfile(avatar_hash={self.avatar_hash!r}, avatar_url={self.avatar_url!r}, credits={self.credits!r}, "
            f"discriminator={self.discriminator!r}, user_id={self.user_id!r}, info_box={self.info_box!r}, "
            f"reputation={self.reputation!r}, subscription_type={self.subscription_type!r}, "
            f"subscription_renewal={self.subscription_renewal!r}, title={self.title!r}, tokens={self.tokens!r}, "
            f"username={self.username!r}, xp={self.xp!r}, original={self.original!r})"
        )

    def to_dict(self):
        return {
            "avatar_hash": self.avatar_hash,
            "avatar_url": self.avatar_url,
            "credits": self.credits,
            "discriminator": self.discriminator,
            "user_id": self.user_id,
            "info_box": self.info_box,
            "reputation": self.reputation,
            "subscription_type": self.subscription_type,
            "subscription_renewal": self.subscription_renewal,
            "title": self.title,
            "tokens": self.tokens,
            "username": self.username,
            "xp": self.xp,
            "original": self.original,
        }


class GuildRankings:
    def __init__(self, guild_id: int, rankings: list, original: dict):
        self.guild_id: int = int(guild_id) if guild_id else guild_id
        self.rankings: list = rankings
        self.original: dict = original

    def __str__(self):
        return (
            f"GuildRankings(guild_id={self.guild_id}, rankings={self.rankings}, "
            f"original={self.original})"
        )

    def __eq__(self, other):
        if isinstance(other, GuildRankings):
            return self.guild_id == other.guild_id
        return False

    def __repr__(self):
        return (
            f"GuildRankings(guild_id={self.guild_id!r}, rankings={self.rankings!r}, "
            f"original={self.original!r})"
        )

    def to_dict(self):
        return {
            "guild_id": self.guild_id,
            "rankings": self.rankings,
            "original": self.original,
        }


class RankingObject:
    def __init__(
        self, rank: int, score: int, user_id: int, original: dict, guild_id: int = None
    ):
        self.rank: int = rank
        self.score: int = score
        self.user_id: int = int(user_id) if user_id else user_id
        self.original: dict = original
        self.guild_id: int = int(guild_id) if guild_id else guild_id

    def __str__(self):
        return (
            f"RankingObject(rank={self.rank}, score={self.score}, user_id={self.user_id}, "
            f"original={self.original}, guild_id={self.guild_id})"
        )

    def __eq__(self, other):
        if isinstance(other, RankingObject):
            return self.user_id == other.user_id and self.guild_id == other.guild_id
        return False

    def __repr__(self):
        return (
            f"RankingObject(rank={self.rank!r}, score={self.score!r}, user_id={self.user_id!r}, "
            f"original={self.original!r}, guild_id={self.guild_id!r})"
        )

    def to_dict(self):
        return {
            "rank": self.rank,
            "score": self.score,
            "user_id": self.user_id,
            "original": self.original,
            "guild_id": self.guild_id,
        }


class StorePrice:
    CURRENCY_MAP = {
        0: "Credits",
        1: "Tokens",
        2: "Emeralds",
        3: "Candy Cane",
        4: "United States Dollar (USD)",
        5: "Candy Corn",
    }

    def __init__(self, currency: int, amount: float):
        self.currency: int = currency
        self.amount: float = amount

    def __str__(self):
        currency_str = self.CURRENCY_MAP.get(self.currency, "Unknown")
        return f"StorePrice(currency={currency_str}, amount={self.amount})"

    def __repr__(self):
        currency_str = self.CURRENCY_MAP.get(self.currency, "Unknown")
        return f"StorePrice(currency={currency_str!r}, amount={self.amount!r})"

    def __eq__(self, other):
        if isinstance(other, StorePrice):
            return self.currency == other.currency and self.amount == other.amount
        return False

    def to_dict(self):
        return {
            "currency": self.currency,
            "amount": self.amount,
        }


class StoreListing:
    def __init__(
        self,
        listing_id: str,
        name: str,
        summary: str,
        description: str,
        new: bool,
        preview: str = None,
        prices: list = None,
        categories: list = None,
        tags: list = None,
    ):
        self.listing_id: str = listing_id
        self.name: str = name
        self.summary: str = summary
        self.description: str = description
        self.new: bool = new
        self.preview: str = preview
        self.prices: list = prices if prices is not None else []
        self.categories: list = categories if categories is not None else []
        self.tags: list = tags if tags is not None else []

    def __str__(self):
        return (
            f"StoreListing(listing_id={self.listing_id}, name={self.name}, summary={self.summary}, "
            f"description={self.description}, new={self.new}, preview={self.preview}, "
            f"prices={self.prices}, categories={self.categories}, tags={self.tags})"
        )

    def __eq__(self, other):
        if isinstance(other, StoreListing):
            return self.listing_id == other.listing_id
        return False

    def __repr__(self):
        return (
            f"StoreListing(listing_id={self.listing_id!r}, name={self.name!r}, summary={self.summary!r}, "
            f"description={self.description!r}, new={self.new!r}, preview={self.preview!r}, "
            f"prices={self.prices!r}, categories={self.categories!r}, tags={self.tags!r})"
        )

    def to_dict(self):
        return {
            "listing_id": self.listing_id,
            "name": self.name,
            "summary": self.summary,
            "description": self.description,
            "new": self.new,
            "preview": self.preview,
            "prices": [price.to_dict() for price in self.prices],
            "categories": self.categories,
            "tags": self.tags,
        }
