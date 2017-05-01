from slacker import Slacker
import json

with open ('config\config_sc.json', 'r') as cf:
    config = json.load(cf)
with open ('config\command.json', 'r') as cmd:
    command = json.load(cmd)
with open ('MediaS\music_link.json', 'r') as ml:
    music = json.load(ml)
# Load Bot_Config, Cmd, Music from DIR


api_key = config['CI']['api_token']
ci_hook_url = config['CI']['hook_url']
slack = Slacker(api_key)
# Keys for Haru_Music
select_motion = [['Calm']]
for selection


slack.chat.post_message('#gom_lab', 'Hola!', username = "Haru_Music")

