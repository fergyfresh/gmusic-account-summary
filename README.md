# gmusic-account-summary
Inspired by my FOMO around Spotify's End of Year summaries, I atleast wanted some all time summaries for my account.

## How to use

### Setup
You'll need your device ID, which is explained [here](https://github.com/simon-weber/gmusicapi)

Then we can do this:
1. `export DEVICE_ID=<device_id>`
1. git clone this repo.
1. start a virtualenv, or w/e your workflow is to install requirements. `virtualenv .venv -p python3`
1. source that virtualenv `source .venv/bin/activate`
1. `pip install -r requirements.txt`
1. cd to `gmusic_account_summary`
1. run `python` to drop into a python terminal
1. start messing around.


### Quick start
This is what the setup should look like:

```
import os
from gmusic_account_summary.api import *

device_id = os.getenv('DEVICE_ID')

api = login(device_id)

# returns top 10 songs with their song counts
top10_songs(api)
```

Then we can start doing things with `top_n_things`, as long as the song in `api.get_all_songs()` contains
that field this function should just work, if its returning an empty list, that means we couldn't find any
items that had a field that matched your "thing"

"Things" I have tried,

1. genre
2. title
3. artist

### Example usage (less quick start)

Use the api that is returned from the `utils.login` function for these below.

`top_n_things(api, 'artist', 5)` will return top 5 artists.

`top_n_things(api, 'genre', 3)` will return top 5 genres

