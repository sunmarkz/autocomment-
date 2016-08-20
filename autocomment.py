# -*- coding:utf-8 -*-
import urllib2,cookielib,re,urllib
cjar= cookielib.LWPCookieJar()
cookie =urllib2.HTTPCookieProcessor(cjar)
opener= urllib2.build_opener(cookie)



def code(url):
    url = unicode(url, "gb2312").encode("utf8")
    print url

def gethash(ID):
    page = opener.open('http://www.fangdede.com/member.php?mod=logging&action=login').read()
    pageid= r'<em id="returnmessage_(.*?)"'

    if ID == 0 :
            return re.findall(pageid,page)[0]
    if ID ==1:
            pageid = r'<input type="hidden" name="formhash" value="(.*?)"/>'
            return re.findall(pageid, page)[0]



def login():

    url = 'http://www.fangdede.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash='+gethash(0)+'&inajax=1'
    Data = 'formhash='+gethash(1)+'&referer=http%3A%2F%2Fwww.fangdede.com%2F&loginfield=username&username=1011642499&password=d79ac2392145ba85a2890c1834f18558&questionid=0&answer=&loginsubmit=true'
    req = urllib2.Request(url, data=Data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    html = opener.open(req).read()
    code(html)

def post():

    url =opener.open('http://www.fangdede.com/forum.php?mod=post&action=reply&fid=44&extra=page%3D1&tid=76&reppost=254').read()
    reg= r'<input type="hidden" name="formhash" value="(.*?)"/>'
    formhash = re.findall(reg, url)[0]

    reg= r'<input type="hidden" name="posttime" id="posttime" value="(.*?)"/>'
    posttime = re.findall(reg, url)[0]

    reg=r'<input type="hidden" name="reppid" value="(.*?)"/>'
    reppid = re.findall(reg, url)[0]

    reg=r'<input type="hidden" name="reppost" value="(.*?)"/>'
    repost = re.findall(reg, url)[0]

    reg=r'<input type="hidden" name="wysiwyg" id="e_mode" value="(.*?)"/>'
    wysiwyg = re.findall(reg, url)[0]

    reg = r'<input type="hidden" name="noticeauthormsg" value="(.*?)"/>'
    noticeauthormsg = re.findall(reg, url)[0]

    reg=r'<input type="hidden" name="noticeauthor" value="(.*?)"/>'
    noticeauthor = re.findall(reg,url)[0]
    #noticeauthor=noticeauthor.replace('+','%2B')

    print formhash,posttime,wysiwyg,reppid,repost,noticeauthor

    Requesturl= 'http://www.fangdede.com/forum.php?mod=post&action=reply&fid=44&tid=76&extra=page%3D1&replysubmit=yes'
    Requestdata= 'formhash'+'='+formhash+'&'+ 'posttime'+'='+posttime+'&'+ 'wysiwyg'+'='+wysiwyg+'&'+ 'noticeauthor'+'='+noticeauthor+'&'+'noticetrimstr'+'='+'&'+'noticeauthormsg'+'='+noticeauthormsg+'&'+  'reppid'+'='+reppid+'&'+ 'reppost'+'='+repost+'&'+ 'subject'+'='+'&'+  'message'+'='+'55555555555555555555555555555555555%0D%0A'+'&'+ 'save'+'='+'&'+  'connect_publish_t'+'=0'
    #Requestdata=urllib.urlencode(Requestdata)
    print Requestdata
    req = urllib2.Request(Requesturl, data=Requesturl)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    code(opener.open(req).read())

   # html=opener.open(Requesturl,data=Requesturl).read()



login()
post()
