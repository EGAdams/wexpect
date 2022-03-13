#
# class TypescriptInstaller
#
import os, sys, wexpect
from DirectoryManager import DirectoryManager

class TypescriptInstaller:
    def __init__( self, child_arg ):
        print ( "constructing TypescriptInstaller object..." )
        self.child = child_arg

    def install_typescript( self ):
        self.child.sendline( "npm install typescript --save" )
        print( "waiting for vulnerabilities text..." )
        self.child.expect( "vulnerabilities" )
        print( "got it." )
        self.child.sendline( "tsc --init" )
        print( "waiting for Success..." )
        self.child.expect( "Successfully" )
        print( "Successfully created a tsconfig.json file." )
        print( "done typescript initialization." )

    def test_me( self ):
        dm = DirectoryManager( self.child ) 
        dm.create_new_directory()
        dm.change_directory( "test" )
        self.install_typescript()
        print(" *** PASSED *** " )
        # os.rmdir( dm.base_path + dm.new_directory_name )
        # print( dm.new_directory_name + " directory removed." )

if len( sys.argv ) > 1:
    data_manager_arguments = sys.argv
    if data_manager_arguments and data_manager_arguments[ 1 ] == 'test':
        print( "testing..." )
        cmd_child = wexpect.spawn('cmd.exe')
        typescript_installer = TypescriptInstaller( cmd_child )
        typescript_installer.test_me()    