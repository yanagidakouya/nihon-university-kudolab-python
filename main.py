import serial
import time
import requests
import json

def main():
  time.sleep(1)
  ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
  ser.flush()
  url = 'http://18.176.192.40/api/insert_data'

  while True:
    line = ser.readline().decode('utf-8')
    line = line.rstrip()
    print(line)
    if not line:
      print('null')
    else:
      send_data = { "send_data": line }
      headers = {"content-type": "application/json"}
      res = requests.post(url, data = json.dumps(send_data), headers = headers, verify = False)
      print(res.text)
      print(res)

main()