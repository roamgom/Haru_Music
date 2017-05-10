# :beers: Haru_Music [V0.1]
## **UPDATE ON PROCESS**

### 1. Music Parcing From SoundCloud Account
### 2. Automatically Add Song List on `music_link.json`
-----------

## Send Your Own Music from Soundcloud to Slack Daily!


### **config/config_sc.json.example**
> "api_token": #"Your Slack_API_Token"
>>    "incoming_webhook":
>>>      "hook_url": "Your_Incoming_Webhook_URL",
>>>      "channel": "#Channel"

#### Change name to 'config_sc.json'
#### Will be added to .gitignore automatically

### **MediaS/music_link.json**
> "Feeling"
>> "Genre"
>>> "Artist"
>>>> "Song_Name" : "URL_LINK"

#### _Based on JSON File Format. Make Your Own List_


### **Make An Instance In AWS or your OWN SERVER, use `Crontab` to set time**
`* * * * * /usr/bin/python /home/usr/dir../haru_music_main.py`
### Minute / Hour / Day / Month / WeekDays |Command|
#### EX) Make Haru_Music Event per 2 hour - `* */2 * * * /usr/bin/python /home/usr/dir../haru_music_main.py`
