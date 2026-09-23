import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv('s.csv')

# Check for required columns
required_cols = ['open', 'high', 'low', 'close', 'volume']
if not all(col in df.columns for col in required_cols):
    raise ValueError("Dataset must contain: open, high, low, close, volume")

# Create target column: 1 if next day's close is higher, else 0
df['Target'] = (df['close'].shift(-1) > df['close']).astype(int)
df.dropna(inplace=True)

# Features and target
features = ['open', 'high', 'low', 'close', 'volume']
X = df[features]
y = df['Target']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
with open('stock_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved to 'stock_model.pkl'")
