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
    'kf':['dev@192.168.2.11:22']
}

#入口函数
def m(name):
    #用这个命令执行操作 excute
    execute(name)

@runs_once
def package():
    #进入某个文件夹下工作
    with lcd(localPath):
        local(install)
    print ">>>>>打包完成<<<<<<<"

@roles('tc')
def tc():
    #进入远程服务器进行工作
    with cd(projectPath):
        run(unzip)
    run(killChild)
    # set -m 独立进程运行
    run("set -m;sh /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/bin/startup.sh")
    run("tail -f /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/logs/catalina.out")

@roles('cs')
def cs():
    #进入远程服务器进行工作
    with cd(projectPath):
        run(unzip)
    run(killChild)
    # set -m 独立进程运行
    run("set -m;sh /usr/local/Tomcat/WeChat/tomcat_wechat_childhealth/bin/startup.sh")
    run("tail -f /usr/local/Tomcat/WeChat/tomcat_wechat_childhealth/logs/catalina.out")

@roles('kf')
def kf():
    with lcd(localPath+"/target"):
        put(warName, remote_path= kfPath)
    print ">>>>>>>上传至开发服务器中"

@roles('cs')
def sz():
    with lcd(localPath+"/target"):
        get(remote_path="/usr/local/project/socket/socketfast/socketfast/yyxk-socket-fast-0.0.1-SNAPSHOT.war")


