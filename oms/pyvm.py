import argparse
import sys
import atexit
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
from pyVim.connect import Disconnect, SmartConnect
sys.dont_write_bytecode = True

service_instance = connect.SmartConnect(host="192.168.10.179",user="root",pwd="Fuck2014!~", port=int(443))
print   service_instance