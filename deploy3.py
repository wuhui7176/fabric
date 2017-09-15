#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from fabric.api import *
from datetime import datetime


env.user="dev"
env.hosts=['172.17.0.10']
env.port=22


def dp():
    package()
    remote()

def remote():
    #进入远程服务器进行工作
    with cd("/usr/local/project/childhealth/childhealth"):
        run("unzip -o *.war")
    run("ps -ef |grep childhealth | grep -v grep |awk '{print $2}' |xargs kill -9")
    # set -m 独立进程运行
    run("set -m;sh /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/bin/startup.sh")
    run("tail -f /usr/local/Tomcat/wechat/tomcat_wechat_childhealth/logs/catalina.out")


def package():
    #进入某个文件夹下工作
    with lcd("/Users/xiaofengche/IdeaProjects/yyxk-web-front/yyxk-web-childhealth"):
        local("mvn -Dmaven.test.skip=true install")
    with lcd("/Users/xiaofengche/IdeaProjects/yyxk-web-front/yyxk-web-childhealth/target"):
        put("yyxk-web-childhealth-0.0.1-SNAPSHOT.war",remote_path="/usr/local/project/childhealth/childhealth")
    local("ls -a")

