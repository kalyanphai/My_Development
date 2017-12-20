def pow(x,n):
  if x==0 or x==1 or n==1:
    return x
  elif x==-1:
    if n%2==0:
      return 1
    else:
      return -1
  elif n==0:
    return 1
  elif n<0:
    return 1/pow(x,-n)
  else:
    return x*pow(x, n-1)