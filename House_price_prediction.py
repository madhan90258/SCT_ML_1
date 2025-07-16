import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = r"C:\Users\madha\OneDrive\Desktop\intern\Housing_price.xlsx"
df = pd.read_excel(file_path, sheet_name='Housing')

# Features and target
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Get sample input from user
try:
    user_area = float(input("Enter the area in square feet: "))
    user_bedrooms = int(input("Enter the number of bedrooms: "))
    user_bathrooms = int(input("Enter the number of bathrooms: "))

    sample_input = pd.DataFrame({
        'area': [user_area],
        'bedrooms': [user_bedrooms],
        'bathrooms': [user_bathrooms]
    })

    # Predict and show result
    predicted_price = model.predict(sample_input)
    print(f"\n🏡 Predicted House Price: ₹{predicted_price[0]:,.2f}")
except ValueError:
    print("❌ Invalid input. Please enter numeric values.")
