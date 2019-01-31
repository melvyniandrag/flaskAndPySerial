from pathlib import Path
from app import app
import time
import serial

if __name__ == "__main__":
    app.debug = True
    app.run()
