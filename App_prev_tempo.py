import requests
import json #JSON é como uma lista ou dicionário convertido para string.
import pprint

#Chave de acesso gerado no Accuweather
accuweatherAPIKey = 'LFlhbOIrjvJVZyfgR1EvGDc4RBAAlUoa'

#Pedido de requisição no site geoplugin para obter as coordenadas
r = requests.get('http://www.geoplugin.net/json.gp')


if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    localizacao = json.loads(r.text) #converte texto json em dicionário python
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    print('lat: ', lat)
    print('long: ', long)

    LocationAPIUrl = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
            +'search?apikey=' + accuweatherAPIKey \
                     + '&q=' + lat + '%2C%20' + long + '&language=pt-br'

    r2 = requests.get(LocationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o código do local.')
    else:
        #print(pprint.pprint(json.loads(r2.text)))
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ', ' \
        + locationResponse['AdministrativeArea']['LocalizedName'] + '. '\
        + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print('Local: ', nomeLocal)
        print('Código do local: ', codigoLocal)
