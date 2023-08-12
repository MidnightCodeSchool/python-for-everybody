import random

# # ให้เขียนเกม rock paper scissor
def play_rsp(player_choice, game_choice):
    """
    เล่นเกม rock paper scissor
    function จะดูว่าค่าที่ให้เข้ามาชนะ เสมอ หรือแพ้
    จากนั้นพิมพ์ผลลัพธ์ออกมา
    ถ้าชนะ จะคืนค่า 1
    ถ้าเสมอ จะคืนค่า 0
    ถ้าแพ้ จะคืนค่า -1
    """
    if player_choice == game_choice:
        print("เสมอ")
        return 0
    elif player_choice == 'rock' and game_choice == 'scissor':
        print("ชนะ")
        return 1
    elif player_choice == 'rock' and game_choice == 'paper':
        print("แพ้")
        return -1
    elif player_choice == 'paper' and game_choice == 'rock':
        print("ชนะ")
        return 1
    elif player_choice == 'paper' and game_choice == 'scissor':
        print("แพ้")
        return -1
    elif player_choice == 'scissor' and game_choice == 'paper':
        print("ชนะ")
        return 1
    elif player_choice == 'scissor' and game_choice == 'rock':
        print("แพ้")
        return -1
    print("ลืม handle กรณี :", player_choice, game_choice)


GAME_CHOICES = ['rock', 'paper', 'scissor']
# เก็บคะแนนของผู้เล่น
score = 0
# ผู้เล่นใส่ค่าที่เลือกมาได้
# เล่นเกมตามรอบ
for _ in GAME_CHOICES:
    game_choice = random.choice(GAME_CHOICES)
    print('===', game_choice)
    player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
    round_score = play_rsp(player_choice, game_choice)
    score += round_score  # score = score + round_score
# # แสดงผลคะแนน
print("คะแนนของคุณคือ", score)
if score >= 2:
    print("ชนะ")
elif score < 2:
    print("แพ้")
