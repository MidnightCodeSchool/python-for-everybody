# ให้เขียนเกม rock paper scissor
# เก็บคะแนนของผู้เล่น
score = 0
# ผู้เล่นใส่ค่าที่เลือกมาได้
player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
# เล่นเกมตามรอบ
game_choice = 'scissor'
if player_choice == game_choice:
    print("เสมอ")
elif player_choice == 'rock':
    print("ชนะ")
    score += 1  # score = score + 1
elif player_choice == 'paper':
    print("แพ้")
player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
game_choice = 'rock'
if player_choice == game_choice:
    print("เสมอ")
elif player_choice == 'rock':
    print("ชนะ")
    score += 1  # score = score + 1
elif player_choice == 'paper':
    print("แพ้")
player_choice = input("ออกอะไร​? (rock, paper, scissor): ")
game_choice = 'paper'
if player_choice == game_choice:
    print("เสมอ")
elif player_choice == 'rock':
    print("ชนะ")
    score += 1  # score = score + 1
elif player_choice == 'paper':
    print("แพ้")

# แสดงผลคะแนน
print("คะแนนของคุณคือ", score)