import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_PATH,MODEL_DIR

df = (
    pd
    .read_csv(DATA_FILE_PATH)
    .drop_duplicates()
    .drop(columns=['name', 'model', 'edition'])
)

X = df.drop(columns = 'selling_price')
y = df['selling_price'].copy()

# Splitting data into train and test splits
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42) 

# Fetches all numeric columns and adds them into a list
num_cols = X_train.select_dtypes(include='number').columns.tolist()

# Fetches all categorical columns and adds them into a list
cat_cols = [col for col in X_train.columns if col not in num_cols] 


num_pipe = Pipeline(steps = [
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())
])

cat_pipe = Pipeline(steps = [
    ('imputer',SimpleImputer(strategy='constant',fill_value='missing')),
    ('encoder',OneHotEncoder(handle_unknown='ignore',sparse_output=False))
])

preprocessor = ColumnTransformer(transformers = [
    ('num',num_pipe,num_cols),
    ('cat',cat_pipe,cat_cols)
])

regressor = RandomForestRegressor(
    n_estimators=10,
    max_depth=5,
    random_state=42
)

rf_model = Pipeline(
    steps=[
        ('pre',preprocessor),
        ('reg',regressor)
    ]
)

rf_model.fit(X_train,y_train)

# creates the model directory if it does not exist
os.makedirs(MODEL_DIR,exist_ok=True) 

# saves the model in the model directory
joblib.dump(rf_model,MODEL_PATH) 