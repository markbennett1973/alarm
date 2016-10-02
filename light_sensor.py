# Based on http://www.mogalla.net/201502/lichtsensor-tsl2561-am-raspberry
import smbus

#Define variables and constants
Bus_Number = 1
TSL2561_Address = 0x39
Start = 0x51
Ambient_High_Byte = 0
Ambient_Low_Byte = 0
IR_High_Byte = 0
IR_Low_Byte = 0
Ambiente = 0
IR = 0
Ratio = 0
Lux = 0

class LightSensor(object):

    def __init__(self):
        #Instantiate an I2C object
        self.i2cBus = smbus.SMBus(Bus_Number)

        #Start the 400ms loop
        self.i2cBus.write_byte_data(TSL2561_Address, 0x80, 0x03)

    def get_light_level(self):
        Ambient_Low_Byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8c)
        Ambient_High_Byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8d)
        Ambient = (Ambient_High_Byte*256)+Ambient_Low_Byte
        IR_Low_Byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8e)
        IR_High_Byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8f)
        IR = (IR_High_Byte*256)+IR_Low_Byte
        Ratio = IR / float (Ambient)
        if 0 < Ratio <= 0.50:
            Lux = 0.0304*Ambient-0.062*Ambient*(Ratio**1.4)
        elif 0.50 < Ratio <= 0.61:
            Lux = 0.0224*Ambient-0.031*IR
        elif 0.61 < Ratio <= 0.80:
            Lux = 0.0128*Ambient-0.0153*IR
        elif 0.80 < Ratio <= 1.3:
            Lux = 0.00146*Ambient-0.00112*IR
        else:
            Lux = 0

        return Lux


