import random


my_text = "Швидка коричнева лисиця стрибнула через ледачого собаку"
text_list = my_text.split(' ')
my_new_list = []
while len(text_list)!=0:
    random_index = random.randint(0,len(text_list)-1)
    word = text_list[random_index]
    text_list.pop(random_index)
    my_new_list.append(word)
print(my_new_list)