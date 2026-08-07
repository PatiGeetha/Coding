def count_product_categories(df):
    return df.groupby('category_name', as_index=False).agg(
        products_count=('product_id', 'count')
    ).sort_values('category_name')