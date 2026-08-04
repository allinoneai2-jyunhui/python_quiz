import json
import random
import datetime

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_input):
        return user_input == self.answer

def load_quizzes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            quizzes = []
            for q in data:
                # 'options'가 없으면 'choices'를 찾아보고, 그것도 없으면 기본값 빈 리스트
                options = q.get('options') or q.get('choices')
                if options is None:
                    print(f"⚠️ 경고: '{q.get('question')}' 문제에 선택지(options)가 없습니다.")
                    continue
                quizzes.append(Quiz(q['question'], options, q['answer']))
            return quizzes
    except FileNotFoundError:
        print("❌ 에러: state.json 파일을 찾을 수 없습니다.")
        return []
    except json.JSONDecodeError:
        print("❌ 에러: JSON 파일 형식이 잘못되었습니다.")
        return []

# ... (기존 Quiz 클래스와 load_quizzes 함수) ...

def save_score(name, score):
    """플레이어의 기록을 파일에 저장합니다."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {name}: {score}점\n")
    print(f"\n✅ {name}님의 기록이 저장되었습니다!")


def play_game():
    quizzes = load_quizzes('state.json')
    if not quizzes:
        print("❌ 불러올 퀴즈가 없습니다. state.json 파일을 확인해주세요.")
        return

    random.shuffle(quizzes)
    
    score = 0
    total = len(quizzes)

    print("🎮 파이썬 퀴즈 게임을 시작합니다!")
    print("-" * 30)

    for idx, quiz in enumerate(quizzes, 1):
        print(f"\nQ{idx}. {quiz.question}")
        for i, option in enumerate(quiz.options, 1):
            print(f"  {i}) {option}")
        
        while True:
            try:
                user_input = input("정답 번호를 입력하세요 (1-4): ").strip()
                if not user_input: continue # 빈 입력 방지
                choice = int(user_input)
                
                if 1 <= choice <= 4:
                    break
                else:
                    print("⚠️  1에서 4 사이의 숫자만 입력해주세요.")
            except ValueError:
                print("⚠️  숫자가 아닙니다. 숫자(1, 2, 3, 4)를 입력해주세요.")

        if quiz.check_answer(choice):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

    print("-" * 30)
    print(f"결과: {total}문제 중 {score}문제를 맞혔습니다!")
    print("게임을 종료합니다. 수고하셨습니다! ")
    player_name = input("기록을 남길 이름을 입력하세요: ")
    save_score(player_name, score)

if __name__ == "__main__":
    play_game()