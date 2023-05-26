# CyberChallenge Scoreboard

A simple auto-updating terminal scoreboard visualizer for the CyberChallenge platform scoreboard and local competition.

## Note

The colors and icons are based on the [Gruvbox](https://github.com/morhetz/gruvbox) color scheme and Apple Emojis. If you have other themes it may not look good. For convenience there is a script (`./setup.sh`) that setups the font and terminal config for xfce.

## Usage

- install the requirements with:

```bash
pip3 install -r requirements.txt
```

- write your access token and scoreboard API URL in the `.env` file, e.g.

```bash
TOKEN="insert_here_your_token"
URL="the_url_of_the_scoreboard"
```

- start the scoreboard with `./scoreboard.py`
