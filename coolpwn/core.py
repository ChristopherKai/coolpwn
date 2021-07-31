import os
from pwn import *

class PwnContext:
    def __init__(self, process, elf):
        self.elf = elf
        self.p = process
        self.breaks = {}
        self.gdbScript = ""

    def debug(self,func):
        rebase = ''
        if self.elf.pie:
            rebase = "$rebase"
        addr = self.breaks[func.__name__]
        self.gdbScript += """
            b *{rebase}({addr})\n
        """.format(addr=addr,rebase=rebase)
        gdb.attach(self.p, self.gdbScript)

    def addDebug(self,addr=None):
        def debugDecorator(func):
            if not self.breaks: self.breaks = {}
            self.breaks[func.__name__] = addr
            return func
        return debugDecorator
    
    def disableAlarm(self):
        self.gdbScript += "skip function alarm\n" 
    
    def nopAlarm(self):
        os.system('sed -i s/alarm/isnan/g ./' + p.argv[0])