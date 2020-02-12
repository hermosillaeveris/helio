import connexion
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('hello_world_swagger.yaml', resolver=RestyResolver('api'))
    app.run(port=9090)
