import pandas as pd

class Solution:
    def frequent_commenters(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df[df["author_id"] == df["viewer_id"]]

        result = (
            result.groupby("author_id")
            .size()
            .reset_index(name="count")
        )

        result = result[result["count"] > 1]

        result = result.rename(columns={"author_id": "id"})

        return result[["id"]].sort_values("id").reset_index(drop=True)