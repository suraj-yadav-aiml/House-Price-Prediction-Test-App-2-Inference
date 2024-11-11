import pickle as pk
from pathlib import Path
from typing import List, Any

from loguru import logger

from config import model_settings

class ModelInferenceService:
    """
    Service class for loading a machine learning model and performing inference (predictions).
    
    Attributes:
        model (Any): The loaded machine learning model instance.
        model_path (Path): The path to the directory containing the model.
        model_name (str): The name of the model file.
    """

    def __init__(self) -> None:
        """
        Initializes ModelInferenceService with model path and name based on configuration.
        """
        self.model = None
        self.model_path = Path(model_settings.MODEL_PATH)
        self.model_name = model_settings.MODEL_NAME

    def load_model(self) -> None:
        """
        Loads the model from the specified path. If the model is not found, logs an error.

        Raises:
            FileNotFoundError: If the model file does not exist at the specified path.
            Exception: For any other error that occurs during model loading.
        """
        model_file = self.model_path / self.model_name

        try:
            if not model_file.exists():
                logger.error(f"Model file '{self.model_name}' not found.")
                raise FileNotFoundError(f"Model file '{self.model_name}' not found.")

            with model_file.open('rb') as f:
                self.model = pk.load(f)
            logger.info(f"Model '{self.model_name}' loaded successfully.")

        except FileNotFoundError as e:
            logger.error(f"FileNotFoundError: {e}")
        except Exception as e:
            logger.error(f"An error occurred while loading the model: {e}")

    def predict(self, input_data: List[Any]) -> List[Any]:
        """
        Makes a prediction using the loaded model on the provided input data.

        Args:
            input_data (List[Any]): A list of input features required by the model.

        Returns:
            List[Any]: A list of prediction results.

        Raises:
            ValueError: If the model is not loaded before calling predict.
            Exception: For any other error that occurs during prediction.
        """
        try:
            if self.model is None:
                logger.error("Model is not loaded. Please load a model first.")
                raise ValueError("Model is not loaded. Please load a model first.")
            
            logger.info("Making Prediction")
            prediction = self.model.predict([input_data])
            return prediction.tolist()

        except ValueError as e:
            logger.error(f"ValueError: {e}")
        except Exception as e:
            logger.error(f"An error occurred during prediction: {e}")
