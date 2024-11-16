def get_letter_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid Score'

def main():
    print("Enter your scores between 0 and 100. Enter -1 to quit.")
    while True:
        score = int(input("Enter score: "))
        if score == -1:
            break
        grade = get_letter_grade(score)
        print(f"Score: {score}, Grade: {grade}")

if __name__ == "__main__":
    main()
