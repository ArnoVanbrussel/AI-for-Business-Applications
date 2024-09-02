import numpy as np
import joblib

# Load the saved model
model_filename = 'cancer_prediction_model.joblib'
loaded_model = joblib.load(model_filename)

# Example new data (replace this with your actual data)
new_data = np.array([[1000025,4,1,1,1,2,1,3,1,1]])

# Make predictions using the loaded model
prediction = loaded_model.predict(new_data)

# Interpret the prediction
if prediction[0] == 2:
    print("Predicted: Benign")
else:
    print("Predicted: Malignant")
