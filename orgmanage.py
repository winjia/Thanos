import tornado.web
from dbmysql import Mysql
import time

class UserAdd(tornado.web.RequestHandler):
    def get(self):
        self.render("manage_admin_add.html")

    def post(self):
        orgname = self.get_argument("orgname")
        username = self.get_argument("username")
        passwd = self.get_argument("passwd")
        handle = Mysql("sass")
        sqlstr = "INSERT INTO user_info (orgname,username,password,identity,createtime,updatetime) VALUES ('%s','%s','%s',1,%d,%d)"%(orgname,username,passwd,time.time(),time.time())
        handle.insert(sqlstr)

class OrgManage(tornado.web.RequestHandler):
    def get(self):
        handle = Mysql("sass")
        sqlstr = "SELECT orgname,username FROM user_info WHERE identity=1 and isdelete=0"
        res = handle.query(sqlstr)
        print(res)
        data = []
        for i,elem in enumerate(res):
            data.append({"idx":i, "orgname":elem[0], "username":elem[1]})
        self.render("manage_admin.html", userdata=data)

    def post(self):
        orgname = self.get_argument("orgname")
        username = self.get_argument("username")
        passwd = self.get_argument("passwd")
        handle = Mysql("sass")
        sqlstr = "INSERT INTO user_info (orgname,username,password,identity,createtime,updatetime) VALUES ('%s','%s','%s',1,%d,%d)"%(orgname,username,passwd,time.time(),time.time())
        handle.insert(sqlstr)
        self.redirect("/usermanage")


#---Patent---
class Page:
    def __init__(self, total, pageid):
        self.pagenum = 5
        self.num = 10
        self.total = total
        pages,more  = divmod(self.total, self.num)
        if more > 0:
            pages += 1
        self.pages = pages
        try:
            currid = int(pageid)
        except Exception as e:
            currid = 1
        if currid < 1:
            currid = 1
        self.currid = currid

    def get_page_range(self):
        s = (self.currid-1)*self.num 
        e = self.currid*self.num
        return s,e

    def get_url(self, baseurl):
        elemlist = []
        elemlist.append('<nav aria-label="Page navigation"><ul class="pagination"><li>')
        if self.pages <= self.pagenum:
            elemlist.append('<a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
            for i in range(self.pages):
                tmp = '<li><a href="/%s/%s">%s</a></li>'%(baseurl,str(i),str(i+1))
                elemlist.append(tmp)
            elemlist.append('<li><a href="#" aria-label="Next">')
        #---

        elemlist.append('<span aria-hidden="true">&raquo;</span></a></li></ul></nav>')
        return "".join(elemlist) 
        



class PatentInfo(tornado.web.RequestHandler):
    def get(self, page):
        patent = []
        for i in range(40):
            data = {}
            data["no"] = str(i+1)
            data["name"] = "自组织服务提供方为无线网络提供服务的能力"
            data["url"] = "http://118.24.63.203/patentinfo/2008801027517"
            patent.append(data)
        pagehandle = Page(len(patent), page)
        s,e = pagehandle.get_page_range()
        pageurl = pagehandle.get_url("patent")
        self.render("manage_org_patent.html", info=patent[s:e], pageurl=pageurl)

    def post(self):
        pass

class PatentDetail(tornado.web.RequestHandler):
    def get(self, pid):
        if pid != "2008801027517":
            self.write("afsafafaf")
            return
        data = {}
        data["no"] = "2008801027517"
        data["name"] = "自组织服务提供方为无线网络提供服务的能力"
        data["applytime"] = "12/08/2008"
        data["agent"] = "永新专利商标代理有限公司"
        data["status"] = "xx"
        data["case"] = "xx"
        data["date"] = "2018-08-12"
        data["fee"] = "1000"
        data["feecase"] = "afafafaff"
        patent = []
        patent.append(data)
        self.render("patent_detail_page.html", info=patent)

    def post(self):
        pass
