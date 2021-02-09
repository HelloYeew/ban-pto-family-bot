# Ban P'To and his family Discord bot

 Delete all discord message that include P'To and his family out of your server.

## Function

- Read every message
- Connect with YouTube API to read that is it a clip about P'To family?
- Have a ban list and if it's a new link, and a code detected it will automatically add to this file for faster loding time next time.

## Support Status

- YouTube : Fully Support
- TENOR : Currently not fully support
- GIPHY : Currently not support
- Normal Text : Support by using 'prohibit_keyword' in [check_link.py](check_link.py)
- Photo : Currently not support
- File : Currently not support

## Run This Bot

### Host on Heroku

*Coming Soon*

### Host by your computer

#### Before Run

- Add your bot_token in [main.py](main.py) file

#### Run a bot

You don't want to care about PIP package because if you don't have a required library it will auto install for you.

```shell
$ python3 main.py
```

## Contribute

You can fork this repo and

- Make more function or edit a bot
- Add more ban keyword to let bot detect more by in [check_link.py](check_link.py) or add a link in [ban_link_list](ban_link_list.txt)

Then, pull request!


