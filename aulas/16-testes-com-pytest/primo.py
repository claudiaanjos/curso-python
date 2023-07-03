def primo(numb):
  if numb > 1:
    for i in range(2,numb):
      if (numb % i ) == 0:
        return False
    return True
  else:
    return False