from pwn import *

# interactions
process.s       = lambda self,data               :self.send(str(data))        #in case that data is an int
process.sa      = lambda self,delim,data         :self.sendafter(str(delim), str(data)) 
process.sl      = lambda self,data               :self.sendline(str(data)) 
process.sla     = lambda self,delim,data         :self.sendlineafter(str(delim), str(data)) 
process.r       = lambda self,numb=4096          :self.recv(numb)
process.ru      = lambda self,delims, drop=True  :self.recvuntil(delims, drop)
process.irt     = lambda self                    :self.interactive()
process.rl      = lambda self                    :self.recvline()

remote.s       = lambda self,data               :self.send(str(data))        #in case that data is an int
remote.sa      = lambda self,delim,data         :self.sendafter(str(delim), str(data)) 
remote.sl      = lambda self,data               :self.sendline(str(data)) 
remote.sla     = lambda self,delim,data         :self.sendlineafter(str(delim), str(data)) 
remote.r       = lambda self,numb=4096          :self.recv(numb)
remote.ru      = lambda self,delims, drop=True  :self.recvuntil(delims, drop)
remote.irt     = lambda self                    :self.interactive()
remote.rl      = lambda self                    :self.recvline()
# misc functions
uu32    = lambda data      :u32(data.ljust(4, '\0'))
uu64    = lambda data      :u64(data.ljust(8, '\0'))
leak    = lambda name,addr :log.success('{} = {:#x}'.format(name, addr))