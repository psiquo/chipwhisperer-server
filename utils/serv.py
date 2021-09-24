#import chipwhisperer as cw

class CWServer:
    def __init__(self):
        self.initialized = False

    def init(self):
        if(not self.initialized):
            print("Initializing Chipwhisperer")
            self.initialized = True
            #self.scope = cw.scope()
        else:
            print("Chipwhisperer already initialized")

    def start_trace(self):
        print("Acquiring trace")

    def stop_trace(self):
        print("Stopping trace")