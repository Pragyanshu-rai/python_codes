import pandas as pd

df = pd.read_csv('data/stack-overflow-developer-survey-2021/survey_results_public.csv')
df_schema = pd.read_csv('data/stack-overflow-developer-survey-2021/survey_results_schema.csv')
pd.set_option('display.max_columns', 80)


print(df.head())
print(df.shape)
print(df_schema)