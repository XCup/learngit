# -*- coding: utf-8 -*-
import tornado
import tornado.web
import subprocess
import tornado.ioloop
class indexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<!DOCTYPE html>\
                    <html lang="en">\
                    <head>\
                        <meta charset="UTF-8">\
                        <title>form</title>\
                    </head>\
                    <body>\
                        <form action="index" method="post">\
                            <input type="submit">\
                        </form>\
                    </body>\
                    </html>'
                   )
    def post(self, *args, **kwargs):
        self.write("ing")

        def status():
            archiveCmd = 'git status'
            process = subprocess.Popen(archiveCmd, shell=True)
            process.wait()
            archiveReturnCode = process.returncode
            if archiveReturnCode != 0:
                print("查看工作区状态错误")
            else:
                add()

            return True
if __name__ == '__main__':
    app=tornado.web.Application([
        ('/index',indexHandler)
    ]
    )
    app.listen(8889)
    tornado.ioloop.IOLoop.instance().start()