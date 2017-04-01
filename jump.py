#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' ssh with password '
__author__ = 'ruofei'

import os
import pwd
import sys
import json
import time
import pexpect

DEFAULT_PORT = '22'
DEFAULT_USER = pwd.getpwuid(os.getuid())[0]
ENV_LIST = []


def main():
	init_env()

	env = ''
	user = ''
	ip = ''
	port = ''
	password = ''

	args = sys.argv
	if len(args) == 1:
		print('Too less arguments!')
		return
	elif len(args) == 2:
		env = args[1]
	else:
		print('Too many arguments!')
		return

	for env_item in ENV_LIST:
		if env_item and env_item.get('env') and env == env_item.get('env'):
			user = DEFAULT_USER if not env_item.get('username') else env_item.get('username')
			ip = env_item.get('ip')
			port = DEFAULT_PORT if not env_item.get('port') else env_item.get('port')
			password = env_item.get('password')

	if not ip:
		print('can\'t find your env, please check your input')
		return

	child = pexpect.spawn('ssh -p%s %s@%s' % (port, user, ip))
	child.expect('password:')
	time.sleep(0.1)
	child.sendline(password)

	child.interact()


def init_env():
	try:
		global ENV_LIST
		with open(os.path.join(sys.path[0], 'env.json'), 'r') as env_json:
			ENV_LIST = json.loads(env_json.read())

	except Exception as e:
		print('load env.json error, please check your file')

if __name__ == '__main__':
	main()