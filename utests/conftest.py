import os
import sys


path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if path not in sys.path:
    sys.path.append(path)
