# http://www.mogalla.net/201502/lichtsensor-tsl2561-am-raspberry
import smbus
from time import sleep

#Definieren der Variablen und Konstanten
Busnummer = 1
Adresse_TSL2561 = 0x39
Start = 0x51
Ambiente_High_Byte = 0
Ambiente_Low_Byte = 0
IR_High_Byte = 0
IR_Low_Byte = 0
Ambiente = 0
IR = 0
Ratio = 0
Lux = 0

#Instanzieren eines I2C Objektes
i2cBus = smbus.SMBus(Busnummer)

#Starten des 400ms Messvorganges
i2cBus.write_byte_data(Adresse_TSL2561, 0x80, 0x03)
while True:
#    print "Auslesen"
    Ambiente_Low_Byte = i2cBus.read_byte_data(Adresse_TSL2561, 0x8c)
    Ambiente_High_Byte = i2cBus.read_byte_data(Adresse_TSL2561, 0x8d)
    Ambiente = (Ambiente_High_Byte*256)+Ambiente_Low_Byte
#    print "Ambiente %d"  % Ambiente
    IR_Low_Byte = i2cBus.read_byte_data(Adresse_TSL2561, 0x8e)
    IR_High_Byte = i2cBus.read_byte_data(Adresse_TSL2561, 0x8f)
    IR = (IR_High_Byte*256)+IR_Low_Byte
#    print "IR %d" % IR
    #Berechnen des Faktors IR/Ambiente
    Ratio = IR / float (Ambiente)
#    print "Ratio %f" % Ratio
    #Berechnung lt. Datenblatt TSL2561T
    if 0 < Ratio <= 0.50:
        Lux = 0.0304*Ambiente-0.062*Ambiente*(Ratio**1.4)
    elif 0.50 < Ratio <= 0.61:
        Lux = 0.0224*Ambiente-0.031*IR
    elif 0.61 < Ratio <= 0.80:
        Lux = 0.0128*Ambiente-0.0153*IR
    elif 0.80 < Ratio <= 1.3:
        Lux = 0.00146*Ambiente-0.00112*IR
    else:
        Lux = 0
    print "Lux = %f" % Lux
#    print "Ende und Sleep 0,5s"
    sleep (2)

