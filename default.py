import sys
import xbmc

from resources.lib import utils, menu, comm

def router(paramstring):
    params = utils.uri_to_dict(paramstring)
    
    if 'action' in params:

        if params['action'] == 'ip':
            utils.command(['vpn',  'ip'])

        elif params['action'] == 'status':
            utils.command(['vpn',  'status'])

        elif params['action'] == 'stop':
            utils.command(['vpn',  'stop'])
    
        elif params['action'] == 'start':
            utils.command(['vpn',  'start', params['nb']], silent=True)
            utils.command(['vpn',  'status'])

        elif params['action'] == 'list':
            menu.make_menu(comm.get_endpoints())

    else:
        menu.make_menu(comm.get_main_menu()) # First level

if __name__ == '__main__':
    router(sys.argv[2][1:])
