from flask import Flask , request
import Article
import requests
import GrayAPI
import os
import html
import time
import threading
from youtube import YouTube , Decoder, Search, SearchMore,GetSong

def repeat():
    while True:
        time.sleep(180)
        print(requests.get('https://gray-server.herokuapp.com/').text)
        

app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
	return 'GrayHat : grayhat12.github.io'

@app.route('/hello/<name>') 
def hello_name(name): 
   return 'Hello %s!' % name 

@app.route('/news',methods=['POST'])
def news():
    req_data = request.get_json()
    search = req_data['search']
    out = {}
    if search:
        ob = GrayAPI.GrayNews(search)
        out.update({"makeReq":ob.makeRequest()})
        out.update({"source" : ob.getSource()})
        out.update({"reqError" : ob.getRequestError()})
        art = ob.getArticles()
        nart = []
        for ar in art:
            dic = {}
            dic.update({"author" : html.unescape(ar.getAuthor())})
            dic.update({"class1" : html.unescape(ar.getClass1())})
            dic.update({"class2" : html.unescape(ar.getClass2())})
            dic.update({"image" : ar.getImage()})
            dic.update({"publishedAt" : ar.getPublishedAt()})
            dic.update({"desc" : html.unescape(ar.getShortDesc())})
            dic.update({"title" : html.unescape(ar.getTitle())})
            dic.update({"url" : ar.getUrl()})
            nart.append(dic)
        out.update({"articles" : nart})
    return out

@app.route('/youtube',methods=['POST'])
def youtube():
    try:
        req_data = request.get_json()
        search = req_data['search']
        continued = int(req_data['more'])
        prevList=[]
        if continued==1:
            prevList = list(req_data['prev'])
        yt = YouTube()
        yt.NewMain(search,prevList)
        yturl = list(yt.getLinks())
        try :
            maax = int(req_data['items'])
            if maax > 0 and maax < len(yturl):
                yturl=yturl[:maax]
        except :
            return {"error" : "Invalid json data. items field compulsory"}
        lst = {}
        for url in yturl:
            dcdr = Decoder(url)
            lst.update({url : dcdr.getDat()})
        data= {"data" : lst}
        data.update({"search" : search})
        data.update({"items" : len(lst)})
        return data
    except Exception as ex:
        return({"error":ex})
    
@app.route('/video',methods=['POST'])
def video():
    lst={}
    req_data = request.get_json()
    vidid = req_data['videoId']
    dcdr = Decoder(vidid)
    lst.update({"https://www.youtube.com/watch?v="+vidid:dcdr.getDat()})
    data = {"data":lst}
    data.update({"search":None})
    data.update({"items":1})
    return data

@app.route('/searchyt',methods=['POST'])
def search():
    lst={}
    req_data = request.get_json()
    term = req_data['search']
    obj = Search(term)
    try:
        obj.compute()
    except Exception as ex:
        return {"error" : ex}
    try:
        v2 = obj.prepare()
        return v2
    except Exception as ex:
        return {"error2" : ex}

@app.route('/msearchyt',methods=['POST'])
def searchMore():
    lst={}
    req_data = request.get_json()
    print('Here : ',req_data)
    session = req_data['sessionToken']
    token = req_data['continuation']
    clickparam = req_data['clickTrackingParams']
    term = req_data['search']
    obj = SearchMore(session,token,clickparam,term)
    try:
        obj.compute()
    except Exception as ex:
        print("error 122")
        return {"error 122" : ex}
    try:
        v2 = obj.prepare()
        return v2
    except Exception as ex:
        print("error 127")
        return {"error2 127" : ex}

@app.route('/getSong/<id>',methods=['GET'])
def getSong(id=''):
    if len(id) != 11:
        return {"Error" : "Bad Video Id"}
    ob = GetSong(id)
    return ob.getSong()
    

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With,Access-Control-Allow-Origin"
    return response

if __name__ == '__main__': 
    port = int(os.environ.get('PORT', 5000))
    #t1 = threading.Thread(target=repeat)
    #t1.start()
    app.run(host='0.0.0.0', port=port)