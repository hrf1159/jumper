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
	args = sys.argv
	if len(args) == 1:
		print('Too less arguments!')
		return
	elif len(args) > 2:
		print('Too many arguments!')
		return

	init_env()

	if args[1].startswith('--'):
		learn(args[1][2:])
		return
	else:
		do_conn(args)
		return


def learn(ask_msg):
	if ask_msg == 'conf':
		print(json.dumps(ENV_LIST, sort_keys=True, indent=4, separators=(',', ': ')))
	elif ask_msg == 'env':
		print(json.dumps(ENV_LIST, sort_keys=True, indent=4, separators=(',', ': ')))
	else:
		print('%s is not define, please check your input!' % ask_msg)


def do_conn(args):
	env = args[1]
	user = ''
	ip = ''
	port = ''
	password = ''

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

	index = child.expect(["(?i)yes/no", "(?i)password:", pexpect.EOF, pexpect.TIMEOUT])
	if (index == 0):
		child.sendline('yes')
		child.expect(["(?i)password", pexpect.EOF, pexpect.TIMEOUT])
		time.sleep(0.1)
		child.sendline(password)
		child.interact()
	elif (index == 1):
		time.sleep(0.1)
		child.sendline(password)
		child.interact()
	else:
		print("error")


def init_env():
	try:
		global ENV_LIST
		with open(os.path.join(sys.path[0], 'env.json'), 'r') as env_json:
			ENV_LIST = json.loads(env_json.read())
	except Exception as e:
		print('load env.json error, please check your file')


if __name__ == '__main__':
	main()