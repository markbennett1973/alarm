# Based on http://www.mogalla.net/201502/lichtsensor-tsl2561-am-raspberry
import smbus
import logging

# Define variables and constants
Bus_Number = 1
TSL2561_Address = 0x39
Start = 0x51
Ambient_High_Byte = 0
Ambient_Low_Byte = 0
IR_High_Byte = 0
IR_Low_Byte = 0
Ambient = 0
IR = 0
Ratio = 0
Lux = 0


class LightSensor(object):
    """ Interface to the light sensor
    """
    def __init__(self):
        """ Initialise the light sensor
        """
        logging.info('LightSensor:init')

        # Instantiate an I2C object
        self.i2cBus = smbus.SMBus(Bus_Number)

        # Start the 400ms loop
        self.i2cBus.write_byte_data(TSL2561_Address, 0x80, 0x03)

    def get_light_level(self):
        """ Get the current light level in lux
        """
        ambient_low_byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8c)
        ambient_high_byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8d)
        ambient = (ambient_high_byte*256)+ambient_low_byte
        ir_low_byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8e)
        ir_high_byte = self.i2cBus.read_byte_data(TSL2561_Address, 0x8f)
        ir = (ir_high_byte*256)+ir_low_byte
        ratio = ir / float(ambient)
        if 0 < ratio <= 0.50:
            lux = 0.0304*ambient-0.062*ambient*(ratio**1.4)
        elif 0.50 < ratio <= 0.61:
            lux = 0.0224*ambient-0.031*ir
        elif 0.61 < ratio <= 0.80:
            lux = 0.0128*ambient-0.0153*ir
        elif 0.80 < ratio <= 1.3:
            lux = 0.00146*ambient-0.00112*ir
        else:
            lux = 0

        logging.debug('Got light level %f', lux)

        return lux
