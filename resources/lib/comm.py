import utils
from classes import MenuItem


def get_endpoints():

    listing = []

    endpoints = utils.command(['vpn', 'list'], silent=True).split("\n")

    for endpoint in endpoints:

        nb, title = endpoint.split(": ", 2)
        listing.append(MenuItem(title=title, nb=nb, action='start'))

    return listing

def get_main_menu():

    listing = [
        MenuItem(title="Fetch external IP", action='ip'),
        MenuItem(title="List available endpoints", action='list'),
        MenuItem(title="Show current status", action='status'),
        MenuItem(title="Terminate active connections", action='stop')
    ]

    return listing
