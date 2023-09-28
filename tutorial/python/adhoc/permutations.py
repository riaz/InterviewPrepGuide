
def permutations(string):
  # your code goes here
  res = []

  def get_permute(prefix, rest):
    """
    This function takes the prefix applies a loop on rest
    and created a combination , recursively called get_permute on the rest.
    """
    if not rest:
      res.append(prefix)
    else:
      for i in range(len(rest)):
        prep_res = rest[:i]
        if i != len(rest) - 1:
          prep_res += rest[i+1:]
        
        get_permute(prefix + rest[i], prep_res)
  
  get_permute('', string)

  print(res)

  return res

if __name__ == '__main__':
  str_value = "abcd"
  permutations(str_value)