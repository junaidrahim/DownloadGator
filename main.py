#!/usr/bin/python3

from flask import Flask, request, redirect, render_template, jsonify
from telegram import Telegram
import os,json

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
    os.system("cd " + download_path + " && ls -lh > size.log")
    # take the second word of the first line in Downloads/size.log
    size = open(download_path+"/size.log","r").read().split("\n")[0].split(" ")[1]
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
    append_to_downloads({'link':link,'folder':folder_name})
    os.system("cd {} && mkdir {} && cd {} && {} &".format(download_path,folder_name,folder_name,wget_cmd))

    return redirect("/")

@app.route("/api/monitor",methods=["GET"])
def api_monitor():
    # read the Downloads/downloads.json and append the wget.log of every folder and
    # return that json
    downloads_data = json.loads(open(download_path+"/downloads.json","r").read())
    for i in downloads_data:
        i["wget_log"] = open(download_path+"/"+i["folder"]+"/wget.log","r").read()
    print(downloads_data)
    return jsonify(downloads_data)


def start_telegram():
    Telegram("Junaid")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)