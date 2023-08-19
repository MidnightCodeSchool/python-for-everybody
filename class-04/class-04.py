from rich import print
# back to string
some_string = "Hello World"
some_more_string = 'Hello World!'
long_string = """HELLO
Hello World
LONG!
"""
string_with_newline = "Hello\nWorld"
single_quote_string = 'John\'s cat'
double_quote_string = "John's cat"
more_double_quote_string = "John said \"Hello\""
# \t: tab, \n: newline
# string เป็น list-like
my_new_string = "Hello World1234"
print(my_new_string[0])
print(my_new_string[1])
print(my_new_string[2])
for character in my_new_string:
    print(character)
my_new_string[0:5]
my_new_string[:5]
my_new_string[-1]  # ตัวสุดท้าย
my_new_string[5:]
"hello" in my_new_string
"Hello" in my_new_string
"Hello" + "World"
# f-string
name = "John"
age = 20
f"Hello {name}, you are {age} years old"  # อะไรที่แปลงเป็น text ได้ใช้ได้ทั้งหมด
f"Hello {name}, next year I will be {age + 1} years old"
symbol = "BTC"
price = 1000000.12323456234523452345
f"Symbol: {symbol}, Price: {price:.2f}"  # format float

# methods
some_new_string = "heLlo worLd"
my_new_string.upper()
my_new_string.lower()
my_new_string.capitalize()
my_new_string.isupper() # ทุกตัวเป็นตัวใหญ่หรือไม่
my_new_string.islower() # ทุกตัวเป็นตัวเล็กหรือไม่

# heLlo worLd -> HELLO WORLD -> True
my_new_string.upper().isupper()  # การ chain method

# basic check
all_alphabets = "abcdefghijklmnopqrstuvwxyz"
all_nums = "0123456789"
all_alphabets.isalpha()
all_alphabets.isnumeric()
all_nums.isnumeric()
all_alphabets.isnumeric()
new_string = all_alphabets + all_nums
new_string.isalnum()  # เป็นอักษรหรือตัวเลข

#เริ่มด้วย ลงท้ายด้วย แยกคำ
hashtags = "#python #programming #coding $cat $dog"
claned_hashtags = []
for hashtag in hashtags.split():
    if hashtag.startswith("#"):
        print(hashtag)
        claned_hashtags.append(hashtag)
claned_hashtags

hello_in_other_lang = "HOLA!"
hello_in_other_lang.endswith("!")

# split string ได้ list
"Hello World".split()
"#python, #java, #c++".split(", ")

# join list ได้ string
list_of_hashtags = ["#python", "#java", "#c++"]
", ".join(list_of_hashtags)

# stripping
'    Hello, World    '.strip()
'    Hello, World    '.lstrip()
'    Hello, World    '.rstrip()