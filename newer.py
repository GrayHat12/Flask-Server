from flask import Flask , request, jsonify
import requests
import time
import threading
import json
from youtube import Search,SearchMore,GetSong

def repeat():
    while True:
        time.sleep(180)
        print(requests.get('https://gray-server.herokuapp.com/').text)

app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
	return 'GrayHat : gray-hat.me'

@app.route('/search',methods=['POST'])
def search():
    search = ''
    try:
        req_data = request.get_json()
        search = req_data['search']
    except:
        return {'error' : 'search compulsory'}
    try:
        sess = req_data['sessionToken']
        tok = req_data['continuation']
        click = req_data['clickTrackingParams']
        ob2 = SearchMore(sess,tok,click,search)
        ob2.compute()
        v2 = ob2.prepare()
        return jsonify(v2)
    except:
        ob = Search(search)
        ob.compute()
        v2 = ob.prepare()
        return jsonify(v2)

@app.route('/song',methods=['POST'])
def getSong():
    req_data = request.get_json()
    ytid = req_data['id']
    return jsonify(GetSong(ytid).getSong())

if __name__ == '__main__': 
    t1 = threading.Thread(target=repeat)
    t1.start()
    app.run()