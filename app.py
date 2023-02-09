from flask import Flask, render_template,request
import json


app = Flask(__name__)

fil=open("ovelser.json")
ovelser=json.load(fil)


def sok_ovelse(okt):
    resultater = []
    for ovelse in ovelser:
        if okt.lower() in ovelse["navn"].lower() or okt.lower() in ovelse["treningstype"].lower():
            resultater.append(ovelse)
    return resultater



@app.route("/")
def index():
    sok_ovelse("m")
    okt = request.args.get("m")
    if okt:
        resultater = sok_ovelse(okt)
    else:
        resultater = []
    
    return render_template("index.html",ovelser=ovelser,resultater=resultater,okt=okt)

app.run(debug=True)