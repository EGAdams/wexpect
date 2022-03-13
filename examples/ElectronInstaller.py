#
# class ElectronInstaller
#
import os, sys, wexpect
from DirectoryManager import DirectoryManager

class ElectronInstaller:
    def __init__( self, child_arg ):
        print ( "constructing ElectronInstaller object..." )
        self.child = child_arg

    def install_electron( self ):
        self.child.sendline( "npm install electron" )
        print( "waiting for vulnerabilities text..." )
        self.child.expect( "vulnerabilities" )
        print( "got it." )

    def test_me( self ):
        dm = DirectoryManager( self.child ) 
        dm.create_new_directory()
        dm.change_directory( "test" )
        self.install_electron()
        print(" *** PASSED *** " )
        os.rmdir( dm.base_path + dm.new_directory_name )
        print( dm.new_directory_name + " directory removed." )

if len( sys.argv ) > 1:
    data_manager_arguments = sys.argv
    if data_manager_arguments and data_manager_arguments[ 1 ] == 'test':
        print( "testing..." )
        cmd_child = wexpect.spawn('cmd.exe')
        electron_installer = ElectronInstaller( cmd_child )
        electron_installer.test_me()    