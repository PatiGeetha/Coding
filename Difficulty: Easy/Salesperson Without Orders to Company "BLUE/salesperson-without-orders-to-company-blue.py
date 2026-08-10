def find_salesperson_without_blue_orders(df_salesperson, df_orders, df_company):
    blue_company = df_company[df_company['name'] == 'BLUE']
    blue_orders = df_orders[df_orders['com_id'].isin(blue_company['com_id'])]

    result = df_salesperson[
        ~df_salesperson['sales_id'].isin(blue_orders['sales_id'])
    ][['name']]

    return result