score = 0

print("\n--- GENERAL KNOWLEDGE QUIZ ---")
print("Answer the following questions:\n")

# Question 1
answer1 = input("Q1: What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The answer is Paris.")

# Question 2
answer2 = input("\nQ2: How many planets are in our Solar System? ").strip().lower()
if answer2 == "8":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The answer is 8.")

# Question 3
answer3 = input("\nQ3: What is the largest ocean on Earth? ").strip().lower()
if answer3 == "pacific" or answer3 == "pacific ocean":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The answer is Pacific Ocean.")

print(f"\n--- QUIZ COMPLETE ---")
print(f"Your Final Score: {score}/3")

if score == 3:
    print("Excellent! Perfect Score!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep practicing!")
else:
    print("Better luck next time!")