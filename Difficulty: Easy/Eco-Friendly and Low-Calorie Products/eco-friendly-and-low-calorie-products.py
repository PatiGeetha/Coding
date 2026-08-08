import pandas as pd

def find_eco_low_calorie_products(df):
    result = df[(df['eco_friendly'] == 'Y') & (df['calories'] <= 200)]
    result = result[['product_id', 'product_name', 'calories']]
    return result