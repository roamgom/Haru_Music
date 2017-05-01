from slacker import Slacker
import json

with open ('config\config_sc.json', 'r') as cf:
    config = json.load(cf)
with open ('config\channels.json', 'w') as cw:
    channels = json(cw)

api_key = config['CI']['api_token']
ci_hook_url = config['CI']['hook_url']
slack = Slacker(api_key)

