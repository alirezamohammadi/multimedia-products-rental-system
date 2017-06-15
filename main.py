import tornado.web
import tornado.ioloop
import os
import sqlite3

import random
import string

def generateRandomString(length):
    s=string.ascii_lowercase+string.digits+string.ascii_uppercase
    return str(''.join(random.sample(s,length)))


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.write(str(self.get_secure_cookie("user")))
    


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        query='SELECT * FROM "user" WHERE "username"=? AND "password"=?;'
        cur=self.application.db.execute(query,[username,password])
        result=cur.fetchone()
        if not result:
            self.write("نام کاربری یا کلمه عبور اشتباه است")
        else:
            self.set_secure_cookie("user","result[2]")
            self.write("ورود موفقیت آمیز")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user")

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register_customer.html")

if __name__=="__main__":
    settings={
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "login_url": "/login",
        "cookie_secret": generateRandomString(50),
    }

    app=tornado.web.Application([
        (r"/", MainHandler),
        (r"/register", RegisterHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
    ],**settings)
    app.db=sqlite3.connect("site.db")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()