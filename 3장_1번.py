a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

"""
맴버연산자 in, not in은 
왼쪽 요소가 오른쪽 요소 안에 있는지를 판별한다.
in은 안에 포함될시 참, 아니면 거짓을 반환하며, not in은 반대로 반환한다.
그리고 중간의 and 연산자는 c언어의 &&과 같다. (왼쪽 논리와 오른쪽 논리가 모두 참일경우 참을 반환)
"""