import json
import random
from tqdm import tqdm
from IPython.display import display, Markdown, Image

# 請確保使用正確的檔路徑
json_file_path = "C:\\Users\\USER\\Desktop\\EXAM\\AWSMLP_QuestionBank.json"

# 使用UTF-8編碼讀取JSON檔
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

PRACTICE_MODE = False
correct = 0
total_questions = 4  # 根據你的JSON資料中的題目數量設置

# 隨機選擇題目數量（這裡設置為總題數，因為total_questions應小於等於實際題數）
questions = random.sample(data["Questions"], total_questions)

for idx, question in enumerate(tqdm(questions)):
    display(Markdown(f"<h3>{question['question']}</h3>"))

    # 檢查並顯示所有圖片
    if 'images' in question and question['images']:
        for image in question['images']:
            if image.strip():  # 如果圖片路徑不為空
                display(Image(filename=image))

    # 初始化選項清單
    options_with_letters = []

    # 顯示選項，並添加到選項清單
    for i, option in enumerate(question["options"], start=1):
        option_letter = f"{chr(64+i)}"  # 將數位1, 2, 3, 4轉換為A, B, C, D
        display(Markdown(f"<h4>{option_letter}. {option}</h4>"))
        options_with_letters.append((option_letter, option))

    # 提示用戶輸入答案
    my_answer = input("Enter your answer (A, B, C, or D) or type 'q' to end the quiz: ").strip().upper()

    # 如果用戶選擇退出
    if my_answer == 'Q':
        break

    # 檢查用戶答案是否正確
    if (my_answer, question["answer"]) in options_with_letters:
        correct += 1
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is: {question['answer']}")

    if PRACTICE_MODE:
        print("\n---")
        my_key = input("Press Enter to continue or type 'q' to quit:")
        if my_key.lower() == 'q':
            break

# 顯示最終得分
print(f"You answered {idx + 1} questions and got {correct} correct. Score: {(correct / (idx + 1)) * 100:.2f}%")

