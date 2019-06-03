# queue_number = [2, 3, 14, 34, 45, 56, 67, 69, 80, 120]
# for number in queue_number:
#     print(number + 1)


# keyboard_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
# for row in keyboard_row:
#     print(row)



my_school = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [2,2,4,2,2]},
    {'school_class': '4c', 'scores': [5,4,4,5,5]},
    {'school_class': '4a', 'scores': [4,4,4,4,5]}
]
per_school = 0
for school in my_school:
    per_class = sum(school['scores'])/len(school['scores']) 
    per_school = per_school + sum(school['scores'])/len(school['scores'])
    print(per_class)
    
print(per_school/len(my_school))


# faq = {
#         "How are you": "Fine!",
#         "What are you doing?": "Coding",
#         "Nothing to add?": "Nope"
# }

# def get_answer(question,faq):
#     try:
#         input(faq.get(question))
#     except (KeyboardInterrupt):
#         return 'dont let me down'

# def ask_user(faq):
#     while True:
#         user_input = input("Tell me sth: ")
#         answer = get_answer(user_input, faq)
#         print(answer)

#         if user_input == "Bye, boy":
#             break 
    
# ask_user(faq)