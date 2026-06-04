
def assign_grade(score):

    if score < 0 or score > 100:
        print("Invalid score")
        return

    if score >= 90:
        print("Grade A")
    elif score >= 75:
        print("Grade B")
    else:
        print("Grade C")

score = 88
assign_grade(score)

