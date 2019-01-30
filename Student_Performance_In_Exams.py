import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

students_df = pd.read_csv("C:/Users/XPS15-9550/Documents/datasets/StudentsPerformance.csv")

# # # LOOKING AT THE ORIGINAL TABLE # # #  
print(students_df)
print(students_df.describe())

students_df = students_df.drop(['race/ethnicity'], axis=1)

math_score = students_df['math score']
reading_score = students_df['reading score']
writing_score = students_df['writing score']

students_gender = students_df['gender']

# # # CHECKING FOR NULL VALUES IN EACH COLUMN # # #
print(math_score.isnull().sum())
print(reading_score.isnull().sum())
print(writing_score.isnull().sum())

students_df['total score'] = math_score + reading_score + writing_score


# # # Able to see the relationship in scores on gender # # #
sns.set(style = "darkgrid")
sns.pairplot(data = students_df , hue="gender")
plt.show()

# # # Able to see the relationship in scores on whether they completed a test preparation course # # #
sns.pairplot(data = students_df , hue="test preparation course")
plt.show()

# # # Able to see the relationship in scores on lunch status # # #
sns.pairplot(data = students_df , hue="lunch")
plt.show()


# # # Building a function for subplots # # # 

def parents_education_graphs():
    plt.figure(figsize=(13, 4))
    
    plt.subplot(1,3,1)
    sns.barplot(x = "parental level of education" , y="reading score" , data=students_df)
    plt.xticks(rotation = 90)
    plt.title("Reading Scores")

    plt.subplot(1,3,2)
    sns.barplot(x = "parental level of education" , y="writing score" , data=students_df)
    plt.xticks(rotation=90)
    plt.title("Writing Scores")

    plt.subplot(1,3,3)
    sns.barplot(x = "parental level of education" , y="math score" , data=students_df)
    plt.xticks(rotation=90)
    plt.title("Math Scores")

    plt.tight_layout()
    plt.show()

parents_education_graphs()