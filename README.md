# product-category-classifier
ML projekat za automatsku klasifikaciju proizvoda po nazivu

Product Category Classifier
Automatski predviđa kategoriju proizvoda na osnovu naziva, ubrzavajući unos novih proizvoda u online prodavnicu.

Struktura projekta
product-category-classifier/

notebooks/ Analiza i treniranje modela (Jupyter/Colab)
products.csv Dataset sa 30.000+ proizvoda
train_model.py Skript za treniranje modela
predict_category.py Skript za interaktivnu predikciju
best_product_category_model.pkl Sačuvani model
README.md

Kako koristiti
Treniranje modela: python train_model.py
Predikcija kategorija: python predict_category.py
Unesite naziv proizvoda i dobićete predviđenu kategoriju. Za kraj unesite exit.

Primeri
iphone 7 32gb gold → Mobile Phones
olympus e m10 mark iii → Digital Cameras
kenwood k20mss15 solo → Microwaves
bosch wap28390gb 8kg 1400 spin → Washing Machines
bosch serie 4 kgv39vl31g → Fridge Freezers
smeg sbs8004po → Fridge Freezers

Tehnologije i biblioteke
Python 3.13.3, pandas, scikit-learn, joblib, Jupyter/Colab
