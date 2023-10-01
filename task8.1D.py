# Task 8.1D (ESD)
# Light Sensor- BH1750
""" The `smbus` library in Python is used to communicate with hardware devices connected via the I2C bus.
    It enables read and write operations, error handling, and support for multiple bus numbers,
    making it ideal for interfacing with I2C-compatible components on platforms like Raspberry Pi."""
### Libraries Imported ###
import smbus
import time

### Sensor Configurations ###
light_sensor = 0x23 # I2C address of the light sensor
low_mode = 0x00 #Configuration setting for low power mode on the light sensor
high_mode = 0x01 #Configure the sensor for high-power mode, which might provide more accurate or frequent readings at the expense of higher power consumption
Reset = 0x07 #Sending hexadecimal value to the sensor might reset its settings or put it in a default state.
ONE_TIME_HIGH_RES_MODE = 0X23 #instructs the sensor to perform a one-time high-resolution measurement of light intensity


bus = smbus.SMBus(1)  # object of smbus library

#Function used to calculate light intensity
def Intensity_Calculation(address):           #Here argument address is used as two-element list containing the high and low bytes of the sensor data.
    intensity = ((address[1] + (256 *address[0]))/1.2) 
    return intensity

#read the light intensity from the sensor.
def light():
    address = bus.read_i2c_block_data(light_sensor,ONE_TIME_HIGH_RES_MODE)
    """ The bus object, which is an instance of the smbus.SMBus class.
        It reads a block of data from the specified I2C device (identified by light_sensor) using the specified mode (ONE_TIME_HIGH_RES_MODE)."""
    value = Intensity_Calculation(address)
    return value
 
# Function used to categorise light intensity into different levels such as "Too bright","Bright","Medium","Dark" and "Too Dark" based on their ideal thresholds. 
def  Light_category():
    while True:
        lux = light() # variable used to store the captured intensity values
        print (lux)

        if(lux >= 1200):
            print("Too bright")
        elif(lux >= 700 and lux < 1199):
            print("Bright")
        elif(lux >= 300 and lux < 699):
            print("Medium")    
        elif(lux < 50 and lux > 299):
            print("Dark")
        elif(lux < 49):
            print("Too Dark")
        
        time.sleep(0.5)
Light_category ()
