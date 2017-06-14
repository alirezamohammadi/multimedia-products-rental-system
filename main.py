import tornado.web
import tornado.ioloop
import os
import sqlite3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",title="Sahar Nafisi")
    def post(self):
        fname=self.get_argument("fname")
        lname=self.get_argument("lname")
        file1 = open("names.txt",'w')
        file1.write(fname+' '+lname+'\n')
        file1.close()

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("add_customer.html")

if __name__=="__main__":
    settings={
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    }

    app=tornado.web.Application([
        (r"/", MainHandler),
        (r"/register", RegisterHandler),
    ],**settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()