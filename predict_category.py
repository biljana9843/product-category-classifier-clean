# -------------------------------
# 10.2: predict_category.py
# -------------------------------
import joblib
import pandas as pd

# Učitavanje sačuvanog modela
model_path = "saved_models/best_product_category_model.pkl"
pipeline = joblib.load(model_path)
print("Model uspešno učitan!")

# Funkcija za predikciju kategorije proizvoda
def predict_category(title):
    df_input = pd.DataFrame({
        'Product Title': [title],
        'Title_Word_Count': [len(title.split())],
        'Title_Char_Count': [len(title)],
        'Contains_Number': [int(any(c.isdigit() for c in title))],
        'Special_Char_Count': [sum(not c.isalnum() and not c.isspace() for c in title)]
    })
    category = pipeline.predict(df_input)[0]
    return category

# Interaktivno testiranje
while True:
    user_input = input("Unesite naziv proizvoda (ili 'exit' za kraj): ").strip()
    if user_input.lower() == 'exit':
        break
    predicted_category = predict_category(user_input.lower())
    print(f"Predviđena kategorija: {predicted_category}")
