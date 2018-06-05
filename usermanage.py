import tornado.web
from dbmysql import Mysql
import time

class UserAdd(tornado.web.RequestHandler):
    print("====")
    def get(self):
        self.render("manage_admin_add.html")

    def post(self):
        orgname = self.get_argument("orgname")
        username = self.get_argument("username")
        passwd = self.get_argument("passwd")
        handle = Mysql("sass")
        sqlstr = "INSERT INTO user_info (orgname,username,password,identity,createtime,updatetime) VALUES ('%s','%s','%s',1,%d,%d)"%(orgname,username,passwd,time.time(),time.time())
        handle.insert(sqlstr)

class UserManage(tornado.web.RequestHandler):
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
