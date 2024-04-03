sec_num =5
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count += 1
    if guess == sec_num:
        print("correct")
        break
    else: 
        print("sorry u failed")