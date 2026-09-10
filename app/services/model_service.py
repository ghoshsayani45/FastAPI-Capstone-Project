import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction, get_cached_prediction

# Loads the ML model
model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data: dict):

    # Generate the cache key based on the input data
    cache_key = " ".join([str(val) for val in data.values()])

    # Check if the prediction is already cached
    cached_result = get_cached_prediction(cache_key)
    if cached_result:
        return cached_result

    # Convert input data to DataFrame
    input_data = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Cache the result
    set_cached_prediction(cache_key,prediction)

    return prediction