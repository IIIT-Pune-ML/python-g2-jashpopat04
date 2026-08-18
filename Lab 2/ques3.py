import pandas as pd

df=pd.DataFrame({
    'Student':['A','B','C','D','E','F','G','H'],
    'Department':['CSE','CSE','ECE','ECE','CSE','ECE','CSE','ECE'],
    'Gender':['F','M','F','M','M','F','F','M'],
    'Marks':[85,72,91,65,78,88,95,70],
    'Attendance':[92,81,96,72,85,90,98,75]
})

print("Average marks by department:")
print(df.groupby('Department')['Marks'].mean())

print("\nAverage marks by Department and Gender:")
print(df.groupby(['Department','Gender'])['Marks'].mean())

print("\nStudent with highest marks in each department:")
print(df.loc[df.groupby('Department')['Marks'].idxmax(),['Department','Student','Marks']])

dept_avg=df.groupby('Department')['Marks'].transform('mean')

print("\nStudents above department average:")
print(df[df['Marks']>dept_avg])

attendance_avg=df.groupby('Department')['Attendance'].mean()

print("\nAverage attendance by department:")
print(attendance_avg)

print("\nDepartment with highest average attendance:")
print(attendance_avg.idxmax())