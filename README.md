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

```
>>> import os
>>> from gmusic_account_summary.utils import *
>>> api = login(os.getenv('DEVICE_ID'))
>>> top_5_artists = top_n_things(api, 'artist', 5)
>>> for i in range(len(top_5_artists)):
...     print(str(i+1) + '. ' + top_5_artists[i])
... 
1. Frightened Rabbit
2. The Front Bottoms
3. You Blew It!
4. Modern Baseball
5. Kate Nash
>>> top_5_genres = top_n_things(api, 'genre', 5)
>>> for i in range(len(top_5_genres)):
...     print(str(i+1) + '. ' + top_5_genres[i])
... 
1. Alternative/Indie
2. Pop
3. Rock
4. Emo/Hardcore
5. Indie
```


# The Yearly Review portion

Alright this one requires downloading your My Activity data from takeout.google.com/settings/takeout.

If you uncheck all the boxes and ctrl+f for `My Activity` and then select the file format and ask for json
and then deselect all the other google services except for Google Play Music, for the fastest download and 
I think the data will be too dirty to use for this right now.

If you're having trouble getting it check out the Issues section, or even file an issue (search for one first).

```
from gmusic_account_summary.yearly_review import *

activity = import_my_activity('MyActivity.json')
songs, searches = clean_activities(activity)
top_n_artists(songs, 5, datetime(2019,1,1), datetime(2020,1,1))
```

I have 2 similar functions, the data you get from the download isn't as hydrated as the data from the api. I am thinking
that maybe I can link them by looking up each song and getting the genre.
