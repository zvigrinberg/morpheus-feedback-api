import argilla


def init_argilla(app):
    """
    Initialize the Argilla SDK using Flask app configuration.
    """
    argilla.Argilla.__init__(
        api_key=app.config['ARGILLA_API_KEY'],
        api_url=app.config['ARGILLA_API_URL']
    )


def process_request(data):
    """
    Processes feedback data by calling the Argilla SDK.
    Replace 'some_function' with the appropriate Argilla SDK function.
    """
    try:
        dataset = argilla.datasets("my_dataset")
        result = argilla.Argilla.some_funtion(data)
    except Exception as e:
        result = {"error": str(e)}
    return result
