# NightMC bot Recode :octocat:

In my last [code](https://github.com/TheMinecraftExplorer/NightMC-bot) I didn't use cogs but this time I did use them which allows us to understand the files better
Also I have made a better music system using Lavalink :)

### Requirements
1. U need to have a lavalink music server (This is used to directly stream music from youtube) - [Create one for free over here](https://client.bombhost.cloud/)


Libraries Required | What they do
------------------ | ------------
youtube-dl | <details><summary>It gets us information from youtube.</summary> <p> More information can be found [here](https://pypi.org/project/youtube_dl/)</p></details>
discord.py | <details><summary>This is the main Library which allows us to interact with the discord bot and get it running</summary> <p> More information can be found [here](https://pypi.org/project/discord.py/)</p></details>
FFmpeg | <details><summary>This allows us to get the audio from the video youtube-dl fetches.</summary> <p> More information can be found [here](https://ffmpeg.org/)</p></details>
praw | <details><summary>This allows us to fetch information from [reddit](https://www.reddit.com/)</summary> <p> More information can be found [here](https://pypi.org/project/praw/)</p></details>
Pynacl | <details><summary>Pynacl enables us to get data from websites -eg. **youtube** securely</summary> <p> More information can be found [here](https://pypi.org/project/PyNaCl/)</p></details>
chat-exporter | <details><summary>Chat Exporter allows us to get a transcript of a discord channel accurately. We are going to be using this for ticket transcripts</summary> <p> More information can be found [here](https://pypi.org/project/chat-exporter/)</p></details>
lavalink | <details><summary>Lavalink allows us to stream Audio from youtube directly</summary> <p> More information can be found [here](https://lavalink.readthedocs.io/en/latest/overview.html)</p></details>

### The music.py is new so it maybe a little buggy. Please let me know if you guys find any bugs