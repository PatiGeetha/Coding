class Solution:
    def teamLeaders(self, employee):
        count = employee.groupby("leaderId").size()
        leaders = count[count >= 4].index

        return employee[employee["id"].isin(leaders)][["name"]].reset_index(drop=True)