import pafy
import urllib
import requests

class YouTube:
    
    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.outlnk = 'https://www.youtube.com/'
        self.lnks = set()
        self.idn = 'watch?v='
    
    def main(self, query):
        requests.utils.default_headers().update(
            {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11'
            }
        )
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:11+len(self.idn)]
                self.lnks.add(self.outlnk+tmp)
                self.data = self.data[12:]
                #print(self.lnks)
        except ValueError as ve:
            return True
    
    def getLinks(self):
        return self.lnks
    
class Decoder:
    def __init__(self,link):
        self.link = link
    
    def getDat(self):
        dat = pafy.new(self.link)
        data={}
        try:
            data.update({"title" : dat.title})
        except:
            data.update({"title" : "null"})
        try :
            data.update({"author" : dat.author})
        except:
            data.update({"author" : "null"})
        try :
            data.update({"category" : dat.category})
        except:
            data.update({"category" : "null"})
        try :
            data.update({"description" : dat.description})
        except:
            data.update({"description" : "null"})
        try :
            data.update({"likes" : dat.likes})
        except:
            data.update({"likes" : "null"})
        try :
            data.update({"dislikes" : dat.dislikes})
        except:
            data.update({"dislikes" : "null"})
        try :
            data.update({"length" : dat.length})
        except:
            data.update({"length" : "null"})
        try :
            data.update({"published" : dat.published})
        except:
            data.update({"published" : "null"})
        try :
            data.update({"rating" : dat.rating})
        except:
            data.update({"rating" : "null"})
        try :
            data.update({"viewcount" : dat.viewcount})
        except:
            data.update({"viewcount" : "null"})
        audio = {}
        try:
            audio.update({"url" : dat.getbestaudio().url})
        except:
            audio.update({"url" : "null"})
        try:
            audio.update({"bitrate" : dat.getbestaudio().bitrate})
        except:
            audio.update({"bitrate" : "null"})
        try:
            audio.update({"size" : str(int(dat.getbestaudio().get_filesize()/1024))+" bytes"})
        except:
            audio.update({"size" : "null"})
        try:
            audio.update({"extension" : dat.getbestaudio().extension})
        except:
            audio.update({"extension" : "null"})
        video = {}
        try:
            video.update({"url" : dat.getbest().url})
        except:
            video.update({"url" : "null"})
        try:
            video.update({"bitrate" : dat.getbest().bitrate})
        except:
            video.update({"bitrate" : "null"})
        try:
            video.update({"size" : str(int(dat.getbest().get_filesize()/1024))+" bytes"})
        except:
            video.update({"size" : "null"})
        try:
            video.update({"extension" : dat.getbest().extension})
        except:
            video.update({"extension" : "null"})
        data.update({"best_audio" : audio})
        data.update({"best_audio_video" : video})
        return data