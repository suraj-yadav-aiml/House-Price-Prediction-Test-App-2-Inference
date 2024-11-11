from typing import Any, Dict

from flask import Blueprint, request, jsonify, abort
from pydantic import ValidationError

from schema.appartment import Apartment
from services import model_inference_service


# Initialize a Flask Blueprint for the prediction API endpoint
bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get("/")
def get_prediction() -> Dict[str, Any]:
    """
    Handle GET requests for apartment price prediction.

    This function:
    - Validates and parses input parameters using the `Apartment` Pydantic model.
    - Loads a pre-trained machine learning model through the `ModelInferenceService`.
    - Makes a prediction using the input apartment features.

    Returns:
        dict: A dictionary containing the predicted value in JSON format.

    Raises:
        ValidationError: If input data does not meet the schema requirements.
        Exception: If there is an error loading the model or making a prediction.
    """
    try:
        # Parse and validate input parameters as apartment features
        apartment_features = Apartment(**request.args)
        validated_features = apartment_features.model_dump()  # Dictionary of validated fields


        # Instantiate and load the model using ModelInferenceService
        # model_service = ModelInferenceService()
        # model_service.load_model()

        # Make prediction with the parsed apartment features
        prediction = model_inference_service.predict(list(validated_features.values()))

        # Return the prediction as a JSON response
        return jsonify({
            'prediction': prediction
        })
    
    except ValidationError:
        abort(code=400,description='Bad input parameters')

    except Exception as e:
        return jsonify({
            'error': f"An error occurred during prediction: {str(e)}"
        }), 500


@bp.post("/")
def get_prediction_post() -> Dict[str, Any]:
    """
    Handle POST requests for apartment price prediction.

    This endpoint accepts a POST request with JSON data representing apartment features.
    It validates and processes the input, loads the pre-trained model, and uses it to 
    predict the result based on the given features.

    Args:
        None (the data is passed in the request body as JSON).

    Returns:
        dict: A dictionary containing the prediction result. The response is returned as 
              a JSON object, and it contains either the prediction or an error message.

    Raises:
        Exception: If an error occurs during the prediction process, a 500 response 
                   with an error message is returned
    """

    try:
        # Parse and validate input parameters as apartment features
        apartment_features = Apartment(**request.json)
        validated_features = apartment_features.model_dump()  # Dictionary of validated fields


        # Instantiate and load the model using ModelInferenceService
        # model_service = ModelInferenceService()
        # model_service.load_model()

        # Make prediction with the parsed apartment features
        prediction = model_inference_service.predict(list(validated_features.values()))

        # Return the prediction as a JSON response
        return jsonify({
            'prediction': prediction
        })

    except Exception as e:
        return jsonify({
            'error': f"An error occurred during prediction: {str(e)}"
        }), 500
