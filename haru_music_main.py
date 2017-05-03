# haru_music_main
from slacker import Slacker
from slackclient import SlackClient
import json
import random

with open ('config\config_sc.json', 'r') as cf:
    config = json.load(cf)
with open ('config\command.json', 'r') as cmd:
    command = json.load(cmd)
with open ('MediaS\music_link.json', 'r') as ml:
    music = json.load(ml)
# Load Bot_Config, Cmd, Music from DIR



api_key = config['CI']['api_token']
ci_hook_url = config['CI']['incoming_webhook']['hook_url']
slack = Slacker(api_key)
send_channel = config['CI']['incoming_webhook']['channel']
# Keys for Haru_Music   (Slacker.Ver)

sc = SlackClient(api_key)
# Keys for Haru_Music   (SlackClient.Ver)


feel_random = random.choice(list(command['Music'].keys()))
genre_random = random.choice(list(music[feel_random].keys()))
artist_random = random.choice(list(music[feel_random][genre_random].keys()))
song_random = random.choice(list(music[feel_random][genre_random][artist_random].keys()))
link_song = (music[feel_random][genre_random][artist_random][song_random])
# Comments/Command/Link For Each Message

hi_comment = command['Message']['say_for'] + '\'', command['Music'][feel_random], '\' ' + command['Message']['say_today']
song_info = 'Genre :', genre_random, ' #Artist :', artist_random, ' #Song :', song_random + '\n'


#slack.chat.post_message(send_channel, text=link_song, attachments=[{"pretext": ''.join(hi_comment), "text": song_info}], unfurl_links='true', username="Haru_Music")
slack.chat.post_message(send_channel, text=link_song, attachments=[{"pretext": ''.join(hi_comment), "text": song_info}], unfurl_links='true', username="Haru_Music", icon_url="")
# Don't know why... if i don't add icon_url, the player doesn't come up...


