import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
#from mainhandler import MainHandler
#from indexhandler import IndexHandler
from wxshedule import WxShedule
from sasshandler import SassHandler
from menuhandler import MenuHandler
from bindhandler import BindHandler
from loginhandler import LoginHandler
from loginhandler import AdminLoginHandler
from loginhandler import OrgLoginHandler 
from loginhandler import StaffLoginHandler
from patentinfo import PatentHandler
from patentdetail import PatentDetailHandler
from usermanage import UserManage
from usermanage import UserAdd
from orgmanage import PatentInfo
#from wxframehandler import WxFrameHandler
import config


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            login_url="/login",
            debug=True,
        )
        #super(Application, self).__init__(urlpatterns, **settings)
        #super(Application, self).__init__([(r'/wx', MainHandler),(r'/', IndexHandler),(r'/frame', WxFrameHandler)], **settings)
        #super(Application, self).__init__([(r'/wx', MainHandler),(r'/', IndexHandler),(r'/sass',SassHandler),], **settings)
        #super(Application, self).__init__([(r'/', IndexHandler),(r'/sass',SassHandler), (r'/menu', MenuHandler)], **settings)
        super(Application, self).__init__([(r'/sass',SassHandler), (r'/menu', MenuHandler),(r'/bind', BindHandler),(r'/login', LoginHandler),(r'/admin',AdminLoginHandler),(r'/org',OrgLoginHandler),(r'/staff',StaffLoginHandler),(r'/usermanage', UserManage),(r'/useradd', UserAdd),(r"/patent/(?P<page>\d*)",PatentInfo),(r"/patentinfo/(?P<pid>\d*)",PatentDetailHandler)], **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(80)
    #
    #wx_shedule = WxShedule()
    #wx_shedule.excute()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

