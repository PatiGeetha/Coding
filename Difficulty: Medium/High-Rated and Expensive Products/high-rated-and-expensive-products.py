class Solution:
    def filterHighRatedExpensive(self, df):

        return df[
            (df['rating'] >= 4.5) &
            (df['quantity_in_stock'] > 0) &
            (df['price'] >= 300)
        ]
    
  
   