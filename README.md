# Flask-Server-API
=============

 ## INTRODUCTION ##
  __So what does the code do ?__
  This is a flask server with two post endpoints :
  * POST : /news
   * This endpoint requires a json file with format similar to :
    ```javascript
     {
	    "search" : "Google Developers"
     }
    ```
    where `search` contains the value of the search item.
    The end point returns Google news articles for the `search` element.
    Sample response : 
    ```javascript
     {
        "articles": [
            {
                "author": "VentureBeat",
                "class1": "App developers in Uganda use TensorFlow to spot armyworm damage in maize",
                "class2": "A team of app developers in Uganda developed an app with Google's TensorFlow machine learning framework that spots signs of maize damage.",
                "desc": "App developers in Uganda use TensorFlow to spot armyworm damage in maize . A team of app developers in Uganda developed an app with Google's TensorFlow machine learning framework that spots signs of maize damage.",
                "image": "https://lh3.googleusercontent.com/dssGWYlOdyqhd_w4PljMjvk3KxkPIZxrbA8zSkS0fFGoaYLZGc6-3wPZ_msExtEQojylGh_tkQlUV3ztEA=-w200-h200-p",
                "publishedAt": ">16 hours ago",
                "title": "App developers in Uganda use TensorFlow to spot armyworm damage in maize",
                "url": "\"https://news.google.com/articles/CAIiECdAOdwbfgPAoQMTSj9if3oqFQgEKgwIACoFCAowsGkw8AYw7eb1BQ?hl=en-IN&amp;gl=IN&amp;ceid=IN%3Aen\""
            },....
        ],
        "makeReq": null,
        "reqError": null,
        "source": "https://news.google.com/search?q=Google%20Developers"
     }
    ```
  * POST : /youtube
   * This endpoint requires a json file with format similar to :
    ```javascript
     {
	    "search" : "Ed Sheeran Songs",
        "items" : 2
     }
    ```
    where `search` contains the value of the search item.
    The end point returns YouTube links and their audio/video data for the `search` element.
    Sample response : 
    ```javascript
     {
        "data": {
            "https://www.youtube.com/watch?v=UDDMYw_IZnE": {
                "author": "DopeLyrics",
                "best_audio": {
                    "bitrate": "160k",
                    "extension": "webm",
                    "size": "4398 bytes",
                    "url": "https://r15---sn-ci5gup-qxad.googlevideo.com/videoplayback?expire=1573763901&ei=3WbNXZr-MIGI3LUPj_iR6A8&ip=2401%3A4900%3A30e2%3A167a%3Ab064%3Aedb2%3Ad825%3Aa5c1&id=o-AF6V9WzB2w5p9GaKoSXIJCZATlVKSCT78-PF0JH5TstT&itag=251&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-ci5gup-qxad%2Csn-cvh76nez&ms=au%2Conr&mv=m&mvi=14&pl=46&initcwndbps=131250&mime=audio%2Fwebm&gir=yes&clen=4504564&dur=268.861&lmt=1569657333023932&mt=1573742219&fvip=3&keepalive=yes&fexp=23842630&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhAO1cvJ2yEK55G5fpFKjoF5aZ1TAtO33x9Vs2ZUQA5rQyAiEAnMsvfpsklPdvY_98OPjxxRPpiOBXg-8GImxphxC7MOY%3D&sig=ALgxI2wwRQIhAIzfRDLwo2k4CnOx2VUQHfZ_aCGhawvCpJ-q0KmyrT2PAiBWcj9549zTWbu6_jxpKLKqomdv5_-PiynUCljxpV1ogQ==&ratebypass=yes"
                },
                "best_audio_video": {
                    "bitrate": "96k",
                    "extension": "mp4",
                    "size": "10210 bytes",
                    "url": "https://r15---sn-ci5gup-qxad.googlevideo.com/videoplayback?expire=1573763901&ei=3WbNXZr-MIGI3LUPj_iR6A8&ip=2401%3A4900%3A30e2%3A167a%3Ab064%3Aedb2%3Ad825%3Aa5c1&id=o-AF6V9WzB2w5p9GaKoSXIJCZATlVKSCT78-PF0JH5TstT&itag=18&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-ci5gup-qxad%2Csn-cvh76nez&ms=au%2Conr&mv=m&mvi=14&pl=46&initcwndbps=131250&mime=video%2Fmp4&gir=yes&clen=10455650&ratebypass=yes&dur=268.887&lmt=1569657298361660&mt=1573742219&fvip=3&fexp=23842630&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhAO1cvJ2yEK55G5fpFKjoF5aZ1TAtO33x9Vs2ZUQA5rQyAiEAnMsvfpsklPdvY_98OPjxxRPpiOBXg-8GImxphxC7MOY%3D&sig=ALgxI2wwRQIgGjjGvbQxKjDw6DjVNXPKEJ7apcxxo-ZLoAJjh94AAB0CIQDkMPeCRT3H10SYNxWKjjI0OjiRISNwrCGTyWokrHAI6A=="
                },
                "category": "Music",
                "description": "Learn how to sing in only 30 days with these easy, fun video lessons! https://www.30daysinger.com/a/8328/BFzaEvmu\n-- \nPerfect - Ed Sheeran (Lyrics)\n▶️Check out Josh Michaels song ‘Dreams Come True’ on Spotify.  It is gaining lots of popularity!  Save & add it to your playlists!\nhttps://open.spotify.com/track/0CK4soIqiYiNbuN0G5WYhD?si=ojxLoFCxSuiM2xLkS2uWFA\n--\nI do not own anything. All credits go to the right owners. No copyright intended. \n--\n🎧: https://ad.gt/yt-perfect\n💰: https://atlanti.cr/yt-album\nSubscribe to Ed's channel: http://bit.ly/SubscribeToEdSheeran\n\nFollow Ed on...\nFacebook: http://www.facebook.com/EdSheeranMusic\nTwitter: http://twitter.com/edsheeran\nInstagram: http://instagram.com/teddysphotos\nOfficial Website: http://edsheeran.com\n--\nCopyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for \"fair use\" for purposes such as criticism, comment, news reporting, teaching, scholarship, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, educational or personal use tips the balance in favor of fair use.",
                "dislikes": 177325,
                "length": 269,
                "likes": 2836977,
                "published": "2017-11-29 11:53:13",
                "rating": 4.7646885,
                "title": "Perfect - Ed Sheeran (Lyrics)",
                "viewcount": 758013550
            },....
        },
        "items": 2,
        "search": "Ed Sheeran Songs"
     }
    ```
 

 ## INSTALLING ##
  * DEPENDENCIES
   Install The dependencies using pip through : `pip install -r requirements.txt` command.

  * RUNNING
   Simply execute the script by `python main.py` on your system or deploy it on a server based on your requirements

 ## DEVELOPER ##
  Hey this is [GrayHat](https://grayhat12.github.io/ "Developer Site") . Yes i developed it.
  Article.py , GrayAPI.py and youtube.py were written by me.
  These are scraping scripts and might be illegal for commercial use.
  This script is only supposed to be used for educational purposes.

 ## SUPPORT ##
  Your support keeps me going. Feel free to [Donate](https://www.instamojo.com/@grayhat/ "Instamojo") and show your support by following me on
  [Website](https://grayhat12.github.io/old/index.html "GrayHat")
  [Twitter](https://twitter.com/gray_rahul "@gray_rahul")
  [Instagram](https://www.instagram.com/gray_._hat/ "@gray_._hat")
  [LinkedIn](https://www.linkedin.com/in/grayhat "@grayhat")
  [Github](https://github.com/GrayHat12 "@grayhat12")
  [Facebook](https://www.facebook.com/grayhathacks/ "@grayhathacks")