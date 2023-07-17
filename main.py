print("--- taylor swift lyrics game - how many can you swiftly guess? ---")
print( )
print("play by filling in the blank lyrics to see how big of a swiftie you are! (or how much we used to be depressed")
print( )
print("the closer to 0, means the higher you rank on the swiftie mountain ladder")
print( )
print( )
print("-- lets gooo (round 1) --")
print( )
count = 0
while True:
  print("those ____ peaks look like a perfect place to cry")
  count +=1 
  answer = input("answer: ")
  if answer == "windermere":
    break
  else:
    print("nope, go again")
    print( )
print( )
print("you got", count, "points")
print( )
input("ready for round 2? ")
print( )
print("round 2!!")
count2 = 0
while True:
  print("i looked around in a ____-soaked gown")
  count2 +=1
  answer = input("answer is :")
  if answer == "blood":
    break
  else:
    print("nope, go again")
    print( )
print( )
print("you got", (count + count2), "points")

  
