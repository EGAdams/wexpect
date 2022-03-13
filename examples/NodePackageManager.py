#
# class NodePackageManager
#
import os
import sys
from DirectoryManager import DirectoryManager
import wexpect

class NodePackageManager:
    def __init__( self, child_arg ):
        self.child = child_arg
        print ( "constructing NodePackageManager object..." )

    def npm_init( self ):
        print( "initializing npm..." )
        self.child.sendline( "npm init -y" )
        print( "waiting for prompt")
        self.child.expect( "ISC", timeout=5)
        print( "*** PASSED: got text ISC. ***" )

    def test_me( self ):
        dm = DirectoryManager( self.child ) 
        dm.create_new_directory()
        dm.change_directory( "test" )
        self.npm_init()
        print( "removing test directory..." )
        os.rmdir( dm.base_path + "test" )
        print( "done test." )

if len( sys.argv ) > 1:
    data_manager_arguments = sys.argv
    if data_manager_arguments and data_manager_arguments[ 1 ] == 'test':
        print( "testing..." )
        cmd_child = wexpect.spawn( 'cmd.exe' )
        manager = NodePackageManager( cmd_child )
        manager.test_me()
