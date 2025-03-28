#! /bin/python3
# ioanding 2020

import json
import requests


# download json
headers = {
    'Accept-Language': 'en-US,en;q=0.9,el;q=0.8',
}

try:
    response = requests.get('http://192.168.1.1/data/Status.json', headers=headers)
except(OSError):
    print('Network is unreachable')
    quit()
except:
    print('Err general')
    quit()

json_s = json.dumps(response.json()) # convert list to string
data = json.loads(json_s)  # decode string to data

lstv = []
for x in data:
    lstv.append(x['varvalue'])

snr = []
snrtosplit = str(lstv[24])
snr = snrtosplit.split()
# display
print('{:<41} {:<1}'.format(lstv[0], lstv[13]))
print('In sync since ' + lstv[14] + '\n')
print('{:<25} {:<15} {:<1}'.format(lstv[21], 'Downstream', 'Upstream\n'))
print('{:<25} {:<15} {:<1}'.format('Synced Bitrate:', lstv[17] + ' kbps', lstv[18] + ' kbps'))
print('{:<25} {:<15} {:<1}'.format('Attainable Bitrate:', lstv[19] + ' kbps', lstv[20] + ' kbps\n'))
print('{:<25} {:<15} {:<1}'.format('Line Attenuation:', lstv[27] + ' dB', lstv[26] + ' dB'))
print('{:<25} {:<15} {:<1}'.format('SNR:', snr[0] + ' dB', snr[2] + ' dB\n'))
print('{:<25} {:<15} {:<1}'.format('Errors in data stream:', lstv[22] + ' CRC', lstv[23] + ' FEC'))
