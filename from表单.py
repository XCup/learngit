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
                        <form action="" method="post">\
                                <input type="text" placeholder="commit -m" name="commit">\
                                <input type="submit">\
                                <input type="button" value="pull" onclick=msg()>\
                        </form>\
                    </body>\
                    </html>'
                   )
    def post(self, *args, **kwargs):
        message=self.get_argument('commit')
        self.write("finish")

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

        def add():
            archiveCmd = 'git add --all'
            process = subprocess.Popen(archiveCmd, shell=True)
            process.wait()
            archiveReturnCode = process.returncode
            if archiveReturnCode != 0:
                print("添加到缓存区错误")
            else:
                commit()

        # 提交本地版本库
        def commit():
            inputNote = message.encode('utf-8')
            archiveCmd = "git commit -m inputNote "
            process = subprocess.Popen(archiveCmd, shell=True)
            process.wait()
            archiveReturnCode = process.returncode
            if archiveReturnCode != 0:
                print("提交失败")
            else:
                print("提交成功"), inputNote
                pull()

        # 拉取
        def pull():
            archiveCmd = 'git pull'
            process = subprocess.Popen(archiveCmd, shell=True)
            process.wait()
            archiveReturnCode = process.returncode
            if archiveReturnCode != 0:
                print("拉取远程代码失败")
            else:
                push()

        # 推送
        def push():
            archiveCmd = 'git push'
            process = subprocess.Popen(archiveCmd, shell=True)
            process.wait()
            archiveReturnCode = process.returncode
            if archiveReturnCode != 0:
                print("上传远程git服务器失败")
            else:
                print("上传成功")

        # 执行一哈
        def main():
            status()

        if __name__ == '__main__':
            main()
if __name__ == '__main__':
    app=tornado.web.Application([
        ('/',indexHandler)
    ]
    )
    app.listen(8889)
    tornado.ioloop.IOLoop.instance().start()