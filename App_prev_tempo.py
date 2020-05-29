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
        print('Obtendo clima do local: ', nomeLocal)
        ##print('Código do local: ', codigoLocal)

        CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/"\
                + codigoLocal + "?apikey=" + accuweatherAPIKey\
                +"&language=pt-br"
        r3 = requests.get(CurrentConditionsAPIUrl)
        if (r3.status_code != 200):
            print('Não foi possível obter o código do local.')
        else:
            CurrentConditionsResponse = json.loads(r3.text)
            #print(pprint.pprint(CurrentConditionsResponse))
            textoClima = CurrentConditionsResponse[0]['WeatherText']
            temperatura = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: ', textoClima)
            print('Temperatura', str(temperatura) + 'graus Ceucius')
