import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def number_loans_per_gender(df):

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))

    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    genderdf = df.groupby(['mnth_yr2', 'gender']).agg('count')[['id']]

    gd_df = df.groupby(['Qtr', 'gender'])['id'].count().reset_index()
    gd_df = gd_df[gd_df['Qtr'] < pd.Period('2017Q3')]
    plt.figure(figsize=(12,6))
    sns.pointplot(
        x='Qtr',
        y='id',
        hue='gender',
        alpha = 0.8,
        data=gd_df)
    plt.title('Number of Loans per Gender and Quarter')
    plt.ylabel('Number of Loans')
    plt.xlabel('Quarter')
    plt.savefig(os.path.join('image', 'num_loans_per_gender.png'))
    plt.show()
