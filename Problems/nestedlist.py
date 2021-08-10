n = int(input())

ls = []
score_list = []
final_name = []; sort_name_list = []

# In this code we are adding list of name and score
for i in range(n):
    t = []
    name = input()
    score = float(input())
    t = [name, score]
    score_list.append(score)
    ls.append(t)

# sorting score list element in ascending order
for i in range(len(score_list)):
    for j in range(i+1, len(score_list)):
        if score_list[i] > score_list[j]:
            t = score_list[i]
            score_list[i] = score_list[j]
            score_list[j] = t

# finding second least element from the score list
second_least = score_list[1]
for i in range(2, len(score_list)):
    if second_least == score_list[0]:
        second_least = score_list[i]

# Adding name that satisfies our condition
for l in ls:
    if second_least == l[1]:
        final_name.append(l[0])

# sorting the final name list in alphabetical order
final_name.sort()
# alternate method to do sorting
# for i in range(len(final_name)):
#     for j in range(i+1, len(final_name)):
#         if final_name[i]>final_name[j]:
#             t = final_name[i]
#             final_name[i] = final_name[j]
#             final_name[j] = t
#     sort_name_list.append(final_name[i])

# print name from the final list
for name in final_name:
    print(name)




