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
    print(f"Resultater: {resultater}")
    return resultater



@app.route("/")
def index():
    try:
        okt = request.args.get("m")
        if okt:
            resultater = sok_ovelse(okt)
        else:
            resultater = []
    
        return render_template("index.html",ovelser=ovelser,resultater=resultater,okt=okt)
    except:
        return render_template("error.html")

app.run(debug=True)



