from src.app import prod_app


def emulate_app_context(func):
    def emulate(*args, **kwargs):
        app = prod_app()
        with app.app_context():
            output = func(*args, **kwargs)
        return output

    return emulate
