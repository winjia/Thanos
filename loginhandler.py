import hashlib
import functools
import tornado.web
from dbmysql import Mysql


def judge_role(rolelist):
    def decorator(func):
        @functools.wraps(func)  
        def wrapper(self,*args,**kwargs):  
            user = self.current_user
            handle = Mysql("sass")
            user = tornado.escape.xhtml_escape(user)
            sqlstr = "SELECT * FROM user_info WHERE username='%s' and isdelete!=1"%(user)
            res = handle.query(sqlstr)
            if res is None:
                raise Exception("404")
            else:
                res = res[0]
                print("info",res)
                if res[3] in rolelist:
                    func(self,*args,**kwargs)
                else:
                    raise Exception("404")
        return wrapper  
    return decorator 


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")



class LoginHandler(BaseHandler):
    def get(self):
        print(self.current_user) 
        print("========")
        self.render("login.html")

    def post(self):
        username = self.get_argument("username")
        passwd = self.get_argument("password")
        usertype = self.get_argument("usertype")
        print(usertype)
        if username=="" or passwd=="":
            self.write("用户名或者密码为空")
            return
        md5passwd = hashlib.md5()
        #md5passwd.update(passwd)
        #passwd = md5passwd.hexdigest()
        handle = Mysql("sass")
        sqlstr = "SELECT * FROM user_info WHERE username='%s' and isdelete!=1"%(username)
        res = handle.query(sqlstr)
        res = res[0]
        print(res)
        print("-=-=-=-=")
        if res is None:
            self.redirect("/login")
        if res[3]==passwd:
            print("aa:",username)
            self.set_secure_cookie("username", username)
            if res[4] == 0:
                print("admin======")
                self.redirect("/usermanage")
            elif res[4] == 1:
                print("org======")
                self.redirect("/patent/0")
            elif res[4] == 2:
                print("staff======")
                self.redirect("/staff")
        else:
            self.write("login error")
            self.redirect("/login")


class AdminLoginHandler(BaseHandler):
    @tornado.web.authenticated
    @judge_role([0])
    def get(self):
        self.render("manage_admin.html")


class OrgLoginHandler(BaseHandler):
    @tornado.web.authenticated
    @judge_role([1])
    def get(self):
        self.render("manage_org_patent.html")

class StaffLoginHandler(BaseHandler):
    @tornado.web.authenticated
    @judge_role([2])
    def get(self):
        self.render("user_manage.html")

