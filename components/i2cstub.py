from hal_impl.i2c_helpers import I2CSimBase

class I2CStub(I2CSimBase):
    def transactionI2C(self, port, deviceAddress, dataToSend, sendSize, dataReceived, receiveSize):
        return True
