from pyModbusTCP.client import ModbusClient
import PyQt5
c = ModbusClient(host="10.0.6.10", port=503, unit_id=1, auto_open=True)

# c.write_single_register(0,12)
# print(c.read_input_registers(0)[0])
 
 
def setTemp(temp):
    if(type(temp) == int or type(temp) == float):
        c.write_single_register(0,temp)

def getTemp():
    print(c.read_input_registers(0)[0])

class ModbusOwen:
    def __init__(self, ipaddr, port):
        self.__ipaddr=ipaddr
        self.__port=port
        self.__c=ModbusClient(host=ipaddr, port=port, unit_id=1, auto_open=True)
    @property
    def ipaddr(self):
        return self.__ipaddr
    
    @ipaddr.setter
    def ipaddr(self, ipaddr):
        self.__ipaddr=ipaddr
    
    @property
    def port(self):
        return self.port
    
    @port.setter
    def port(self, port):
        self.__port=port
    
    def setTemp(self, val):
        self.__c.write_single_register(0,val)
    
    def getTemp(self):
        return self.__c.read_input_registers(0)[0]

owen=ModbusOwen("10.0.6.10", 503)
