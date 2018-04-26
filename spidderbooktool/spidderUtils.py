
import requests
import urllib.parse
import json
from concurrent.futures import ThreadPoolExecutor


from spidderbooktool import sqlliteconnect, writebookchapterUtils


# 获取章节内容
def  getBookcontent(bookid,bookchapter,url):
    urlstart= "http://chapter2.zhuishushenqi.com/chapter/"
    urlencode= urllib.parse.quote(url)
    urlall=urlstart+urlencode+"?k=2124b73d72e1945&t=1524537244"
    print("获取章节内容的地址："+urlall)
    r = requests.get(urlall)

    # with open(bookid+bookchapter+'_bookcontent'+'.json', 'w') as f:
    #     json.dump(r.text, f)

    return r.text

# 获取章节内容
def link(contenturl):
    r = requests.get(contenturl)
    return r.text


# 获取书本目录
def getbookCatalog(bookid):
    r=requests.get("http://api.zhuishushenqi.com/mix-toc/"+bookid)

    # with open(bookid+'_bookCatalog'+'.json', 'w') as f:
    #     json.dump(r.text, f)
    return r.text

# 获取书本详情
def getbookDetail(bookid):
    url="http://api.zhuishushenqi.com/book/"+bookid
    r=requests.get(url)
    # print("书本封面："+coverurl)
    # with open(bookid+'_bookdetail'+'.json', 'w') as f:
    #     json.dump(r.text, f)

    # with open(bookid+'_bookdetail'+'.json', 'r') as f:
    #     data = json.load(f)
    #
    # jsonobj=json.loads(data)
    # print("_id="+jsonobj['_id'])
    return r.text

def  saveBookfromResouRank(book):
    bookname = book['title']
    print("书名：" + bookname)
    # return

    # bookdetail---start
    bookid=book['_id'];
    bookdetailstr =getbookDetail(bookid)
    # print("书本详情：\n"+)

    bookdetailobj = json.loads(bookdetailstr)

    bookcoverurl = urllib.parse.unquote(bookdetailobj['cover']).replace("/agent/", "")
    print("\n\n书本封面:\n" + bookcoverurl)

    bookauthor = bookdetailobj['author'];
    print("\n\n书本作者:\n" + bookauthor)

    bookintro = bookdetailobj['longIntro'];
    print("\n\n书本介绍:\n" + bookintro)

    booktpye = bookdetailobj['majorCate'];
    print("\n\n书本类型:\n" + booktpye)

    bookcatalogstr=getbookCatalog(book['_id']);
    # print("\n\n书本目录：\n" + )
    bookcatalogobj=json.loads(bookcatalogstr);
    # print("\n\n書本第一章標題：\n" + json.loads(getbookCatalog(book['_id']))['mixToc']['chapters'][0]['title'])
    bookchaptersobj=bookcatalogobj['mixToc']['chapters']
    print("\n\n书本章节列表:\n" + booktpye)
    sqlliteconnect.addbookinfo(bookid, bookname, bookcoverurl, bookauthor, bookintro, booktpye)
    executor = ThreadPoolExecutor(10)

    i=0;
    for chapter in bookchaptersobj:
        i=i+1
        id = str(i);
        print("\n第:"+id+"章章节名：\n" + chapter['title'])
        print("\n第:" + id + "章章节内容url：\n" + chapter['link'])
        chapterbooklink =  chapter['link']
        chaptertitle = chapter['title']

        try:
         content=json.loads(getBookcontent(book['_id'], chaptertitle, chapterbooklink))['chapter']['body']
        except:
         print("出现异常,用链接里面的地址")
         if("api.easou.com" in chapterbooklink):
          content=json.loads(link(chapterbooklink))['content']
         else:
          content=""



        # print("\n\n書本第+"+id+"+章內容：\n" + content)
        executor.submit(sqlliteconnect.addchapters, bookid, i, chaptertitle, chapterbooklink, writebookchapterUtils.writebook(bookid, id, content))
        # mysqlconnect.addchapters(bookid,i,chaptertitle,chapterbooklink,writebookchapterUtils.writebook(bookid,id,content))

        print("\n\n書本第+"+id+"+章內容写入成功")






