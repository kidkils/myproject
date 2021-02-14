from influxdb import InfluxDBClient
from datetime import datetime

def getData(query):
    client = InfluxDBClient(host='192.168.43.70', port=8086, username='iot', password='iot12345')
    client.switch_database('iot_multinode_DB')
    result = client.query(query).raw

    if result:
        return result
    
    return 0

def getDataHujan():
    query = "SELECT time, value FROM hujan ORDER BY desc LIMIT 1"
    result = getData(query)
    hujan = {}
    hujan['label'] = []
    hujan['data'] = []

    for data in result['series'][0]['values']:
        data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        data[0] = data[0].strftime('%H:%M:%S')

        hujan['label'].append(data[0])
        hujan['data'].append(data[1])
    
    if hujan:
        return hujan

    return 0

def getDataSuhu():
    query = "SELECT time, value FROM suhu ORDER BY desc LIMIT 12"
    result = getData(query)
    suhu = {}
    suhu['label'] = []
    suhu['data'] = []

    for data in result['series'][0]['values']:
        data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        data[0] = data[0].strftime('%H:%M:%S')

        suhu['label'].append(data[0])
        suhu['data'].append(data[1])

    if suhu:
        return suhu
    
    return 0

def getDataMoisture():
    query = "SELECT time, value FROM moisture ORDER BY desc LIMIT 12"
    result = getData(query)
    moisture = {}
    moisture['label'] = []
    moisture['data'] = []

    for data in result['series'][0]['values']:
        data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        data[0] = data[0].strftime('%H:%M:%S')

        moisture['label'].append(data[0])
        moisture['data'].append(data[1])

    if moisture:
        return moisture
    
    return 0

def getDataKelembapan():
    query = "SELECT time, value FROM kelembapan ORDER BY desc LIMIT 12"
    result = getData(query)
    kelembapan = {}
    kelembapan['label'] = []
    kelembapan['data'] = []

    for data in result['series'][0]['values']:
        data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        data[0] = data[0].strftime('%H:%M:%S')

        kelembapan['label'].append(data[0])
        kelembapan['data'].append(data[1])

    if kelembapan:
        return kelembapan
    
    return 0