class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    APP_NAME = 'Routing App'
    DESCRIPTION = 'Aplicación para practicar routing en Flask'
    DEVELOPERS = [
        {'nombre': 'Carlos', 'apellido': 'Santana'},
        {'nombre': 'James', 'apellido': 'Hetfield'}
    ]
    VERSION = '1.0.0'

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

    from todo_app import init_app

    app = init_app()

    if __name__ == "__main__":
        app.run()

