#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from fabric.api import *
#自动化部署脚本

#fab -f deploy3.py m:12    :后面跟参数
#env.user="dev"
#env.hosts=['192.168.2.11','192.168.2.102','172.17.0.10']
#env.port=22

kfPath="/data/public/war/testonline"
warName="yyxk-web-childhealth-0.0.1-SNAPSHOT.war"
localPath="/Users/xiaofengche/IdeaProjects/yyxk-web-front/yyxk-web-childhealth"
install="mvn -Dmaven.test.skip=true install"
killChild="ps -ef |grep childhealth | grep -v grep |awk '{print $2}' |xargs kill -9"
projectPath="/usr/local/project/childhealth/childhealth"
unzip="unzip -o *.war"


#服务器分组
env.roledefs ={
    'cs':['dev@192.168.2.102:22'],
    'tc':['dev@172.17.0.10:22'],
    'kf':['dev@192.168.2.11:22'],
    'xg':['root@47.90.127.54']
}

#入口函数
def m(name):
    #用这个命令执行操作 excute
    execute(name)

@roles('xg')
def geta():
    with cd("/opt"):
        get("KindleForMac-47032.dmg")

@runs_once
def package():
    #进入某个文件夹下工作
    with lcd(localPath):
        local(install)
    print ">>>>>打包完成<<<<<<<"

@roles('tc')
def tc():
    with lcd(localPath+"/target"):
    #进入远程服务器进行工作
        put(warName, remote_path=projectPath)
    with cd(projectPath):
        run(unzip)

    run(killChild)
    # set -m 独立进程运行
    run("set -m;sh /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/bin/startup.sh")
    run("tail -f /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/logs/catalina.out")

@roles('tc')
def tctf():
    run("tail -f /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/logs/catalina.out")


@roles('tc')
def cstf():
    run("tail -f /usr/local/Tomcat/WeChat/tomcat_wechat_childhealth/logs/catalina.out")

@roles('cs')
def cs():
    #进入远程服务器进行工作
    with lcd(localPath+"/target"):
        put(warName, remote_path=projectPath)
    with cd(projectPath):
        run(unzip)
    run(killChild)
    # set -m 独立进程运行
    run("set -m;sh /usr/local/Tomcat/WeChat/tomcat_wechat_childhealth/bin/startup.sh")
    run("tail -f /usr/local/Tomcat/WeChat/tomcat_wechat_childhealth/logs/catalina.out")

@roles('kf')
def kf():
    with lcd(localPath+"/target"):
        put(warName, remote_path= kfPath,use_sudo=True)
    print ">>>>>>>上传至开发服务器中"


@roles('cs')
def sz():
    with lcd(localPath+"/target"):
        get(remote_path="/usr/local/project/socket/socketfast/socketfast/yyxk-socket-fast-0.0.1-SNAPSHOT.war")


def xiaxian():
    with cd(""):
        f=open("nginx.conf","r+")
        line = f.readlines()
        f.seek(0, 0)
        for l in line:
            p = l.replace("中文", "英文")
            f.write(p)
            print p
        f.close()
        run("nginx -s reload")
        print "服务器下线成功"

def shangxian():
    print "服务器上线成功"


