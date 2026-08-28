import pandas as pd
import numpy as np
df = pd.read_csv('data/student_performance.csv')
tmp_df = df.copy()
print(df.head())
rows, columns = df.shape
print(f"Number of Rows: {rows}")
print(f"Number of Columns: {columns}")
print(df.columns)
print(f"Missing Values: {df.isna().values.any()}")
print(f"Average Final Score: {df['Final_Score'].mean()}")
print(f"Student with Highest Final Score: {df[df['Final_Score'] == df['Final_Score'].max()]['Student'].iloc[0]}")
tmp_df['Improvement'] = tmp_df['Final_Score'] - tmp_df['Previous_Score']
print(tmp_df['Improvement'].head())
print(f"Students with Attendance >= 80: {list(df[df['Attendance'] >= 80]['Student'])}")
processed_df = tmp_df.sort_values(by='Final_Score', ascending=False)
processed_df.to_csv('data/processed_student_performance.csv', index=False)