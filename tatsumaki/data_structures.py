class UserProfile:
    def __init__(self, avatar_url, credits_, discriminator, id_, info_box, reputation, title, tokens, username, xp):
        self.avatar_url = avatar_url
        self.credits = credits_
        self.discriminator = discriminator
        self.id = id_
        self.info_box = info_box
        self.reputation = reputation
        self.title = title
        self.tokens = tokens
        self.username = username
        self.xp = xp


class GuildMember:
    def __init__(self, guild_id, rank, score, user_id):
        self.guild_id = guild_id
        self.rank = rank
        self.score = score
        self.user_id = user_id


class GuildRankings:
    def __init__(self, guild_id, rankings):
        self.guild_id = guild_id
        self.rankings: [Ranking] = rankings


class Ranking:
    def __init__(self, rank, score, user_id, guild_id=None):
        self.rank = rank
        self.score = score
        self.user_id = user_id
        self.guild_id = guild_id
