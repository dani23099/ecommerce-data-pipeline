import pandas as pd
import requests

# 1. New data source
url = "https://fakestoreapi.com/products"

print("Calling the Global E-commerce API...")
response = requests.get(url)

if response.status_code == 200:
    print("Access granted! Extracting data...")
    datos_json = response.json()


    df = pd.DataFrame(datos_json)

    # 3. Clean and structure the columns for database
    df_limpio = df[['id', 'title', 'price', 'category']]
    df_limpio = df_limpio.rename(columns={
        'id': 'product_id',
        'title': 'product_name',
        'price': 'current_price',
        'category': 'product_category'
    })

    # 4.Save the table in CSV format
    df_limpio.to_csv("ecommerce_data.csv", index=False)
    print("\nEcommerce_data.csv file is ready to be analyzed.")

else:
    print(f"Something went wrong. Error code: {response.status_code}")