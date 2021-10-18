import chipwhisperer as cw


class CWServer:
    def __init__(self,com_channel):
        self.initialized = False
        self.com = com_channel

    def init(self):
        """
        Inizializza la chipwhisperer e richiede la posizione di un file per creare un progetto
        """

        if(self.initialized):
            self.com.send_data("Chipwhisperer already initialized")
            return

        self.com.send_data("Initializing Chipwhisperer")
        fname = self.com.receive_data().strip()

        if not fname:
            fname = "tmp_project.cwp"

        self.initialized = True
        self.scope = cw.scope()
        try:
            self.proj = cw.create_project(fname)
        except OSError:
            self.proj = cw.open_project(fname)

    def start_trace(self):
        if not self.initialized:
            self.com.send_data("Chipwhisperer not yet initialized")
            return

        self.com.send_data("Acquiring trace")
        self.scope.arm()
        self.scope.capture()

    def quit(self):
        self.proj.close()
        self.scope.dis()

    def stop_trace(self):
        """
        Send data to save the acquired trace.

        The server waits for 2 string:
            - The plaintext
            - The cyphertext
        """
        if not self.initialized:
            self.com.send_data("Chipwhisperer not yet initialized")
            return
            
        self.com.send_data("Stopping trace")
        wave = self.scope.get_last_trace()

        plaintext = self.com.receive_data(decode = False)
        cyphertext = self.com.receive_data(decode = False)

        trace = cw.Trace(wave,plaintext,cyphertext,None)
        self.proj.traces.append(trace)



