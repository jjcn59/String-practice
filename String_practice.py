import re
####
def get_number(str):
  sl = re.findall("\d+.?\d*", str)
  s =''.join(sl) 
  if('.' in s):
    r = s.split('.')[1][:2]
    if(len(r) == 0):
      print(s + '00')
    elif(len(r) == 1):
       print(s + '0')
    else:
      print(s). 
  else:
    print(s + '00')

if __name__=='__main__':
  get_number('abc123')


