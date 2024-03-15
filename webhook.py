from github_webhook import Webhook
from flask import Flask
import git
import shutil
import datetime


app = Flask(__name__)  
webhook = Webhook(app) 

@app.route("/")        
def hello_world():
    return "Hello, World!"

@webhook.hook()        
def on_push(data):
    print("Got push with: {0}".format(data))
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    destino = "C:/Users/romul/Documents/projeto-integrador-git-backup"+now_str
    shutil.move("C:/Users/romul/Documents/projeto-integrador-git", destino)
    git.Git("C:/Users/romul/Documents").clone("https://github.com/wilwilpopcorn/projeto-integrador-git.git")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)