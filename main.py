from flask import Flask , request
import Article
import GrayAPI
import html
from youtube import YouTube , Decoder

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
    req_data = request.get_json()
    search = req_data['search']
    yt = YouTube()
    yt.main(search)
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
    data.update({"items" : req_data['items']})
    return data
    
    

if __name__ == '__main__': 
	app.run() 