#!/usr/bin/env python3
import requests
from requests import post
import twitter # pip install python-twitter
from json import load

with open("twitter.json") as f:
    api = twitter.Api(**load(f))

with open(".bottoken") as f:
    token = f.read().strip()


def get_list_since(since):
#    try:
    timeline = api.GetListTimeline(slug="<TWITTER LIST NAME BUT WITHOUT THE GREATER/LESS THAN SIGNS>", owner_screen_name="<YOUR TWITTER NAME BUT WITHOUT THE GREATER/LESS THAN SIGNS>", since_id=since)
#    except twitter.error.TwitterError:
#        return [], None
    return timeline, timeline[0].id if timeline else None

def post_to_discord(channel, text):
    """ Posts to Discord like a boss """
    if text is False:
        return "cool"
    d = post("https://discordapp.com/api/channels/{}/messages".format(channel),
             json={"content": text},
             headers={"Authorization": "Bot " + token,
                      "User-Agent": "twitter-discord-lists by suv"
                     }).json()
    return "cool"

if __name__ == "__main__":
    with open(".since") as f:
        since = f.read().strip()
    timeline, since = get_list_since(since)
    if since:
        for t in timeline:
            post_to_discord("<CHANGE THIS TO YOUR DISCORD CHANNEL ID BUT WITHOUT THE GREATER/LESS THAN SIGNS>", "https://twitter.com/{}/status/{}".format(t.user.screen_name, t.id))
        with open(".since", "w") as f:
            f.write(str(since))
