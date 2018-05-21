import tornado.httpserver
import tornado.ioloop
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define,options
define("port",default=8000,help="run on th e given port",type=int)


def calculator(num1,num2,mode):

    if mode=="addition":
        return num1+num2
    elif mode=="substraction":
        return num1-num2
    elif mode=="multiplication":
        return num1*num2
    else:
        return num1/num2

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        '''

        :return:
        '''
        self.render("index.html")





class ResultHandler(tornado.web.RequestHandler):
    def post(self):
        num1=int(float(self.get_argument("num1")))
        num2=int(float(self.get_argument("num2")))
        mode=self.get_argument("mode")
        print(num1)

        print(mode)
        output=calculator(num1,num2,mode)
        print(output)
        self.render("result.html",num1=num1,num2=num2,mode=mode,output=output)











if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers=[(r"/0",IndexHandler),(r"/5",ResultHandler)]
                                ,template_path=os.path.join(os.path.dirname(__file__),"templates"))
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()