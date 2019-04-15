#!/usr/bin/env python3
import os
from fabric.api import *
env.user = 'root'
# Will get the hostname of this worker:
def getHostname():
    name = run("hostname")
    print(name)

def setupWebServer():
	run("hostnamectl set-hostname www")
	run("yum install httpd -y")
	run("systemctl enable httpd")
	run("systemctl start httpd")
	with cd("/var/www/html/"):
		put("webcontents.tar.gz", ".")
		run("tar -xvf webcontents.tar.gz")

def setupFirewall():
	run("yum -y -d1 remove firewalld")
	run("yum -y -d1 install iptables-services")
	run("systemctl enable iptables")
	run("systemctl start iptables")
	with settings(warn_only=True):
		firewallAlreadySetUp = run("iptables -C INPUT -p tcp --dport 80 -j ACCEPT")
		if firewallAlreadySetUp.return_code == 1:
			run("iptables -I INPUT -p tcp --dport 80 -j ACCEPT")
			run("iptables-save > /etc/sysconfig/iptables")
