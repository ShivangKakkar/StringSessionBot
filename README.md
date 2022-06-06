# Pyrogram and Telethon String Session Bot [@StarkStringGenBot](https://t.me/StarkStringGenBot)

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/StarkBotsIndustries/StringSessionBot"><img src="https://telegra.ph/file/7ec22c82f580a334dd13e.jpg" width="2000"></a></p>

Telegram bot to generate pyrogram and telethon string session.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/StarkBotsIndustries/StringSessionBot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN` (and `MUST_JOIN`).
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/StarkBotsIndustries/StringSessionBot
   ```
2. Get a `DATABASE_URL`. If you don't know how, deploy using Heroku Button only or delete database things as it's not a compulsion.
   
3. Rename `.env.sample` to `.env` and fill the needed variables

4. Enter the directory
   ```markdown
   cd StringSessionBot
   ```

5. Install all the dependencies
   ```markdown
   pip install -r requirements.txt
   ```

6. Run the file
   ```markdown
   python3 bot.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `DATABASE_URL` - Will be automatically added by Heroku.
- `MUST_JOIN` - Username/ID of your telegram channel/group.

## Functions

- Generate Pyrogram user string session
- Generate Pyrogram bot string session
- Generate Pyrogram (Major) Version 1 and 2 string sessions
- Generate Telethon string session


## To-Do

> That's on you mainly...

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library
- [Lonami](https://github.com/Lonami) for his [Telethon](https://docs.telethon.dev) Library 
- [aylak](https://t.me/ayIak) for **Telethon** idea of [v1.0.0](https://github.com/StarkBotsIndustries/StringSessionBot/commit/48e06bb6d9ed156797ef4bc0dab88820fef948f3)

## Support

Channel :- [@StarkBots](https://t.me/StarkBots)

Group Chat :- [@StarkBotsChat](https://t.me/StarkBotsChat)

## :)

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/StarkBotsIndustries)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/StarkBotsIndustries)
