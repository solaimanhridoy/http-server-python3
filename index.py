import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Querying tweet with id " + id)

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n%2 else "even"

        self.write("The number " + str(n) + " is " + r)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/blog", staticRequestHandler),
        (r"/isEven", queryStringRequestHandler),
        (r"/tweet/([0-9]+)", resourceRequestHandler)
    ])

    app.listen(8080)
    print("I'm listening on port localhost:8080")
    tornado.ioloop.IOLoop.current().start()
