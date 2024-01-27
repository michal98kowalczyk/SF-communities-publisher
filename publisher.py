import yaml
import os
import subprocess
import shlex
import time


ORG_CONFIG_DIR_PATH = 'config/org.yml'
COMMANDS_FILE_PATH = 'config/commands.yml'
AUTH_FILES_DIR = 'authFiles/'
LOGIN_WEB = 'loginWeb'
COMMAND_PARAM = 'cmd'
SAVE_COMMAND = 'saveAuth'
LOGIN_URL = 'loginUrl'
LOGOUT_PARAM = 'logout'
SITES = 'sites'
PUBLISH_COMMAND = 'publish'

class Publisher:
    def __init__(self, org):
        self.org = org
        self.readCommands()
        self.readConfig()

    def login(self):
        if os.path.exists('{dir}auth-{org}.json'.format(dir=AUTH_FILES_DIR,org=self.org)):
            self.loginUrl()
        else:
            self.loginWeb() 
               
    def loginWeb(self):
        print('\n Now you will be redirected to your browser, please login using standard credentials\n')
        loginWebCommand = self.commands[LOGIN_WEB][COMMAND_PARAM].format(org=self.org)
        self.runCommand(loginWebCommand)
        self.saveAuth()
        self.loginUrl()

    def loginUrl(self):
        loginUrlCommand = self.commands[LOGIN_URL][COMMAND_PARAM].format(file=self.org,org=self.org)
        self.runCommand(loginUrlCommand)


    def logout(self):
        logoutCommand = self.commands[LOGOUT_PARAM][COMMAND_PARAM].format(org=self.org)
        self.runCommand(logoutCommand)

    def saveAuth(self):
        saveCommand = self.commands[SAVE_COMMAND][COMMAND_PARAM].format(org=self.org,file=self.org)
        self.runCommand(saveCommand)


    def publish(self):
        self.login()

        for site in self.config[SITES]:
            print('\nPublishing {site}...'.format(site=site))
            publishCommand = self.commands[PUBLISH_COMMAND][COMMAND_PARAM].format(site=site, org=self.org)
            self.runCommand(publishCommand)

        self.logout()

    def runCommand(self, command):
        print('Executing: ',command)
        os.system(command)
        print()
        time.sleep(1)         
       

    def readCommands(self):
        with open(COMMANDS_FILE_PATH, 'r') as file:
            self.commands = yaml.safe_load(file)

    def readConfig(self):
        with open(ORG_CONFIG_DIR_PATH, 'r') as file:
            self.config = yaml.safe_load(file)[self.org]
