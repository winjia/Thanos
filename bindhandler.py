import tornado.web
import time
from dbmysql import Mysql


class BindHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("bind_page.html")

    
    def post(self):
        name = self.get_argument("compname")
        phone = self.get_argument("phonenum")
        if len(name)==0:
            self.write("error")
        if len(phone)==0:
            self.write("error")
        handle = Mysql("sass")
        sqlstr = "INSERT INTO wechat_bind_info (wechatid,companyname,cellphone,createtime,updatetime) VALUES ('aaaaa','%s','%s',%d,%d)"%(name,phone,time.time(),time.time())
        handle.insert(sqlstr)
