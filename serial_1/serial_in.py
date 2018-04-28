import serial

ser = serial.Serial('COM2', 9600, timeout=0.1)
def main():
    while 1:
        if(ser.inWaiting()>0):
            data = ser.readline().decode()
            if str(data) == 's':
                break
            print(data)
            ser.write(b'r')
def fn():
    while 1:
        ser.write(b's')
        print('sent')
        if ser.inWaiting()>0:
            d = ser.read().decode()
            print(d)
            break

try:
    fn()
except KeyboardInterrupt:
    print('end')
