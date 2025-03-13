import logging
import logging.config
from app.commands import CalculatorREPL

# Set up logging from the configuration file
logging.config.fileConfig('logging.conf')

if __name__ == "__main__":
    print("Starting the calculator...")  # Debugging print
    print("Running the interactive REPL...")  # Debugging print
    CalculatorREPL().cmdloop()
