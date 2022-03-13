#
# class ProjectFactory
#
from DirectoryManager import DirectoryManager
from NodePackageManager import NodePackageManager
from ElectronInstaller import ElectronInstaller
from TypescriptInstaller import TypescriptInstaller

class ProjectFactory:
    def __init__( self, child_arg ):
        print ( "constructing ProjectFactory object..." )
        self.child = child_arg
        self.node_package_manager = NodePackageManager( child_arg )

    def build_project( self ):
        print( "starting new project creation..." )
        directory_manager = DirectoryManager( self.child )
        directory_manager.input_new_directory_name()
        directory_manager.create_new_directory()
        directory_manager.change_directory( directory_manager.base_path + directory_manager.new_directory_name )
        self.node_package_manager.npm_init()
        electron_installer = ElectronInstaller( self.child )
        electron_installer.install_electron()
        typescript_installer = TypescriptInstaller( self.child )
        typescript_installer.install_typescript()
