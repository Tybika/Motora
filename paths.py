import sys
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.abspath(os.path.join(ROOT, 'controller')))
sys.path.append(os.path.abspath(os.path.join(ROOT, 'view')))
sys.path.append(os.path.abspath(os.path.join(ROOT, 'model')))
sys.path.append(os.path.abspath(os.path.join(ROOT, 'model', 
                                 'chain_of_responsability')))