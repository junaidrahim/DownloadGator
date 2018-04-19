import requests,json

class Telegram:
    def __init__(self,token,user_id):
        self.both_auth_token = token
        self.user_id = user_id
    
    def sendServerStartedMessage(self):
        token = self.both_auth_token
        user_id = self.user_id

        ngrok_data = json.loads(requests.get("http://127.0.0.1:4040/api/tunnels",headers={"Content-Type":"application/json"}).text)
        self.public_url = ngrok_data["tunnels"][1]["public_url"]

        try:   
            requests.post("https://api.telegram.org/bot" + token + "/sendMessage",data={'chat_id':user_id, 'text': "DownloadGator Server was started on " + str(self.public_url)})
        except Exception as e:
            requests.post("https://api.telegram.org/bot" + token + "/sendMessage",data={'chat_id':user_id, 'text':e})

    def sendServerStoppedMessage(self):
        token = self.both_auth_token
        user_id = self.user_id

        try:   
            requests.post("https://api.telegram.org/bot" + token + "/sendMessage",data={'chat_id':user_id, 'text': "DownloadGator Server on " + str(self.public_url) + " was stopped"})
        except Exception as e:
            requests.post("https://api.telegram.org/bot" + token + "/sendMessage",data={'chat_id':user_id, 'text':e})
