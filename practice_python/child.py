import sys, subprocess
from pexpect import popen_spawn, spawn
import pexpect

# cmd = "echo 'Type yes or no: '"
# child = spawn('ls -l')
# child.expect('Type yes or no: ')
# print(child.)
# child.sendline('yes')

cmd = 'gitPushAll.py'.split()
subprocess.Popen(cmd)
