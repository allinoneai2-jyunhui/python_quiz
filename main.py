import json
import os

class QuizManager:
    def __init__(self, file_path="state.json"):
        self.file_path = file_path
        self.quizzes = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.quizzes = data
                else:
                    self.quizzes = {"대한민국": [], "미국": [], "중국": []}
        else:
            self.quizzes = {"대한민국": [], "미국": [], "중국": []}
            self.save_data()


    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.quizzes, f, indent=4, ensure_ascii=False)

    # 이 메서드가 반드시 있어야 합니다!
    def get_topics(self):
        return list(self.quizzes.keys())





class QuizGame:
    def __init__(self, manager):
        self.manager = manager
        self.score = 0

    def play(self):
        topics = self.manager.get_topics()
        if not topics:
            print("등록된 주제가 없습니다.")
            return

        print("\n주제를 선택하세요:")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")
        
        try:
            choice = int(input("번호 입력: ")) - 1
            selected_topic = topics[choice]
        except (ValueError, IndexError):
            print("잘못된 입력입니다.")
            return
        
        # 문제 리스트 가져오기
        questions = self.manager.quizzes.get(selected_topic, [])
        
        if not questions:
            print(f"[{selected_topic}] 주제에 등록된 문제가 없습니다. 퀴즈 추가 메뉴에서 문제를 먼저 등록해 주세요!")
            return
        
        print(f"\n[{selected_topic}] 퀴즈 시작! (그만하려면 0 입력)")
        for q in questions:
            while True:
                user_input = input(f"{q['question']} ")
                if user_input == "0":
                    print(f"종료합니다. 최종 점수: {self.score}점")
                    return
                if user_input == q['answer']:
                    print("정답입니다!")
                    self.score += 10
                    break
                else:
                    print("틀렸습니다. 다시 시도하세요.")

    def add_quiz(self):
        topics = self.manager.get_topics()
        print("\n--- 주제 선택 ---")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")
        
        try:
            choice = int(input("번호 입력: ")) - 1
            if 0 <= choice < len(topics):
                topic = topics[choice]
                question = input("문제: ")
                answer = input("정답: ")
                self.manager.quizzes[topic].append({"question": question, "answer": answer})
                self.manager.save_data()
                print(f"[{topic}]에 퀴즈가 추가되었습니다!")
            else:
                print("잘못된 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

def main():
    mgr = QuizManager()
    game = QuizGame(mgr)

    while True:
        print("\n--- 퀴즈 프로그램 ---")
        print("1. 퀴즈 풀기 | 2. 퀴즈 추가 | 3. 점수 확인 | 4. 종료")
        choice = input("선택: ")

        if choice == '1':
            game.play()
        elif choice == '2':
            game.add_quiz()
        elif choice == '3':
            print(f"\n현재 점수: {game.score}점")
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()