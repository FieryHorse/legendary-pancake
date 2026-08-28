import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('data/processed_student_performance.csv')
plt.figure(figsize=(60, 6))
plt.bar(df['Student'], df['Final_Score'])
plt.xlabel('Student', fontsize = 30)
plt.ylabel('Final Score', fontsize = 30)
plt.title('Final Scores of Students', fontsize = 50)
plt.grid(True, alpha = 0.3, axis = 'y')
plt.savefig('plots/final_scores.png')
plt.close()

plt.scatter(df['Hours_Studied'], df['Final_Score'], alpha = 0.5)
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.title('Final Score vs Hours Studied')
plt.grid(True, alpha = 0.3)
plt.savefig('plots/study_vs_score.png')
plt.close()

plt.hist(df['Final_Score'], edgecolor='black', bins=20, alpha = 0.7)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Distribution of Final Scores')
plt.grid(True, alpha = 0.3, axis = 'y')
plt.savefig('plots/scores_distribution.png')
plt.close()

categories = ['>60', '40-60', '<=40']
size1 = len(df[df['Final_Score'] > 60])
size2 = len(df[(df['Final_Score'] > 40) & (df['Final_Score'] <= 60)])
size3 = len(df[df['Final_Score'] <= 40])
total = size1 + size2 + size3
sizes = [(size1/total)*100, (size2/total)*100, (size3/total)*100]
plt.pie(sizes, labels = categories, colors = ['lightcoral', 'lightblue', 'lightgreen'], autopct = '%1.1f%%', startangle = 90)
plt.title('Final Score Distribution')
plt.savefig('plots/custom_plot.png')