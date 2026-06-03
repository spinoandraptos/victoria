from pathlib import Path

from qcore import Server

if __name__ == "__main__":
    """
    Initialize a Server with a yml config file specifying Instruments to be served remotely. This initialization is a blocking call which serves the Instruments on a remote stage until the stage is torn down.
    """

    instruments_config = Path(__file__).resolve().parent / "config/instruments.yml"
    server = Server(instruments_config)
    server.serve()
