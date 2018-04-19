# DownloadGator

### Simplest Web App to Start a file download remotely on the server. Could be used by college students who have limited internet access in their colleges to remotely put stuff to download on a server hosted at home(tv shows and stuff). Server can be hosted using [ngrok](https://ngrok.com/) and connecting it to a Telegram Bot can notify about Server activities

## How to Start ?

#### Dependencies:
1. Flask
2. Wget (built-in in linux, need to install on windows)
3. Python 3

The server is started using ngrok. When the server starts, a message with the url is sent to the Telegram bot @downloadgator_bot (Download Telegram from Google Playstore)

**Add your telegram user id in the `main.py` file on line 65, else it won't work.**
**You can get your id from the @get_id_bot in Telegram**

1.   Make the `start_server.sh` file executable and run with `./start_server.sh` or
2.   Run `sh start_server.sh`

To clear the `Downloads/` folder and reset the `Downloads/downloads.json` file, run the `reset_downloads.sh` file on the server by either
1.  `sh reset_downloads.sh`  or
2.  `./reset_downloads.sh` (make it executable before running)




## Features to be Added:

1.  Cancel a particular Download
2.  Alert whether Download was started or not
3.  Server Download Speed Data


## Screenshots

> ![Main](screenshots/a.png)


> ![Main](screenshots/b.png)


> ![Main](screenshots/c.png)