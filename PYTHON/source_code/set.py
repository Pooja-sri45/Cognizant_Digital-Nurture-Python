def common_skills(set1, set2):

    if not isinstance(set1, set) or not isinstance(set2, set):
        print("Invalid input")
        return

    common = set1 & set2

    print("Common Skills:", common)

skills1 = {"Python", "Java", "SQL"}
skills2 = {"Python", "C++", "SQL"}

common_skills(skills1, skills2)