
isl_score = int(input("score in islamiyat :"))
math_score = int(input("score in math:"))
eng_score = int(input("score in english:"))
CF_score = int(input("score in CF:"))
PF_score = int(input("score in PF:"))

subjects = {
    'islamiyat':isl_score,
    'math':math_score,
    'english':eng_score,
    'CF':CF_score,
    'PF':PF_score
}
grading_scale = {
    90:'A',
    80:'B',
    70:'C',
    60:'D',
    50:'E',
    40:'F'
}

obtain_score  = (isl_score + math_score + eng_score + CF_score + PF_score) 
percentage = (obtain_score/80) * 100
print(f"your percentage is:{percentage}")

if percentage >= 90:
    print(f"your Grade :{grading_scale[90]}")
elif percentage > 80 and percentage < 90:
    print(f"your Grade :{grading_scale[80]}")
elif percentage > 70 and percentage < 80:
    print(f"your Grade :{grading_scale[70]}")
elif percentage > 60 and percentage < 70:
    print(f"your Grade :{grading_scale[60]}")
elif percentage > 50 and percentage < 60:
    print(f"your Grade :{grading_scale[50]}")
else:
    print(f"your Grade :{grading_scale[40]}")    