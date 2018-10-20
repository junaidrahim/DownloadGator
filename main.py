#!/usr/bin/python3

from flask import Flask, request, redirect, render_template, jsonify
from telegram import Telegram
import os,json,datetime,subprocess,time

app = Flask(__name__)
download_path = "{}/Downloads/".format(os.getcwd())

def append_to_downloads(data):
    # append the argument to Downloads/downloads.json file
    downloads_json_file = json.loads(open(download_path+"/downloads.json","r").read())
    downloads_json_file.append(data)
    downloads_json_file = json.dumps(downloads_json_file,sort_keys=True, indent=4)
    open(download_path + "/downloads.json","w").write(downloads_json_file)

@app.route("/",methods=["GET"])
def index():
    size = subprocess.check_output(['du','-sh', download_path]).split()[0].decode('utf-8')
    return render_template("index.html",dir_size = size)

@app.route("/monitor",methods=["GET"])
def monitor():
    return render_template("monitor.html")

@app.route("/api/download",methods=["POST"])
def api_download():
    # starting the download
    link = request.form["linkInput"]
    wget_cmd = "wget {} -o wget.log".format(link)
    folder_name = link.split("/")[-1]

    now = datetime.datetime.now()
    current_date_time = str(now).split(" ")[0] + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    try:
        os.mkdir(download_path+"/"+folder_name)
        os.system("cd {} && {} &".format(download_path + "/" + folder_name,wget_cmd))
        append_to_downloads({'time':current_date_time,'link':link,'folder':folder_name})
        
    except OSError:
        print("")
    return redirect("/")

@app.route("/api/monitor",methods=["GET"])
def api_monitor():
    # read the Downloads/downloads.json and append the wget.log of every folder and
    # return that json
    downloads_data = json.loads(open(download_path+"/downloads.json","r").read())
    for i in downloads_data:
        i["wget_log"] = open(download_path+"/"+i["folder"]+"/wget.log","r").read()
    return jsonify(downloads_data)


if __name__ == "__main__":
    time.sleep(5) # some time for ngrok to start

    # Token of DownloadGatorBot (@downloadgator_bot) on Telegram
    bot_token = "580264852:AAHd6JUBxjj6iDoYMH8GN95bwZkZ3A7Byvw"
    
    #Enter your user id on Telegram, its an integer, you can get it from @get_id_bot
    user_id = 470088607 # put your id here
    
    telegram_bot = Telegram(bot_token,user_id) #instantiating the bot
    
    # sending the message to the user that the server was started on this ngrok url
    telegram_bot.sendServerStartedMessage()
    
    app.run(host="0.0.0.0",port=3000)

    telegram_bot.sendServerStoppedMessage()
    raise SystemExit
    