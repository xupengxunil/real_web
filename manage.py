#/usr/bin/env python
#coding: uTF-8
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from saltui import app, db

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("server",Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Post=Post,Tag=Tag,Comment=Comment)


if __name__ == '__main__':
    manager.run()