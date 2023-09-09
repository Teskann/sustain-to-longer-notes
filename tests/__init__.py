import sys
from os.path import dirname, abspath, join, normpath

sys.path.append(normpath(join(dirname(abspath(__file__)), "..")))
sys.path.append(normpath(join(dirname(abspath(__file__)))))

from create_test_data import *
clear_test_data()
create_test_data()