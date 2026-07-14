student_scores = [87, 64, 152, 91, 118, 73, 56, 184, 97, 125, 68, 79, 143, 102, 59, 167, 84, 199, 76, 111, 94, 61, 138, 82, 175]

total_exams_score = sum(student_scores)
print(total_exams_score)

# the same but using loops

total_exams_score = 0
for score in student_scores:
    total_exams_score += score

print(total_exams_score)

max_score = max(student_scores)
print(max_score)

# finding max
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)