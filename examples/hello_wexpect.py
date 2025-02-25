'''
This is the simplest example. It starts a windows command interpreter (aka. cmd) lists the current
directory and exits.
'''

import wexpect

# Start cmd as child process
child = wexpect.spawn('cmd.exe')

# Wait for prompt when cmd becomes ready.
child.expect('>')

# Prints the cmd's start message
print(child.before, end='')
print(child.after, end='')

# run list directory command
child.sendline('dir')

# Waiting for prompt
child.expect('>')

# run list directory command
child.sendline('dir')

# Waiting for prompt
child.expect('>')

# Prints content of the directory
print(child.before, end='')
print(child.after, end='')

# Exit from cmd
child.sendline('exit')

# Waiting for cmd termination.
child.wait()
