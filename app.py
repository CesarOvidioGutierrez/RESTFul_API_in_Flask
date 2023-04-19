from flask import Flask
from dotenv import load_dotenv
from config import configure_app, configure_logging


load_dotenv()
configure_logging()

def create_app():
    app = Flask(__name__)
    app = configure_app(app)
    return app

def run():
    app = create_app()
    @app.route('/')
    def index():
        return 'Hola, este es mi primer contenedor Docker!'
    app.run(host='0.0.0.0')



if __name__ == '__main__':
    run()
