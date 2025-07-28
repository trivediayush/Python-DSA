age = 17
voter_id = True

if age > 18:
    if voter_id == True:
        print("You can vote with your ID.")
    else:
        print("You need a voter ID to vote.")
else:
    print("You cannot vote yet.")