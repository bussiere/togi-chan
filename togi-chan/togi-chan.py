import urllib2,gadfly,re,time
try:
    while 1==1:
        time.sleep(60)
        try :
            moeboard = urllib2.urlopen('http://moeboard.net/list.php?table=moe')
            page = moeboard.read()
        except :
            page = ""
        listeDeLiens= re.findall('<img src="(.*?)"',page)
        for lien in listeDeLiens:
            baseDonn = gadfly.gadfly("urlimages","BD/")
            cur = baseDonn.cursor()
            lien = "http://moeboard.net/"+ lien
            nomimages = re.findall('/moe/(.*?)$|_memicon/(.*?)$',lien)
            result = None
            for nomimagep in nomimages:
                for nomimage in nomimagep:
                    if nomimage != "":
                        cur.execute("Select * from urlimages where url = '%s' "%nomimage)
                        result = cur.fetchall()
                        if result :
                            i = 0
                        else :
                            
                            if nomimage :
                                furl = urllib2.urlopen(lien)
                                f = file('IMG/'+nomimage,'wb')
                                f.write(furl.read())
                                f.close()
                                print lien
                                cur.execute("Insert Into urlimages(url) Values ('%s')"%nomimage)
                                baseDonn.commit()
        baseDonn.commit()
        baseDonn.close()
        try :
            danbooru = urllib2.urlopen('http://danbooru.donmai.us/post/list')
            page = danbooru.read()
        except :
            page = ""
        listepage= re.findall('href="/post/view/(.*?)"',page)
        for pages in listepage:
                baseDonn = gadfly.gadfly("urlimages","BD/")
                cur = baseDonn.cursor()
                lienpageimage = "http://danbooru.donmai.us/post/view/"+pages
                danbooruimage = urllib2.urlopen(lienpageimage)
                page = danbooruimage.read()
                image = re.findall('/data/(.*?)"',page)
                nomimages = image
                result = None
        
                for nomimage in nomimages:
                    if nomimage != "":
                        cur.execute("Select * from urlimages where url = '%s' "%nomimage)
                        result = cur.fetchall()
                        if result :
                            i = 0
                        else :
                            
                            if nomimage :
                                lien = "http://danbooru.chiisai.net/data/"+nomimage
                                nomimag = lien[39:]                 
                                furl = urllib2.urlopen(lien)
                                f = file('IMG/'+nomimag,'wb')
                                f.write(furl.read())
                                f.close()
                                print lien
                                cur.execute("Insert Into urlimages(url) Values ('%s')"%nomimage)
                                baseDonn.commit()
            
            
        baseDonn.commit()
        baseDonn.close()
except :
    raw_input("Erreur")