#
# class Console
#
class Console:
    def __init__( self, spawned_child_arg ):
        self.spawned_child = spawned_child_arg
        print ( "constructing console..." )


    def wait_for_prompt( self, prompt_to_wait_for ):
        print( "waiting for prompt..." )
        
        # Waiting for prompt
        self.spawned_child.expect( prompt_to_wait_for )
        print( "got prompt." )
