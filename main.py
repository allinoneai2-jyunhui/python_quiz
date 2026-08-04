import json
import random

class Quiz:
    # 클래스는 한 문제의 정보를 담도록 설계합니다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_ans):
        return user_ans == self.answer

def run_quiz():
    # 1. 파일에서 퀴즈 데이터 불러오기
    try:
        with open('state.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("퀴즈 파일을 찾을 수 없습니다.")
        return

    # 2. 데이터로부터 Quiz 객체 리스트 생성
    quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data]
    
    # [핵심!] 07단계: 문제 리스트를 랜덤하게 섞습니다.
    random.shuffle(quizzes)
    
    score = 0 
    total = len(quizzes)

    print("--- 퀴즈를 시작합니다! ---")

    for i, quiz in enumerate(quizzes, 1):
        print(f"\n문제 {i}: {quiz.question}")
        for idx, choice in enumerate(quiz.choices, 1):
            print(f"{idx}. {choice}")

        while True:
            try:
                user_ans = int(input("정답 번호를 입력하세요 (1-4): "))
                if 1 <= user_ans <= 4:
                    break
                else:
                    print("1에서 4 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("숫자만 입력 가능합니다.")

        if quiz.check_answer(user_ans):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

    print("\n" + "="*30)
    print("      퀴즈 종료!      ")
    print(f"  최종 점수: {score} / {total}")
    print(f"  정답률: {(score/total)*100:.1f}%")
    print("="*30)
    
    if score == total:
        print("🎉 만점입니다! 대단해요!")
    elif score >= total // 2:
        print("👍 잘하셨어요! 조금만 더 하면 만점이에요.")
    else:
        print("📚 복습이 조금 필요할 것 같아요. 화이팅!")

if __name__ == "__main__":
    run_quiz()