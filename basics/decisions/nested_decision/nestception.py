def run():
  #asking where to look
  print("Where should I look for the doctor")
  wherelook = input()
  #if tardis
  if wherelook == 'tardis':
    print("Where in the tardis should I look?")
    wheretardis = input()
    if wheretardis == 'console room':
      print("ahh there he is")
    else:
      print("I cant see him there")
  #if gallifrey
  elif wherelook == 'gallifrey':
    print("where abouts on gallifrey? it is rather large you know")
    wheregallifrey = input()
    if wheregallifrey == 'panopticon':
      print("There he is, nice work")
    else:
      print("no he isn't there sadly")
  #if scaro
  elif wherelook == 'scaro':
    print("scaro!!! oh dear, but where abouts?")
    wherescaro = input()
    if wherescaro == 'bunker':
      print("He is there but he had better get the heck out of there!")
    else:
      print("nowhere is safe on scaro, but I can't see him so that's good!")
  #else
  else:
    print("well, he's  not there and i don't know where else to look")


