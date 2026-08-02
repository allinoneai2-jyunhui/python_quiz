import json

# [유지] 02단계에서 만든 클래스 구조
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 혹시 지난번에 만들었던 to_dict가 있다면 남겨둬도 좋고, 없어도 지금은 괜찮아요!
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

# [추가] JSON 파일을 읽어서 Quiz 객체 리스트로 만드는 함수
def load_quizzes(filename):
    quiz_list = []
    try:
        # 파일을 읽기 모드('r')로 열기
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file) # JSON 파일 내용을 파이썬 리스트/딕셔너리로 변환
            for item in data:
                # 읽어온 데이터를 Quiz 클래스의 인스턴스로 생성
                quiz = Quiz(item['question'], item['choices'], item['answer'])
                quiz_list.append(quiz)
    except FileNotFoundError:
        print(f"에러: {filename} 파일을 찾을 수 없습니다.")
    
    return quiz_list

def run_quiz(quiz_list):
    score = 0  # 점수 초기화
    
    print(f"\n총 {len(quiz_list)}문제를 시작합니다!")
    
    for i, quiz in enumerate(quiz_list):
        print(f"\n문제 {i+1}: {quiz.question}")
        # 보기 출력
        for idx, choice in enumerate(quiz.choices):
            print(f"{idx+1}. {choice}")
        
        # 사용자 입력 받기
        user_answer = input("정답 번호를 입력하세요: ")
        
        # 정답 확인 (JSON의 answer는 숫자이므로 문자열로 변환해 비교)
        if user_answer == str(quiz.answer):
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"틀렸습니다. 😢 정답은 {quiz.answer}번입니다.")
            
    print(f"\n--- 게임 종료! ---")
    print(f"당신의 최종 점수: {score} / {len(quiz_list)}")



# [수정] 실행부: 기존의 연습용 코드를 지우고 아래 내용을 넣으세요
if __name__ == "__main__":
    # 1. JSON 파일에서 문제 불러오기
    quizzes = load_quizzes('questions.json')
    
    # 2. 문제가 정상적으로 로드되었는지 확인 후 게임 시작
    if quizzes:
        print(f"총 {len(quizzes)}개의 문제를 성공적으로 불러왔습니다!")
        run_quiz(quizzes)  # <--- 이 부분이 있어야 게임이 시작됩니다!
    else:
        print("문제를 불러오지 못했습니다. questions.json 파일을 확인해주세요.")