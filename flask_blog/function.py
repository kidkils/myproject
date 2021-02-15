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
    number_of_node = 1
    hujan = {}

    for i in range(1, number_of_node +1):
        query = "SELECT time, value FROM hujan where namenode='node"+ str(i) +"' ORDER BY desc LIMIT 6"
        result = getData(query)
        h = {}
        h['label'] = []
        h['data'] = []

        for data in result['series'][0]['values']:
            data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            data[0] = data[0].strftime('%H:%M:%S')

            h['label'].append(data[0])
            h['data'].append(data[1])

        hujan['node' + str(i)] = h

    if hujan:
        return hujan

    return 0

def getDataSuhu():
    number_of_node = 1
    suhu = {}

    for i in range(1, number_of_node + 1):
        query = "SELECT time, value FROM suhu where namenode='node"+ str(i) +"' ORDER BY desc LIMIT 6"
        result = getData(query)
        s = {}
        s['label'] = []
        s['data'] = []

        for data in result['series'][0]['values']:
            data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            data[0] = data[0].strftime('%H:%M:%S')

            s['label'].append(data[0])
            s['data'].append(data[1])
        
        suhu['node' + str(i)] = s

    if suhu:
        return suhu
    
    return 0

def getDataMoisture():
    number_of_node = 1
    moisture = {}

    for i in range(1, number_of_node + 1):
        query = "SELECT time, value FROM moisture where namenode='node"+ str(i) +"' ORDER BY desc LIMIT 6"
        result = getData(query)
        m = {}
        m['label'] = []
        m['data'] = []

        for data in result['series'][0]['values']:
            data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            data[0] = data[0].strftime('%H:%M:%S')

            m['label'].append(data[0])
            m['data'].append(data[1])
        
        moisture['node' + str(i)] = m

    if moisture:
        return moisture
    
    return 0

def getDataKelembapan():
    number_of_node = 1
    kelembapan = {}

    for i in range(1, number_of_node + 1):
        query = "SELECT time, value FROM kelembapan where namenode='node"+ str(i) +"' ORDER BY desc LIMIT 6"
        result = getData(query)
        k = {}
        k['label'] = []
        k['data'] = []

        for data in result['series'][0]['values']:
            data[0] = datetime.strptime(data[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            data[0] = data[0].strftime('%H:%M:%S')

            k['label'].append(data[0])
            k['data'].append(data[1])

        kelembapan['node' + str(i)] = k

    if kelembapan:
        return kelembapan
    
    return 0