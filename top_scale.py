import serial

class Scale(object):

    def __init__(self, device):
        device.baudrate = 9600
        self._device = device
        self._data = '' 
        self._readings = []
        self._max_stored_readings = 10

    def _store_reading(self, data):
        if len(self._readings) >= self._max_stored_readings:
            self._readings = self._readings[1::]
        self._readings.append(data)

    def fetch_data(self):

        bits = self._device.inWaiting()

        # NOTE if there are bits to read and we have old data, clear it out
        if self._data is not '' and bits:
            self._data = ''

        # NOTE only update the reading if we have bits to read.
        if bits:
            d = self._device.read(bits)
            reading = self.parse_data(d)
            self._store_reading(reading)
            self._data += d

    def parse_data(self, data):
        pd = None
        parseable_data = None

        if len(data) == 14:
            parseable_data = data

        if len(data) > 14:
            parseable_data = data[-14::]


        if parseable_data is not None:
            pd = parseable_data[3:11].strip()

        return pd

    def get_reading(self):
        reading = None

        self.fetch_data()
        if any(self._readings):
            reading = self._readings[-1]

        return reading

    def reading(self):
        return self.get_reading()
