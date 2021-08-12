dept_limit = int(input())

with open("applicants.txt", "r") as f:
    x = [line.split() for line in f]


def student_allocation(limit, ppl_list):
    def exam_sorting(the_list, the_subject):
        if the_subject == "Physics":
            for i in the_list:
                i.append((float(i[2]) + float(i[4])) / 2)
                if i[-1] < float(i[6]):
                    i.append(float(i[6]))
            return sorted(the_list, key=lambda y: (-float(y[-1]), y[0], y[1]))
        elif the_subject == "Chemistry":
            for i in the_list:
                i.append(float(i[3]))
                if i[-1] < float(i[6]):
                    i.append(float(i[6]))
            return sorted(the_list, key=lambda y: (-float(y[-1]), y[0], y[1]))
        elif the_subject == "Mathematics":
            for i in the_list:
                i.append(float(i[4]))
                if i[-1] < float(i[6]):
                    i.append(float(i[6]))
            return sorted(the_list, key=lambda y: (-float(y[-1]), y[0], y[1]))
        elif the_subject == "Engineering":
            for i in the_list:
                i.append((float(i[4]) + float(i[5])) / 2)
                if i[-1] < float(i[6]):
                    i.append(float(i[6]))
            return sorted(the_list, key=lambda y: (-float(y[-1]), y[0], y[1]))
        elif the_subject == "Biotech":
            for i in the_list:
                i.append((float(i[2]) + float(i[3])) / 2)
                if i[-1] < float(i[6]):
                    i.append(float(i[6]))
            return sorted(the_list, key=lambda y: (-float(y[-1]), y[0], y[1]))
    all_subject = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
    temp_list = ppl_list
# first priority
    for i in temp_list:
        all_subject[i[7]].append(i)
    for i, j in all_subject.items():
        all_subject[i] = exam_sorting(j, i)
        all_subject[i] = all_subject[i][:limit]
    enrolled = []
    for i in all_subject.values():
        for j in i:
            enrolled.append(j)
    temp_list = [i for i in ppl_list if i not in enrolled]

# second priority
    second_intake = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
    for i in temp_list:
        second_intake[i[8]].append(i)
    for i, j in second_intake.items():
        second_intake[i] = exam_sorting(j, i)
        second_intake[i] = second_intake[i][:limit - len(all_subject[i])]
    for i in second_intake.values():
        for j in i:
            all_subject[j[8]].append(j)
            enrolled.append(j)
    temp_list = [i for i in ppl_list if i not in enrolled]
# third priority
    third_intake = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
    for i in temp_list:
        third_intake[i[9]].append(i)
    for i, j in third_intake.items():
        third_intake[i] = exam_sorting(j, i)
        third_intake[i] = third_intake[i][:limit - len(all_subject[i])]
    for i in third_intake.values():
        for j in i:
            all_subject[j[9]].append(j)
            enrolled.append(j)
    temp_list = [i for i in ppl_list if i not in enrolled]

    for i in all_subject.keys():
        all_subject[i] = sorted(all_subject[i], key=lambda y: (-float(y[-1]), y[0], y[1]))

    for i, j in all_subject.items():
        print(i)
        for k in j:
            print(" ".join(k[:2]), k[-1])
        if i != "Physics":
            print()

    for i, j in all_subject.items():
        with open(f"{i}.txt", 'w') as f:
            for k in j:
                f.write(f"{' '.join(k[:2])} {k[-1]}\n")



student_allocation(dept_limit, x)
