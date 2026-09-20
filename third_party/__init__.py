import os
import sys

third_party = os.path.dirname(os.path.abspath(__file__))

if third_party not in sys.path:
    sys.path.insert(0, third_party)