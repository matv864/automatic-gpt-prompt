
from src.chatgpt import ChatGPT



chatgpt = ChatGPT()
chatgpt.create_new_chat()
chatgpt.enter_prompt("please say word 'cat'")
print(chatgpt.get_result_from_prompt())
chatgpt.enter_prompt("please say word 'dog'")
print(chatgpt.get_result_from_prompt())