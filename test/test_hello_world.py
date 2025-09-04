# import os
import sys
# import pytest
#from ASL.utils.cusip import Cusip

module_directory = r"."
# # module_directory = r".."
print(f"module directory {module_directory}")
sys.path.insert(0, module_directory)

from hello_world import hello_worldx
# import hello_world

sys.path.remove(module_directory)

class TestHelloWorld:
    def test_hello_world(self):
       val = hello_worldx()
       assert("Hello World" in val)
           