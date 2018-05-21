import tornado.httpserver
import tornado.ioloop
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define,options
define("port",default=7000,help="run on th e given port",type=int)


class AgeHandler(tornado.web.RequestHandler):
    def get(self):
        age=int(self.get_argument("age","15"))
        print(age)


        self.write(calc_age(age))




def calc_age(age):
    for st in range(0,70,10):
        if  st<age and age<(st+10):
            return str(st)+"s"


    return "80s"








if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers=[(r"/",AgeHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()