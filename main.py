import serial
import time
import requests
import json

def main():
  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.flush()
  url = 'http://18.176.192.40/api/insert_data'

  while True:
    time.sleep(1)
    line = ser.readline().decode('utf-8')
    line = line.rstrip()
    print(line)
    send_data = { "send_data": line }
    headers = {"content-type": "application/json"}
    res = requests.post(url, data = json.dumps(send_data), headers = headers, verify = False)
    print(res.text)
    print(res)

main()