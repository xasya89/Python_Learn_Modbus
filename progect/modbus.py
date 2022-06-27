from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import encode_ieee, decode_ieee, \
                              long_list_to_word, word_list_to_long

class ModbusOwen:
    def __init__(self):
        self.__ipaddr="10.0.6.10"
        self.__port=503
        self.__c=ModbusClient(host=self.__ipaddr, port=self.__port, unit_id=1, auto_open=True)
    
    def getStatusProcess(self):
        return int(self.__c.read_input_registers(0)[0])
    
    def startProcess(self):
        self.__c.write_single_register(0,1)
    
    def startCooling(self):
        self.__c.write_single_register(0,3)
    
    def setTemp(self, val):
        self.__c.write_single_register(0,val)
    
    def getTemp(self):
        curTemp = self.__c.read_input_registers(2)[0]
        setTemp = self.__c.read_input_registers(3)[0]
        return [curTemp, setTemp]
    
    def setTemp(self, temp):
        self.__c.write_single_register(3,temp)