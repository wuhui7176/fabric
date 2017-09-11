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
        local('/Library/Java/JavaVirtualMachines/jdk1.8.0_144.jdk/Contents/Home/bin/java -Dmaven.multiModuleProjectDirectory=/Users/xiaofengche/IdeaProjects/yyxk-web-front/yyxk-web-childhealth "-Dmaven.home=/Applications/IntelliJ IDEA.app/Contents/plugins/maven/lib/maven3" "-Dclassworlds.conf=/Applications/IntelliJ IDEA.app/Contents/plugins/maven/lib/maven3/bin/m2.conf" "-javaagent:/Applications/IntelliJ IDEA.app/Contents/lib/idea_rt.jar=54242:/Applications/IntelliJ IDEA.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath "/Applications/IntelliJ IDEA.app/Contents/plugins/maven/lib/maven3/boot/plexus-classworlds-2.5.2.jar" org.codehaus.classworlds.Launcher -Didea.version=2017.2.2 install')
    with lcd("/Users/xiaofengche/IdeaProjects/yyxk-web-front/yyxk-web-childhealth/target"):
        local("scp yyxk-web-childhealth-0.0.1-SNAPSHOT.war dev@172.17.0.10:/usr/local/project/childhealth/childhealth")
    local("ls -a")

