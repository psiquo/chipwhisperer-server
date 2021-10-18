
import src.chipwhisperer_server as soc
import sys

def main(servName):
    if servName:
        soc.start_pyro_server(servName)
    else:
        soc.start_pyro_server()

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv >= 2) else None)
