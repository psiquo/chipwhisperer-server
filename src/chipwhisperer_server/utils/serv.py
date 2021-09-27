#import chipwhisperer as cw


class CWServer:
    def __init__(self,com_channel):
        self.initialized = False
        self.com = com_channel

    def init(self):
        if(not self.initialized):
            self.com.send_data("Initializing Chipwhisperer")
            self.initialized = True
            #self.scope = cw.scope()
        else:
            self.com.send_data("Chipwhisperer already initialized")

    def start_trace(self):
        if not self.initialized:
            self.com.send_data("Chipwhisperer not yet initialized")
            return

        self.com.send_data("Acquiring trace")

    def stop_trace(self):
        if not self.initialized:
            self.com.send_data("Chipwhisperer not yet initialized")
            return
            
        self.com.send_data("Stopping trace")