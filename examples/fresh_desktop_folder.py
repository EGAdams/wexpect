'''
'''
from ProjectFactory import ProjectFactory
import wexpect
wexpect.TIMEOUT

# Start cmd as child process
child = wexpect.spawn('cmd.exe')
project_factory = ProjectFactory( child )
project_factory.build_project()
