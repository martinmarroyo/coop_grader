def check_suspect(suspect):
    guess = suspect.lower()
    murderer = "jeremy bowers"
    mastermind = "miranda priestly"
    if guess not in (murderer, mastermind):
        return(f"{suspect} is not the murderer! Keep on investigating, sleuth!")
        
    if guess == murderer:
        return(
            "Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge," 
            "try querying the interview transcript of the murderer to find the real villain behind this crime." 
            "If you feel especially confident in your SQL skills, try to complete this final step with no more than 2 queries.\n"     
            "Use this same `check_suspect` function with your new suspect to check your answer."
        )
        
    if guess == mastermind:
        return(
            "Congrats, you found the brains behind the murder!\n" 
            "Everyone in SQL City hails you as the greatest SQL detective of all time.\n" 
            "Time to break out the champagne!"
        )