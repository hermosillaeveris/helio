# -*- coding: utf-8 -*-
"""[summary]
"""
import connexion
from connexion.resolver import RestyResolver

connexionApp = connexion.FlaskApp(__name__, specification_dir='swagger/')
connexionApp.add_api('hello_world_swagger.yaml', resolver=RestyResolver('api'))

app = connexionApp.app

if __name__ == '__main__':
    connexionApp.run(port=9090)
