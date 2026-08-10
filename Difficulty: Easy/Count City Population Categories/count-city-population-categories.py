class Solution:
    def countCityPopulationCategories(self, cities):
        small = (cities['population'] < 100000).sum()
        medium = ((cities['population'] >= 100000) & (cities['population'] <= 1000000)).sum()
        large = (cities['population'] > 1000000).sum()

        return pd.DataFrame({
            'category': ['Small City', 'Medium City', 'Large City'],
            'cities_count': [small, medium, large]
        })