#!/usr/bin/env python3

from sys import stdout

import requests
import paramiko
import re
import json

API_ENDPOINT = {
    'login': '/login',
    'chall': '/api/v1/challenges',
    'challid': '/api/v1/challenges/{}',
    'solve': '/api/v1/challenges/{}/solves',
    'scoreboard': '/api/v1/scoreboard',
    'teams': '/api/v1/teams',
    'users': '/api/v1/users',
    'me': '/api/v1/users/me'
}

finalist = {
    53: (1,'%zqIH@#eo#1YT6pCjQwyQCiO0'),
    54: (2,'BigBrainGurls'),
    55: (3,'Brahmastra'),
    56: (4,'No Rush & Relax'),
    57: (5,'NoBrainBois'),
    58: (6,'Panitia'),
    59: (7,'Rahasia'),
    60: (8,'SHOCKER'),
    61: (9,'Sopan Kh Begitu??'),
    62: (10,'Terlantarkan'),
    63: (11,'Walkie O Talkie'),
    64: (12,'ctf terakhir pas smk'),
    65: (13,'gatao aja lah'),
    66: (14,'jeopardized'),
    67: (15,'tim wangy wangy')
}


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas + '\n')
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)


stdout = Unbuffered(stdout)


class Auth(object):
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

        self.create_session()

    def create_session(self):
        self.ses = requests.session()

        try:
            self.login()
        except:
            stdout.writelines('\n[x] Incorrect username/password')
            exit()

    def get_csrf_token(self, target_url):
        response = self.ses.get(target_url)
        regex = re.compile(r'csrfNonce.*"([a-f0-9]*)"')

        nonce = regex.findall(response.text)[0]

        return nonce

    def login(self):
        target_url = self.url + API_ENDPOINT.get('login')
        csrf_token = self.get_csrf_token(target_url)
    
        auth_data = {
            'name': self.username,
            'password': self.password,
            'nonce': csrf_token
        }

        post_response = self.ses.post(target_url, data=auth_data)

        assert('incorrect' not in post_response.text)

    def get_user_team(self):
        target_url = self.url + API_ENDPOINT.get('me')
        response = self.ses.get(target_url).json()

        try:
            json_data = response.get('data')
            team_id = json_data['team_id']
            host, team_name = finalist[int(team_id)]
        except:
            stdout.writelines("\n[x] You're not registered as finalist")
            exit()
        else:
            return f'server_snapshot_{host}', team_name

class Prompt(object):
    def __init__(self, username, password, host, port, team=''):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.team = team

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def start(self):
        try:
            self.connect()
            stdout.writelines(f'[+] Logged in as {self.team}\n')
        except Exception as e:
            exit(str(e))

        while True:
            try:
                stdout.write('$ ')
                command = input()
                response = self.recv(command)

                for r in response:
                    if r:
                        stdout.write(r.read().decode())
            
            except KeyboardInterrupt:
                exit()

    def recv(self, command):
        return self.ssh.exec_command(command)[1:]


if __name__ == '__main__':
    CTFd_url = 'https://ctf.joints.id'

    stdout.write('CTFd username: ')
    username = input()
    stdout.write('CTFd password: ')
    password = input()

    s = Auth(username, password, CTFd_url)
    host, team_name = s.get_user_team()

    p = Prompt('user', 'joints21ulala', host, 2222, team_name)
    p.start()
