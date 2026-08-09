class Solution:
    def calculateDiscount(self, products):
        products["discount"] = products.apply(
            lambda row: row["price"]
            if row["product_id"] % 2 == 0 and row["category"].startswith("A")
            else 0,
            axis=1
        )

        return products[["product_id", "discount"]].sort_values("product_id")
        