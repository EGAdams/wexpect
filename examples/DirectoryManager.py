#
# class DirectoryManager
#
from Console import Console
import os, sys, wexpect

class DirectoryManager:
    def __init__( self, child_arg ):
        print ( "constructing DirectoryManager object..." )
        self.child = child_arg
        self.cmd_console = Console( child_arg )
        self.base_path = "C:\\Users\\EG\Desktop\\"
        self.new_directory_name = "test"

    def input_new_directory_name( self ):
        print( "enter new directory name: " )
        self.new_directory_name = ( input())

    def create_new_directory( self ):
        the_new_directory = self.base_path + self.new_directory_name
        mkdir_command = 'mkdir ' + the_new_directory

        print( "sending mkdir " + the_new_directory )
        self.child.sendline( mkdir_command )
        self.cmd_console.wait_for_prompt( ">" )
        if not self.test_directory_existence( the_new_directory ):
            print( "*** ERROR: failed to create direcory: " + the_new_directory )
    
    def change_directory( self, change_to_directory ):
        print( "changing directory to: " + change_to_directory )
        self.child.sendline( "cd " + change_to_directory )
        self.cmd_console.wait_for_prompt( ">" )

    def test_directory_existence( self, directory_to_test ):
        if os.path.isdir( directory_to_test ):
            print( "directory: " + directory_to_test  + " exists." )
            return True
        else:          
            return False

    def test_me( self ):
        self.create_new_directory()
        os.rmdir( self.base_path + self.new_directory_name )
        print( self.new_directory_name + " directory removed." )

if len( sys.argv ) > 1:
    data_manager_arguments = sys.argv
    if data_manager_arguments and data_manager_arguments[ 1 ] == 'test':
        print( "testing..." )
        cmd_child = wexpect.spawn('cmd.exe')
        directory_manager = DirectoryManager( cmd_child )
        directory_manager.test_me()
