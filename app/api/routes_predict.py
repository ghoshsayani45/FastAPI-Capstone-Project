from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key , get_current_user
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float

@router.post("/predict")
def predict_price(car_features: CarFeatures, user = Depends(get_current_user),_=Depends(get_api_key)):
    """
    Predict the price of a car based on its features.

    Args:
        car_features (CarFeatures): The features of the car.
        user : The current authenticated user (injected by dependency).
        _ : API key validation (injected by dependency).

    Returns:
        dict: A dictionary containing the predicted price.
    """
    # Convert the Pydantic model to a dictionary
    features_dict = car_features.model_dump()
    
    # Call the prediction service
    predicted_price = predict_car_price(features_dict)
    
    return {"predicted_price": f'{predicted_price:,.2f}'}