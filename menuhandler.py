import tornado.web
import random
import json

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class MenuHandler(tornado.web.RequestHandler):
    def __create_menu_key(self):
        global seed
        return "V1001_"+"".join(random.sample(seed,5))

    def __get_button_type(self, btntuple):
        if btntuple[1] == "0":
            return "click", self.__create_menu_key()
        elif btntuple[1] == "1":
            return "view", btntuple[2]
        return None, None

    def get_button_info(self, btnlist):
        if len(btnlist) == 0:
            return None
        if len(btnlist[0][0]) == 0:
            return None
        #one menu
        button = {}
        if btnlist[1][0]=="":
            button["name"] = btnlist[0][0]
            button["type"],button["key"] = self.__get_button_type(btnlist[0])
            return button
        #more than one menu
        button["name"] = btnlist[0][0]
        n = len(btnlist)
        subbtn = []
        for i in range(1,n,1):
            if len(btnlist[i][0]) == 0:
                continue
            btn = {}
            btn["name"] = btnlist[i][0]
            btn["type"],btn["key"] = self.__get_button_type(btnlist[i])
            subbtn.append(btn)
        button["sub_button"] = subbtn
        return button

    def get(self):
        self.render("menu_page.html")

    def post(self):
        appid = self.get_argument("appid")
        appsecret = self.get_argument("appsecret")
        if appid=="" or appsecret=="":
            self.write("appid or appsecret is null!")
            return
        button1 = []
        menu1name = self.get_argument("menu1")
        menu1type = self.get_argument("menu1_type")
        menu1value = self.get_argument("menu1_")
        menu11name = self.get_argument("menu11")
        menu11type = self.get_argument("menu11_type")
        menu11value = self.get_argument("menu11_")
        menu12name = self.get_argument("menu12")
        menu12type = self.get_argument("menu12_type")
        menu12value = self.get_argument("menu12_")
        menu13name = self.get_argument("menu13")
        menu13type = self.get_argument("menu13_type")
        menu13value = self.get_argument("menu13_")
        button1.append((menu1name,menu1type,menu1value))
        button1.append((menu11name,menu11type,menu11value))
        button1.append((menu12name,menu12type,menu12value))
        button1.append((menu13name,menu13type,menu13value))
        print(button1)
        btn1 = self.get_button_info(button1)
        print(btn1)
        
        #
        button2 = []
        menu2name = self.get_argument("menu2")
        menu2type = self.get_argument("menu2_type")
        menu21name = self.get_argument("menu21")
        menu21type = self.get_argument("menu21_type")
        menu22name = self.get_argument("menu22")
        menu22type = self.get_argument("menu22_type")
        menu23name = self.get_argument("menu23")
        menu23type = self.get_argument("menu23_type")
        menu2value = self.get_argument("menu2_")
        menu21value = self.get_argument("menu21_")
        menu22value = self.get_argument("menu22_")
        menu23value = self.get_argument("menu23_")
        button2.append((menu2name,menu2type,menu2value))
        button2.append((menu21name,menu21type,menu21value))
        button2.append((menu22name,menu22type,menu22value))
        button2.append((menu23name,menu23type,menu23value))
        btn2 = self.get_button_info(button2)
        print(btn2)
        #
        button3 = []
        menu3name = self.get_argument("menu3")
        menu3type = self.get_argument("menu3_type")
        menu31name = self.get_argument("menu31")
        menu31type = self.get_argument("menu31_type")
        menu32name = self.get_argument("menu32")
        menu32type = self.get_argument("menu32_type")
        menu33name = self.get_argument("menu33")
        menu33type = self.get_argument("menu33_type")
        menu3value = self.get_argument("menu3_")
        menu31value = self.get_argument("menu31_")
        menu32value = self.get_argument("menu32_")
        menu33value = self.get_argument("menu33_")
        button3.append((menu3name,menu3type,menu3value))
        button3.append((menu31name,menu31type,menu31value))
        button3.append((menu32name,menu32type,menu32value))
        button3.append((menu33name,menu33type,menu33value))
        btn3 = self.get_button_info(button3)
        print(btn3)
        btnlist = []
        if btn1 is not None:
            btnlist.append(btn1)
        if btn2 is not None:
            btnlist.append(btn2)
        if btn3 is not None:
            btnlist.append(btn3)
        menu = {"button":btnlist}
        print(json.dumps(menu))
    
        



