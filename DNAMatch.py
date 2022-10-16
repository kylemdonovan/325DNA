def dna_match_topdown(DNA1, DNA2):

    LDNA1 = len(DNA1)
    LDNA2 = len(DNA2)

    cache = [[-1 for _ in range(LDNA1+1)] for _ in range(LDNA2+1)]
    result = top_help(DNA1, DNA2, LDNA1, LDNA2, cache)
    return result

def top_help(DNA1, DNA2, LDNA1, LDNA2, cache):
    if (LDNA1 == 0 or LDNA2 == 0):
        return 0

    if (cache[LDNA1][LDNA2] != -1):
        return cache[LDNA1][LDNA2]

    if DNA1[LDNA1 - 1] == DNA2[LDNA2 - 1]:
        cache[LDNA1][LDNA2] = 1 + top_help(DNA1, DNA2, LDNA1 - 1, LDNA2 - 1, cache)
        return cache[LDNA1][LDNA2]

    cache[LDNA1][LDNA2] = max(top_help(DNA1, DNA2, LDNA1, LDNA2 - 1, cache), top_help(DNA1, DNA2, LDNA1 - 1, LDNA2, cache))
    return cache[LDNA1][LDNA2]













def dna_match_bottomup(str1, str2):
    pass
#
#     m = len(str1)
#     n = len(str2)
#
#     cache = [[0 for x in range(n+1)] for x in range(m + 1)]
#
#     for i in range(m + 1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 cache[i][j] = 0
#             elif str1[i-1] == str2[j-1]:
#                 cache[i][j] = cache[i-1][j-1] + 1
#             else:
#                 cache[i][j] = max(cache[i-1][j] , cache[i][j-1])
#
#     return cache[m][n]
#
# if __name__ == '__main__':
#     DNA1 = "ATAGTTCCGTCAAA"
#     DNA2 = "GTGTTCCCGTCAAA"
#     print(dna_match_topdown(DNA1, DNA2))
#     print(dna_match_bottomup(DNA1, DNA2))
#











# def dna_match_topdown(DNA1, DNA2):
#     matches = {}
#     if DNA1 == 0:
#         return 1
#     elif DNA1 == 1:
#         return 1
#     else:
#         length1 = len(DNA1)
#         length2 = len(DNA2)
#         counter1 = 0
#         counter2 = 0
#
#         for item in DNA1:
#             if DNA1[counter1] == DNA2[counter2]:
#                 newVar = DNA1[counter1]
#                 matches[item] = newVar
#                 counter2 += 1
#                 print("Items ", DNA1[counter1], " and ", DNA2[counter2], " matched!")
#             if DNA1[counter1] != DNA2[counter2]:
#                 print("Items ", DNA1[counter1], " and ", DNA2[counter2], " did not match this time but we will keep trying!")
#
#
#             if counter2 == length2 and counter1 != length1:
#                 counter1 = 0
#                 print("We get to the counter2 check and counter 1 anti check")
#
#             if counter1 == counter1 and counter2 == length2:
#                 print("DUCKFART")
#                 print(matches)
#                 return
#             #this will need to switch to return matches later
#
#         print(matches)
#
# dna = [1,2,3]
# dna2 = [2,3,4]
# dna_match_topdown(dna, dna2)
