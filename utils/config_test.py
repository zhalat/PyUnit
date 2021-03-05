import os
import sys

PRJ = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir, os.pardir))
SCRIPTS_PATH = os.path.join(PRJ, 'scripts')
sys.path.insert(0, SCRIPTS_PATH)
