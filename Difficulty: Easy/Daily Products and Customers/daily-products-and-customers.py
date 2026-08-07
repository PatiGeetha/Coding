class Solution:
    def dailyProductsAndCustomers(self, activities):
        return activities.groupby(
            ['date_id', 'store_name'], as_index=False
        ).agg(
            unique_products=('product_id', 'nunique'),
            unique_customers=('customer_id', 'nunique')
        )