import sys
import os
import json
if sys.argv[1:]:
    file = sys.argv[1]
    os.system('taskkill /im sublime_text.exe')
    sublime_path = file + '/../../../sublime_text.exe'
    file += '/../../Local/Session.sublime_session'
    f = open(file)
    j = json.load(f)
    rworkspaces = j['workspaces']['recent_workspaces']
    for idx, i in enumerate(rworkspaces, 1):
        print(idx, i)
    v = input('Enter which projects to remove separated by spaces\n').split()
    for i in v[::-1]:
        del rworkspaces[int(i) - 1]
    j['workspaces']['recent_workspaces'] = rworkspaces
    f = open(file, 'w')
    f.write(json.dumps(j))
    os.system(f'start /B {sublime_path}')
    exit()

import sublime
import sublime_plugin


class RemoveWorkspace(sublime_plugin.TextCommand):
    def run(self, edit):
        a = (f'python {__file__} {os.path.dirname(__file__)}')
        os.system(f'start /B {a}')
