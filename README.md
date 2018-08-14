# Tatsumaki.py
A async python api wrapper for the tatsumaki API https://api.tatsumaki.xyz/.


# Tutorial:

* Download the library with the `pip install tatsumaki.py` command

* Import the library: `from tatsumaki.wrapper import ApiWrapper`

* Code examples:

```
# create an instance of the wrapper
wrapper = ApiWrapper("YOUR-API-KEY")


# get a users server stats, first argument is the server id, second argument is the user id
# example response: {'guild_id': '277954215194787840', 'user_id': '274561812664549376', 'score': '2386', 'points': '96566'}
await wrapper.get_user_stats(277954215194787840, 274561812664549376)


# get a users information, the first argument is the users id
# example response: {'name': 'Pum', 'credits': 6294, 'background': 'opulus_wallhaven_background8_bg', 'title': 'I love hugs （っ・ω・)っ', 'badgeSlots': ['gameico_portal_badge', 'gameico_playstation_badge', 'gameico_pcmr_badge', 'flag_austria_badge', 'gameico_mario_badge', 'gameico_limbo_badge', 'commands-used_t4', 'gameico_bindingofisaac_badge', 'gameico_pokemon_badge', 'gameico_steam_badge', 'gameico_witcher_badge', 'gameico_asscreed_badge'], 'rank': 6525, 'level': 85, 'xp': [9595, 11875], 'total_xp': 511331, 'reputation': 496, 'info_box': 'You can call me Pum :-)', 'avatar_url': 'https://discordapp.com/api/users/274561812664549376/avatars/a_5b5fb9301eda12b836a6ac85316e34af.jpg', 'background_url': 'https://www.tatsumaki.xyz/images/backgrounds/profile/opulus_wallhaven_background8_bg.png', 'badgeURLs': ['https://www.tatsumaki.xyz/images/badges/gameico_portal_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_playstation_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_pcmr_badge.png', 'https://www.tatsumaki.xyz/images/badges/flag_austria_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_mario_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_limbo_badge.png', 'https://www.tatsumaki.xyz/images/badges/commands-used_t4.png', 'https://www.tatsumaki.xyz/images/badges/gameico_bindingofisaac_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_pokemon_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_steam_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_witcher_badge.png', 'https://www.tatsumaki.xyz/images/badges/gameico_asscreed_badge.png']}
# Note: All links are generated and its possible that they won't work
await wrapper.user(274561812664549376)

# get the guilds leaderboard, first argument is the guild id and the second argument can be the last rank (always shows ten ranks)
# example response: [{'user_id': '280031155846381569', 'rank': 11, 'score': '4400'}, ..., {'user_id': '269106790279544832', 'rank': 20, 'score': '2837'}]
await wrapper.leaderboard(277954215194787840, 20))
```
