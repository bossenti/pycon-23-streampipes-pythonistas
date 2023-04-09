from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import logging

"""
    This script provides the Modbus device
    Implementation is based on 
    https://pymodbus.readthedocs.io/en/latest/source/example/synchronous_server.html
"""

# configure the logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server(ip_address, num_fields, port=5002):
    """
    Initiates a modbus server (device)
    :param ip_address: ip address under which the Modbus device should be accessible
    :param port: port to which the server listens
    :param num_fields: length of the registers
    :return: None
    """

    # configure the device and initialize the registers
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*num_fields),
        co=ModbusSequentialDataBlock(0, [0]*num_fields),
        hr=ModbusSequentialDataBlock(0, [0]*num_fields),
        ir=ModbusSequentialDataBlock(0, [0]*num_fields))

    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Modbus Replica'
    identity.ProductCode = 'MS'
    identity.ProductName = 'Streampipes Modbus Simulator'
    identity.ModelName = 'Modbus Device'
    identity.MajorMinorRevision = '2.3.0'

    StartTcpServer(context, identity=identity, address=(ip_address, port))


if __name__ == "__main__":
    run_server("localhost", num_fields=10000, port=5002)
