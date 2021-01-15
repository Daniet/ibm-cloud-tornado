import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define('port', default=8080, help='run on the given port', type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Whatsaaaaaa !.!')


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r'/', MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
