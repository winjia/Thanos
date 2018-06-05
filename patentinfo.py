import tornado.web
import time

class Page:
    def __init__(self, itemlist, pageid):
        self.total = len(itemlist)
        pages,more  = divmod(self.total, 5)
        if more>0:
            pages += 1
        self.allpages = pages
        try:
            currpageid = int(pageid)
        except Exception as e:
            currpageid = 1
        if currpageid < 1:
            currpageid = 1
        self.currpageid = currpageid

    def get_page_url(self, baseurl):
        urllist = []
        for i in range(self.allpages):
            tmp = "<a href='/%s/%s'>%s</a>"%(baseurl,str(i),str(i+1))
            urllist.append(tmp)
        return "".join(urllist)

    def get_start_end(self):
        s = (self.currpageid-1)*5
        e = self.currpageid*5
        return s,e


class PatentHandler(tornado.web.RequestHandler):
    def get(self, page):
        record = []
        for i in range(100):
            record.append({"no":i, "title":str(i)+"_afadff"})
        pagehandle = Page(record, page)
        pageurl = pagehandle.get_page_url("patent")
        s,e = pagehandle.get_start_end()
        self.render("patent_page.html", item_list=record[s:e], pageurl=pageurl)
        
    def post(self):
        pass


