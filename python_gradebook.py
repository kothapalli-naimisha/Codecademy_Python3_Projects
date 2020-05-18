last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics','calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
gradebook =list(zip(subjects, grades))
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
full_gradebook = list(zip(last_semester_gradebook, gradebook))
print(full_gradebook)
