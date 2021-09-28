def solution(lst):
  dic = {}
  answer = []
  for i in lst:
    if i not in dic:
      dic[i] = 1
    else:
      dic[i] += 1
      dic = sorted(dic.items(), key=lambda x:x[1], reverse = True )
  for i in range(len(dic)):
    if dic[i][1] > 1:
      answer.append(dic[i][0])

  return answer
