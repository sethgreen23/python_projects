#!/usr/bin/env python3

try:
    import sys
    import gnureadline
    sys.modules["readline"] = gnureadline
except ImportError:
    pass

import cmd

class Illustrate(cmd.Cmd):
    """Illustrate the base class method use"""
    
    def cmd_loop(self, intro=None):
        print('Inside cmd_loop: cmdloop({})'.format(intro))
        return cmd.Cmd.cmdloop(self, intro)
    
    def preloop(self):
        print('Inside preloop: preloop()')
        
    def postloop(self):
        print("Inside postloop: postloop()")
        
    def parseline(self, line):
        print("Inside parseline 1",line)
        print('Inside parseline 2: parseline({!r}) =>'.format(line), end='')
        ret = cmd.Cmd.parseline(self, line)
        print("Inside parseline 3:", ret)
        return ret
    
    def onecmd(self, s):
        print('Inside onecmd: onecmd({})'.format(s))
        return cmd.Cmd.onecmd(self, s)
    
    def emptyline(self):
        print("emptyline()")
        return cmd.Cmd.emptyline(self)
    
    def defaul(self, line):
        print('default({})'.format(line))
        return cmd.Cmd.default(self, line)
    
    def precmd(self, line):
        print('precmd({})'.format(line))
        return cmd.Cmd.precmd(self, line)
    
    def postcmd(self, stop, line):
        print("postcmd({}, {})".format(stop, line))
        return cmd.Cmd.postcmd(self, stop, line)
    
    def do_greet(self, line):
        print('hello', line)
    
    def do_EOF(self, line):
        "Exit"
        return True

if __name__=='__main__':
    Illustrate().cmd_loop('Illustrate the methods of cmd.Cmd')
