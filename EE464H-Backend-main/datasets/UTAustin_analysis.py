import pandas as pd
import math

def UTAustinAnalysis():
    grad_df = pd.read_csv('datasets/UTAustin_gradData.csv')
    en_df = pd.read_csv('datasets/UTAustin_enrollData.csv')

    year = grad_df['Year'].max()
    gender = {'Men':0, 'Women':1}
    

    grad_df = grad_df.loc[grad_df['Year'] == year]
    # grad_df = grad_df.loc[grad_df['Sex'] == gender_category]
    print(grad_df)
    en_df = en_df.loc[en_df['Year'] == year]
    en_df = en_df.loc[en_df['ID University'] == '228778']
    print(en_df)
    US_grad_data = 0
    # US_metric = en_g_USTotal[race_category][gender[gender_category]] - grad_g_USTotal[race_category][gender[gender_category]]
    # regional_metric = race_enrollment[region][race_category][gender[gender_category]] - race_grad[region][race_category][gender[gender_category]]
    # local = 0

    return US_grad_data

UTAustinAnalysis()