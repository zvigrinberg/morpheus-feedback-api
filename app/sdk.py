import argilla as rg
from flask import current_app

def init_argilla(app):
    """
    Initialize the Argilla client once at app startup,
    pointing at the configured workspace.
    """
    app.argilla_client = rg.Argilla(
        api_url=app.config['ARGILLA_API_URL'],
        api_key=app.config['ARGILLA_API_KEY'],
    )

def process_feedback(data):
    """
    Submits feedback data as an rg.Record to the configured Argilla dataset,
    auto-creating the dataset if it does not exist.
    Postman test:localhost:5001/api/feedback
    {
    "response": "Testing feedback via Postman",
    "thumbs": "👍",
    "rating": "5",
    "comment": "Everything looks good!"
    }

    """
    try:
        client  = current_app.argilla_client
        ws      = current_app.config['ARGILLA_WORKSPACE']
        ds_name = current_app.config['ARGILLA_DATASET']

        # 1) Load your pre‑created dataset
        dataset = client.datasets(name=ds_name, workspace=ws)
        if dataset is None:
            return {
                "status":  "error",
                "message": f"Dataset '{ds_name}' not found in workspace '{ws}'",
                "data":    data
            }

        # 2) Build a single Record
        record_dict = {
            "response": data["response"],
            "thumbs":   data["thumbs"],
            "rating":   int(data["rating"]),
            "comment":  data["comment"],
        }

        # 3) Log it
        dataset.records.log([record_dict])

        return {
            "status": "success",
            "data":   data
        }

    except Exception as e:
        return {
            "status":  "error",
            "message": str(e),
            "data":    data
        }