import chipwhisperer as cw
import Pyro5.server

@Pyro5.server.expose
class CWServer:
    def __init__(self):
        self.initialized = False

    def init(self,filename = None):
        """
        Inizializza la chipwhisperer e richiede la posizione di un file per creare un progetto
        """

        if(self.initialized):
            print("Chipwhisperer already initialized")
            return
            

        print("Initializing Chipwhisperer")

        if not filename:
            filename = "tmp_project.cwp"

        self.scope = cw.scope()
        self.proj = proj = cw.create_project(filename)
        self.initialized = True


    def start_trace(self):
        if not self.initialized:
            print("Chipwhisperer not yet initialized")
            return

        print("Acquiring trace")
        self.scope.arm()
        self.scope.trace()

    def stop_trace(self,plaintext,cyphertext):
        """
        Send data to save the acquired trace.

        The server waits for 2 string:
            - The plaintext
            - The cyphertext
        """
        if not self.initialized:
            print("Chipwhisperer not yet initialized")
            return
            
        print("Stopping trace")
        wave = self.scope.get_last_trace().wave

        trace = cw.Trace(wave,plaintext,cyphertext,None)
        self.proj.traces.append(trace)



