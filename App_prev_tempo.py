#Importando as ferramentas para fazer as requisições.
import requests

#JSON é como uma lista ou dicionário convertido para string.
import json

#Utilizamos o pprint como uma forma mais fácil de visualizacão. Com o programa pronto não precisamos mais dele.
##import pprint
#----------------------------------------------------------------------------------------------------------------
#Chave de acesso gerado no Accuweather
accuweatherAPIKey = 'LFlhbOIrjvJVZyfgR1EvGDc4RBAAlUoa'

#Função p/ pegar as coordenadas.
def pegarCoordenadas():
    #Pedido de requisição no site geoplugin para obter as coordenadas
    r = requests.get('http://www.geoplugin.net/json.gp')
    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
    else:
        localizacao = json.loads(r.text) #converte texto json em dicionário python
        #Var de dici p/ colocar as coordenadas.
        coordenadas = {}
        #Criar uma chave 'lat' no dici p/ jogar a coordenada de latitude.
        coordenadas['lat'] = lat = localizacao['geoplugin_latitude']
        # Criar uma chave 'long' no dici p/ jogar a coordenada de longitude.
        coordenadas['long'] = long = localizacao['geoplugin_longitude']
        return coordenadas
        ##print('lat: ', lat)
        ##print('long: ', long)

#Função p/ pegar o código do local.
def pegarCodigoLocal(lat,long):

    LocationAPIUrl = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
            +'search?apikey=' + accuweatherAPIKey \
                     + '&q=' + lat + '%2C%20' + long + '&language=pt-br'

    #Envio da requisição p/ o site.
    r = requests.get(LocationAPIUrl)
    #Verificação do status da requisição.
    if (r.status_code != 200):
        print('Não foi possível obter o código do local.')
    else:
        ##print(pprint.pprint(json.loads(r2.text)))
        locationResponse = json.loads(r.text)
        #Var dici p/ colocar o nome e o código do local.
        infoLocal = {}
        #Criar chave no dici p/ colocar o nome do local.
        infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ', ' \
            + locationResponse['AdministrativeArea']['LocalizedName'] + '. '\
            + locationResponse['Country']['LocalizedName']
        #Criar chave no dici p/ colocar o código do local.
        infoLocal['codigoLocal'] = locationResponse['Key']
        return infoLocal
        ##print('Código do local: ', codigoLocal)

#Função p/ pegar a previsão do tempo.
def pegarTempoAgora(codigoLocal, nomeLocal):
    #Montagem da URL com o cod e a key inseridas automaticamente.
    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/"\
        + codigoLocal + "?apikey=" + accuweatherAPIKey\
        +"&language=pt-br"
    #Solicitação da requisição do tempo atual.
    r = requests.get(CurrentConditionsAPIUrl)
    #Condicional da resposta p/ imprimir p/ o cliente.
    if (r.status_code != 200):
        print('Não foi possível obter o código do local.')
    else:
        #Var p/ converter a resposta de txt p/ dici python.
        CurrentConditionsResponse = json.loads(r.text)
        #Var dici p/ abrigar as informações do clima.
        infoClima = {}

        ##print(pprint.pprint(CurrentConditionsResponse))
        #Chave p/ abrigar todo texto coletado no Accweather.
        infoClima['textoClima'] = CurrentConditionsResponse[0]['WeatherText']
        #Chave p/ abrigar a temperatura.
        infoClima['temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
        #Chave p/ abrigar o nome do local.
        infoClima['nomeLocal'] = nomeLocal
        return infoClima
#Início do programa:
#Criar um var para facilitar as funções.

coordenadas = pegarCoordenadas()

local = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])

climaAtual = pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])

#Imprimir as respostas.
print('Clima atual em: ' + climaAtual['nomeLocal'])
print(climaAtual['textoClima'])
print('Temperatura: ' + str(climaAtual['temperatura']) + '\xb0' + 'C') #código \xb0 é o cogido p/ graus ceucius
