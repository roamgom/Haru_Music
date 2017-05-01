from slacker import Slacker
import json

with open ('config.json', 'r') as cf:
    config = json.load(cf)

api_key = config['CI']['api_token']
ci_hook_url = config['CI']['hook_url']

slack = Slacker(api_key)

slack.chat.post_message('#gom_lab', 'Hello! Testing!')

response = slack.users.list()
users = response.body['members']


