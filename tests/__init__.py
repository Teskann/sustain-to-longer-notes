import sys
from os.path import dirname, abspath, join, normpath
from tests.create_test_data import create_test_data, clear_test_data

sys.path.append(normpath(join(dirname(abspath(__file__)), "..")))
sys.path.append(normpath(dirname(abspath(__file__))))

clear_test_data()
create_test_data()
