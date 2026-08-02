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

# [수정] 실행부: 기존의 연습용 코드를 지우고 아래 내용을 넣으세요
if __name__ == "__main__":
    # 1. JSON 파일에서 문제 불러오기
    quizzes = load_quizzes('questions.json')
    
    # 2. 잘 불러왔는지 확인 (테스트)
    print(f"총 {len(quizzes)}개의 문제를 성공적으로 불러왔습니다!")

    if quizzes:
        print(f"첫 번째 문제: {quizzes[0].question}")
        print(f"선택지: {quizzes[0].choices}")