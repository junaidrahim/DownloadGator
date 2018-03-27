from flask import Flask, request, redirect, render_template, jsonify
import os

app = Flask(__name__)
download_path = "{}/Downloads/".format(os.getcwd())

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/download",methods=["POST"])
def api_download():
    link = request.form["linkInput"]
    wget_cmd = "wget {} -o wget.log".format(link)
    folder_name = link.split("/")[-1]
    os.system("cd {} && mkdir {} && cd {} && {}".format(download_path,folder_name,folder_name,wget_cmd))
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)