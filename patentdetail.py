import tornado.web
import time

class PatentDetailHandler(tornado.web.RequestHandler):
    def get(self, aid):
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
        self.render("patent_detail_page.html", info=data)

    def post(self):
        pass
