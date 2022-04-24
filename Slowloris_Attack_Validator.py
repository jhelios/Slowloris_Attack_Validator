import requests
import urllib3
from colorama import init, Fore, Back, Style
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get(targetURI):
    instanteInicial = datetime.now()
    try:
        re =  requests.get(targetURI, verify=False, timeout=15)

    except Exception as e:
        respuesta = Style.BRIGHT+Fore.RED+'[-] No veo la URL. Han pasado 20 segundos'+Fore.RESET
        print respuesta
        return False, respuesta
    respuesta = (Style.BRIGHT+'[+] Veo la URL en '+Fore.BLUE+'%s milisegundos' % ((datetime.now() - instanteInicial).microseconds / 1000)+Fore.RESET)
    print respuesta
    return True, respuesta


if __name__ == '__main__':
    import argparse
    import sys
    parser= argparse.ArgumentParser(description='Script para validar disponibilidad tras ejecutar SlowDOS')
    parser.add_argument('-url', help='Indique la URL a revisar')
    parser.add_argument('-revisar', action='store_true', default=True, help='Vertificar si el sitio responde')
    args = parser.parse_args()

    if  args.revisar:
        if args.url is None:
            print('Por favor indicar la -url')
            sys.exit()
        targetURI = args.url
        for i in range(1,20,1):
            res, run = get(targetURI)
