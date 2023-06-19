import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime




# **************** variable decleration ****************
productsList = []
currentTime = int(datetime.timestamp(datetime.now()) * 1000)

# Use the application default credentials.
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



with open('listings.csv', "r") as f:
    for line in f:
        productsList.append(line.rstrip())
f.close()

i = 0
for product in productsList:
    if len(product.split(';')[2]) > 1:
        db.collection('Products').document().set({
            'name': product.split(';')[1],
            'url': product.split(';')[0],
            'photo': product.split(';')[4],
            'discountPrice': product.split(';')[2].split('$')[1].split()[0],
            'price': product.split(';')[3].split('$')[1].split()[0] if len(product.split(';')[3]) > 1 else product.split(';')[2].split('$')[1].split()[0],
        })
        i = i + 1
