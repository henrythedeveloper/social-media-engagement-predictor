import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import classification_report

# Load processed data
data = pd.read_csv('processed_data.csv')

# Separate features and target
X = data[['Daily_Minutes_Spent', 'Posts_Per_Day', 'App', 'Likes_Per_Day', 'Follows_Per_Day']]
y = data['High_Engagement']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'model.pkl')
print("Model training completed. Model saved to 'model.pkl'.")
