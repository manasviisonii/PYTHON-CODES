#Write a lambda function to find min max from a list


def min_max(list_b):
  l=len(list_b)
  n=1
  min=list_b[0]
  max=list_b[0]
  for i in range(list_b[0],list_b[l-1]):
    if min<=list_b[n]:
      n+=1
    else :
      min=list_b[n]
    if max>=list_b[n]:
      n+=1
    else:
      max=list_b[n]
  print(min)
  print(max)



list_a=[10,6,8,12,3,11]
min_max(list_a)

     
