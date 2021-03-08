grades=[[10,23,34,67],[66],[45,78,90]]
grades[1].append(70)
# print(grades)
# for inner_list in grades:
#     print(inner_list)

# for i in range(len(grades)):
#     for j in range(len(grades[i])):
#         print(grades[i][j],end=" ")
#     print()

print(sorted(grades))

def print_2d(grades):
    for inner_list in grades:
        for grade in inner_list:
            print(grade,end=" ")
        print()

print_2d(grades)

