class UserProfile:
    def __init__(self, avatar_url, credits_, discriminator, id_, info_box,
                 reputation, title, tokens, username, xp, original):
        self.avatar_url: str = avatar_url
        self.credits: int = credits_
        self.discriminator: str = discriminator
        self.id: int = int(id_) if id_ else id_
        self.info_box: str = info_box
        self.reputation: int = reputation
        self.title: str = title
        self.tokens: int = tokens
        self.username: str = username
        self.xp: int = xp
        self.original: int = original


class GuildRankings:
    def __init__(self, guild_id, rankings, original):
        self.guild_id: int = int(guild_id) if guild_id else guild_id
        self.rankings: [RankingObject] = rankings
        self.original: dict = original


class RankingObject:
    def __init__(self, rank, score, user_id, original, guild_id=None):
        self.rank: int = rank
        self.score: int = score
        self.user_id: int = int(user_id) if user_id else user_id
        self.original: dict = original
        self.guild_id: int = int(guild_id) if guild_id else guild_id
