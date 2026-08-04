import json

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

def load_quizzes(filename):
    # 파일 읽기 예외 처리 추가
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Quiz(q['question'], q['choices'], q['answer']) for q in data]
    except FileNotFoundError:
        print(f"❌ 오류: {filename} 파일을 찾을 수 없습니다.")
        return []

def main():
    quiz_list = load_quizzes('state.json') 
    
    if not quiz_list:
        return

    score = 0
    print("=== 파이썬 퀴즈 게임을 시작합니다! ===")

    for i, quiz in enumerate(quiz_list, 1):
        print(f"\n문제 {i}. {quiz.question}")
        for idx, choice in enumerate(quiz.choices, 1):
            print(f"{idx}) {choice}")

        # --- 05단계: 예외 처리 입력 로직 ---
        while True:
            user_input = input("정답 번호를 입력하세요 (1-4): ").strip()
            
            # 1. 숫자인지 확인
            if not user_input.isdigit():
                print("❌ 숫자만 입력할 수 있습니다. 다시 입력해주세요.")
                continue
            
            user_answer = int(user_input)
            
            # 2. 범위가 1~4 사이인지 확인
            if 1 <= user_answer <= 4:
                break # 올바른 입력이면 반복문 탈출
            else:
                print("❌ 1번부터 4번 사이의 숫자를 입력해주세요.")
        # ----------------------------------

        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

    print(f"\n=== 게임 종료! ===")
    print(f"당신의 점수: {score} / {len(quiz_list)}")

if __name__ == "__main__":
    main()