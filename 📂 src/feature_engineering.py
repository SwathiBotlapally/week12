def add_clv(df):
    df['CLV'] = df['MonthlyCharges'] * df['tenure']
    return df
