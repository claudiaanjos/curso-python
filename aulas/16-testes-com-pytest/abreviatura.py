def abreviatura(nome):
  s = nome.split()
  iniciais = ""
  for i in s:
    iniciais += i[0].upper()
  return iniciais