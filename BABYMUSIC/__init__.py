from BABYMUSIC.core.bot import Spotify
from BABYMUSIC.core.dir import dirr
from BABYMUSIC.core.git import git
from BABYMUSIC.core.userbot import Userbot
from BABYMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Spotify()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "Gaana_MusicBot"  # connect music api key "Dont change it"
