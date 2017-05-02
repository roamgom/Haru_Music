from slacker import Slacker
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
# Keys for Haru_Music

feel_random = random.choice(list(command['Music'].keys()))
genre_random = random.choice(list(music[feel_random].keys()))
artist_random = random.choice(list(music[feel_random][genre_random].keys()))
song_random = random.choice(list(music[feel_random][genre_random][artist_random].keys()))
link_song = (music[feel_random][genre_random][artist_random][song_random])

hi_comment = command['Message']['say_hi'] + command['Message']['say_music'] + '\'',feel_random, '\'' + command['Message']['say_today']
song_info = 'Genre :', genre_random, ' #Artist :', artist_random, ' #Song :', song_random + '\n' + link_song


slack.chat.post_message('#gom_lab', text = 'hola!', attachments = [{"pretext": ''.join(hi_comment), "text": ''.join(song_info)}], username = "Haru_Music")

