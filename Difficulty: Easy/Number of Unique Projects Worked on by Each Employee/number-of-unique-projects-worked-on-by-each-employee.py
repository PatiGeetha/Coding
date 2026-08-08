class Solution:
    def employeeProjects(self, employee_projects):
        result = (
            employee_projects
            .groupby('employee_id')['project_id']
            .nunique()
            .reset_index(name='cnt')
        )
        return result