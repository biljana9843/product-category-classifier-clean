# -------------------------------
# 10.1: train_model.py
# -------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Učitavanje podataka
df = pd.read_csv("products.csv")
df.columns = df.columns.str.strip()

# Priprema i čišćenje podataka
df_model = df[['Product Title', 'Category Label']].dropna()
df_model['Product Title'] = df_model['Product Title'].str.lower()
df_model = df_model.reset_index(drop=True)

# Feature engineering
df_model['Title_Word_Count'] = df_model['Product Title'].str.split().str.len()
df_model['Title_Char_Count'] = df_model['Product Title'].str.len()
df_model['Contains_Number'] = df_model['Product Title'].str.contains(r'\d').astype(int)
df_model['Special_Char_Count'] = df_model['Product Title'].str.count(r'[^a-zA-Z0-9 ]')

# Podela na X i y
X = df_model[['Product Title', 'Title_Word_Count', 'Title_Char_Count', 'Contains_Number', 'Special_Char_Count']]
y = df_model['Category Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Preprocesor
preprocessor = ColumnTransformer(transformers=[
    ('tfidf', TfidfVectorizer(), 'Product Title'),
    ('num', StandardScaler(), ['Title_Word_Count', 'Title_Char_Count', 'Contains_Number', 'Special_Char_Count'])
])

# Definisanje modela
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
])

# Treniranje
pipeline.fit(X_train, y_train)

# Čuvanje modela
model_folder = "saved_models"
os.makedirs(model_folder, exist_ok=True)
model_path = os.path.join(model_folder, "best_product_category_model.pkl")
joblib.dump(pipeline, model_path)
print(f"Najbolji model je uspešno sačuvan u: {model_path}")
