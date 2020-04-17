import pafy
import urllib
import gzip
import requests
import json


class YouTube:

    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.prev = []
        self.outlnk = 'https://www.youtube.com/'
        self.idn0 = 'https://i.ytimg.com/vi/'
        self.lnks = set()
        self.idn = 'watch?v='

    def NewMain(self, query, prevList=[]):
        self.prev = prevList
        requests.utils.default_headers().update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11'
            }
        )
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn0)):
                self.data = self.data[self.data.index(
                    self.idn0)+len(self.idn0):]
                outLnk = 'https://www.youtube.com/watch?v='+self.data[:11]
                if outLnk not in self.prev:
                    self.lnks.add(outLnk)
        except ValueError as ve:
            return True

    def main(self, query, prevList=[]):
        self.prev = prevList
        requests.utils.default_headers().update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11'
            }
        )
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:11+len(self.idn)]
                if (self.outlnk+tmp) not in self.prev:
                    self.lnks.add(self.outlnk+tmp)
                self.data = self.data[12:]
                # print(self.lnks)
        except ValueError as ve:
            return True

    def getLinks(self):
        return self.lnks


class Search:
    req_url = 'https://www.youtube.com/results'
    headers = {
        'Accept-Encoding': 'gzip',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20200207.03.01'
    }
    def __init__(self,search='Nightcore Songs'):
        params = {
            'search_query' : search,
            'pbj' : '1'
        }
        self.req = requests.get(url=self.req_url,params=params,headers=self.headers)
        self.data = {'data' : json.loads(self.req.text.encode('utf-8'))}
        self.vidData = dict()
        #print(self.req.headers)
    
    def compute(self,i=0):
        dat=self.data['data'][1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']
        dat=dat['contents']
        if i>=len(dat):
            return
        dat=dat[i]
        dat=dat['itemSectionRenderer']
        dat=dat['contents']
        for items in dat:
            for k,v in items.items():
                if k in self.vidData.keys():
                    put=self.vidData.get(k)
                    put.append(v)
                    self.vidData.update({k : put})
                else:
                    put = []
                    put.append(v)
                    self.vidData.update({k : put})
        return self.compute(i+1)
    
    def prepare(self):
        fnalOut = dict()
        fnalOut.update({'data' : []})
        continuations = self.data['data'][1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]
        continuations = continuations['itemSectionRenderer']['continuations'][0]['nextContinuationData']
        fnalOut.update({'continuation' : continuations['continuation']})
        fnalOut.update({'clickTrackingParams' : continuations['clickTrackingParams']})
        sessionToken = self.data['data'][1]['xsrf_token']
        fnalOut.update({"sessionToken" : sessionToken})
        for key in self.vidData.keys():
            if key == 'videoRenderer':
                for item in self.vidData.get(key):
                    try:
                        thumb = ''
                        title = ''
                        access = ''
                        desc = ''
                        channel = ''
                        published = ''
                        length = ''
                        simplelength = ''
                        views = ''
                        viewsShort = ''
                        videoId = item['videoId']
                        try:
                            thumbs = item['thumbnail']['thumbnails']
                            thumb = thumbs[len(thumbs)-1]
                        except:
                            pass
                        try:
                            titles = item['title']['runs']
                            for tit in titles:
                                if len(title)==0:
                                    title+=tit['text']
                                else:
                                    title+=" "+tit['text']
                        except :
                            pass
                        try:
                            access = item['title']['accessibility']['accessibilityData']['label']
                        except:
                            pass
                        try:
                            channel = item['longBylineText']['runs'][0]['text']
                        except :
                            pass
                        try:
                            descriptions = item['descriptionSnippet']['runs']
                            for des in descriptions:
                                if len(desc)==0:
                                    desc+=des['text']
                                else:
                                    desc+=" "+des['text']
                        except:
                            pass
                        try:
                            published = item['publishedTimeText']['simpleText']
                        except:
                            pass
                        try:
                            length = item['lengthText']['accessibility']['accessibilityData']['label']
                        except:
                            pass
                        try:
                            simplelength = item['lengthText']['simpleText']
                        except:
                            pass
                        try:
                            views = item['viewCountText']['simpleText']
                        except:
                            pass
                        try:
                            viewsShort = item['shortViewCountText']['simpleText']
                        except:
                            pass
                        data = fnalOut.get('data')
                        item = dict()
                        item.update({
                            'videoId' : videoId,
                            'thumb' : thumb,
                            'title' : title,
                            'access' : access,
                            'author' : channel,
                            'desc' : desc,
                            'published' : published,
                            'length' : length,
                            'lengthShort' : simplelength,
                            'views' : views,
                            'viewShort' : viewsShort
                        })
                        data.append(item)
                        fnalOut.update({'data' : data})
                        """fnalOut.update({videoId : {
                            'videoId' : videoId,
                            'thumb' : thumb,
                            'title' : title,
                            'access' : access,
                            'author' : channel,
                            'desc' : desc,
                            'published' : published,
                            'length' : length,
                            'lengthShort' : simplelength,
                            'views' : views,
                            'viewShort' : viewsShort
                        }})"""
                    except:
                        pass
        return fnalOut
        
class SearchMore:
    req_url = 'https://www.youtube.com/results'
    headers = {
        'Accept-Encoding': 'gzip',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20200207.03.01'
    }
    def __init__(self,session='',token='',clickTrackingParams='',search=''):
        params = {
            'search_query' : search,
            'pbj' : '1',
            'ctoken' : token,
            'continuation' : token,
            'itct' : clickTrackingParams
        }
        data = {
            'session_token' : session
        }
        self.req = requests.post(url=self.req_url,params=params,headers=self.headers,data=data)
        self.data = {'data' : json.loads(self.req.text.encode('utf-8'))}
        self.vidData = dict()
    
    def compute(self,i=0):
        dat=self.data['data'][1]['response']['continuationContents']['itemSectionContinuation']
        dat=dat['contents']
        for items in dat:
            for k,v in items.items():
                if k in self.vidData.keys():
                    put=self.vidData.get(k)
                    put.append(v)
                    self.vidData.update({k : put})
                else:
                    put = []
                    put.append(v)
                    self.vidData.update({k : put})
    
    def prepare(self):
        fnalOut = dict()
        fnalOut.update({'data' : []})
        continuations = self.data['data'][1]['response']['continuationContents']['itemSectionContinuation']['continuations'][0]
        continuations = continuations['nextContinuationData']
        fnalOut.update({'continuation' : continuations['continuation']})
        fnalOut.update({'clickTrackingParams' : continuations['clickTrackingParams']})
        sessionToken = self.data['data'][1]['xsrf_token']
        fnalOut.update({"sessionToken" : sessionToken})
        for key in self.vidData.keys():
            if key == 'videoRenderer':
                for item in self.vidData.get(key):
                    try:
                        thumb = ''
                        title = ''
                        access = ''
                        desc = ''
                        channel = ''
                        published = ''
                        length = ''
                        simplelength = ''
                        views = ''
                        viewsShort = ''
                        videoId = item['videoId']
                        try:
                            thumbs = item['thumbnail']['thumbnails']
                            thumb = thumbs[len(thumbs)-1]
                        except :
                            pass
                        try:
                            titles = item['title']['runs']
                        except :
                            pass
                        try:
                            for tit in titles:
                                if len(title)==0:
                                    title+=tit['text']
                                else:
                                    title+=" "+tit['text']
                        except :
                            pass
                        try:
                            access = item['title']['accessibility']['accessibilityData']['label']
                        except :
                            pass
                        try:
                            channel = item['longBylineText']['runs'][0]['text']
                        except:
                            pass
                        try:
                            descriptions = item['descriptionSnippet']['runs']
                            for des in descriptions:
                                if len(desc)==0:
                                    desc+=des['text']
                                else:
                                    desc+=" "+des['text']
                        except:
                            pass
                        try:
                            published = item['publishedTimeText']['simpleText']
                        except:
                            pass
                        try:
                            length = item['lengthText']['accessibility']['accessibilityData']['label']
                        except :
                            pass
                        try:
                            simplelength = item['lengthText']['simpleText']
                        except:
                            pass
                        try:
                            views = item['viewCountText']['simpleText']
                        except:
                            pass
                        try:
                            viewsShort = item['shortViewCountText']['simpleText']
                        except:
                            pass
                        try:
                            data = fnalOut.get('data')
                            item = {
                                'videoId' : videoId,
                                'thumb' : thumb,
                                'title' : title,
                                'access' : access,
                                'author' : channel,
                                'desc' : desc,
                                'published' : published,
                                'length' : length,
                                'lengthShort' : simplelength,
                                'views' : views,
                                'viewShort' : viewsShort
                            }
                            data.append(item)
                            fnalOut.update({'data' : data})
                            #fnalOut.update({videoId : datttt})
                        except :
                            print("err 237 ytSM")
                    except:
                        pass
        return fnalOut
    
class GetSong:
    def __init__(self,idd):
        self.dat = pafy.new(idd,basic=False).getbestaudio().url
    
    def getSong(self):
        return self.dat

class Decoder:
    def __init__(self, link):
        self.link = link

    def getDat(self):
        dat = pafy.new(self.link)
        data = {}
        try:
            data.update({"title": dat.title})
        except:
            data.update({"title": "null"})
        try:
            data.update({"author": dat.author})
        except:
            data.update({"author": "null"})
        try:
            data.update({"category": dat.category})
        except:
            data.update({"category": "null"})
        try:
            data.update({"description": dat.description})
        except:
            data.update({"description": "null"})
        try:
            data.update({"thumb": dat.thumb})
        except:
            data.update(
                {"thumb": "https://cdn.shopify.com/s/files/1/2018/8867/files/play-button.png"})
        try:
            data.update({"likes": dat.likes})
        except:
            data.update({"likes": "null"})
        try:
            data.update({"dislikes": dat.dislikes})
        except:
            data.update({"dislikes": "null"})
        try:
            data.update({"length": dat.length})
        except:
            data.update({"length": "null"})
        try:
            data.update({"published": dat.published})
        except:
            data.update({"published": "null"})
        try:
            data.update({"rating": dat.rating})
        except:
            data.update({"rating": "null"})
        try:
            data.update({"viewcount": dat.viewcount})
        except:
            data.update({"viewcount": "null"})
        audio = {}
        try:
            audio.update({"url": dat.getbestaudio().url})
        except:
            audio.update({"url": "null"})
        try:
            audio.update({"bitrate": dat.getbestaudio().bitrate})
        except:
            audio.update({"bitrate": "null"})
        try:
            audio.update(
                {"size": str(int(dat.getbestaudio().get_filesize()/1024))+" bytes"})
        except:
            audio.update({"size": "null"})
        try:
            audio.update({"extension": dat.getbestaudio().extension})
        except:
            audio.update({"extension": "null"})
        video = {}
        try:
            video.update({"url": dat.getbest().url})
        except:
            video.update({"url": "null"})
        try:
            video.update({"bitrate": dat.getbest().bitrate})
        except:
            video.update({"bitrate": "null"})
        try:
            video.update(
                {"size": str(int(dat.getbest().get_filesize()/1024))+" bytes"})
        except:
            video.update({"size": "null"})
        try:
            video.update({"extension": dat.getbest().extension})
        except:
            video.update({"extension": "null"})
        data.update({"best_audio": audio})
        data.update({"best_audio_video": video})
        return data
