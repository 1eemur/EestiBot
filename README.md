# EestiBot 🇪🇪

A Discord bot designed to help users learn Estonian through interactive dictionary lookups, word case displays, and helpful language learning resources.

### 📚 Estonian Dictionary
- **Word Definitions**: Get comprehensive Estonian definitions with English translations
- **Grammatical Cases**: Display all grammatical cases for nouns, adjectives, and verbs
- **Part of Speech**: Automatic detection and display of word types
- **API Integration**: Uses the official Estonian dictionary API (api.sonapi.ee)

## Commands

### Dictionary Commands
- `!define <word>` or `!d <word>` - Show Estonian definitions for a word
- `!edefine <word>` or `!ed <word>` - Show English translated definitions
- `!cases <word>` or `!c <word>` - Display grammatical cases for a word

### Learning Commands
- `!quickstart` or `!qs` - Get started with Estonian learning resources
- `!kuskustkuhu` - Learn the difference between kus/kust/kuhu
- `!speakly` - Information about Speakly language learning platform

### General Commands
- `!hommik` - Friendly Estonian greeting
- `!listcommands` - Show all available commands
- `!sourcecode` or `!lähtekood` - Link to bot's source code

### Fun Commands
- `!clearskies`
- `!theia`
- `!alatiolnud`
- `!alatihommik`

### Setup Instructions

1. **Clone or download the bot files**
   ```bash
   git clone https://github.com/1eemur/EestiBot.git
   ```

2. **Install dependencies**
   ```bash
   cd EestiBot
   pip install -r requirements.txt
   ```

3. **Create a Discord bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications/)
   - Create a new application and bot
   - Copy the bot token

4. **Configure the bot**
   - Edit `config/constants.ini`
   - Add your bot token:
   ```ini
   [CONSTANTS]
   BOTTOKEN=your_discord_bot_token_here
   ```

5. **Enable privileged intents**
   - In the Discord Developer Portal, go to Bot → Privileged Gateway Intents
   - Enable **Message Content Intent**
   - Save changes

6. **Invite the bot to your server**
   - In the Developer Portal, go to OAuth2 → URL Generator
   - Select "bot" scope and necessary permissions
   - Use the generated URL to invite the bot

7. **Run the bot**
   ```bash
   python main.py
   ```

## Project Structure

```
EestiBot/
├── main.py                    # Main bot entry point
├── requirements.txt           # Python dependencies
├── config/
│   ├── __init__.py
│   ├── settings.py           # Configuration management
│   └── constants.ini         # Bot token and settings
├── cogs/
│   ├── __init__.py
│   ├── general.py            # General utility commands
│   ├── estonian.py           # Estonian dictionary commands
│   └── fun.py               # Entertainment commands
├── services/
│   ├── __init__.py
│   ├── api_service.py        # Estonian API integration
│   └── translation_service.py # Google Translate integration
└── utils/
    ├── __init__.py
    └── helpers.py            # Utility functions and word processing
```

## API Usage

EestiBot uses the [unofficial Sõnaveeb Dictionary API](https://api.sonapi.ee/) to provide accurate linguistic data.

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Support

For support or questions:
- Create a new issue for bugs or feature requests
- Join Estonian learning communities on Discord
