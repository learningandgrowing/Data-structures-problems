per = float(input())
def grade():
    if per>=91 and per <= 100:
        print('grade is A')
    elif per>= 81 and per<= 90:
        print('grade is B')
    elif per>= 71 and per<= 80:
        print('grade is C')
    elif per>= 61 and per<= 70:
        print('grade is D')
    elif per>= 51 and per <= 60:
        print('grade is E')
    else:
        print('Fail')
if __name__ == "__main__":
    grade()

