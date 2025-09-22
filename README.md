Product Category Classifier

Ovaj projekat koristi mašinsko učenje za automatsku klasifikaciju proizvoda prema nazivu, ubrzavajući unos artikala u online prodavnicu.

Struktura projekta

notebooks/ – analize i eksperimenti u Jupyter/Colab sveskama

products.csv – skup podataka sa nazivima proizvoda i kategorijama

train_model.py – trenira model i čuva ga u best_product_category_model.pkl

predict_category.py – omogućava interaktivnu predikciju kategorije

README.md – uputstvo za rad sa projektom

Kako pokrenuti projekat

Kloniraj repozitorijum:
git clone https://github.com/biljana9843/product-category-classifier-clean.git
cd product-category-classifier-clean

Instaliraj potrebne biblioteke:
pip install -r requirements.txt

(Po želji) treniraj model na lokalnim podacima:
python train_model.py

Pokreni skriptu za predikciju:
python predict_category.py
Zatim unesi naziv proizvoda; za izlaz otkucaj exit.

Primeri unosa i očekivanih kategorija

iphone 7 32gb gold → Mobile Phones

olympus e m10 mark iii → Digital Cameras

kenwood k20mss15 solo → Microwaves

bosch wap28390gb 8kg 1400 spin → Washing Machines

bosch serie 4 kgv39vl31g → Fridge Freezers

smeg sbs8004po → Fridge Freezers

Napomena
Fajl best_product_category_model.pkl nije postavljen na GitHub zbog veličine. Može se dobiti pokretanjem train_model.py.
