import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    app.listen(8080)
    print("I'm listening on port localhost:8080")
    tornado.ioloop.IOLoop.current().start()
