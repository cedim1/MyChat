prompt = ["Hello", "hi", "bye", "bye"] #insert more prompts and responses here for it to say
print("how can I help?")
def chat():
pro = input()
numberof = prompt.index(pro)
print(prompt[numberof + 1])
chat()
return
chat()
