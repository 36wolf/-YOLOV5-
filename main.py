import ollama
import requests
import pyttsx3
import re
https_= "127.0.0.1：11434"
class Solution:
    def message(self,problem):
        host="127.0.0.1"
        port="11434"
        url = f"http://{host}:{port}/api/chat"
        model = "deepseek-r1:7b"
        headers = {"Content-Type": "application/json"}
        data = {
                "model": model, #模型选择
                "options": {
                    "temperature": 0.,
                    "num_ctx": 8192#为0表示不让模型自由发挥，输出结果相对较固定，>0的话，输出的结果会比较放飞自我
                 },
                "stream": False, #流式输出
                "messages": [{
                    "role": "system",
                    "content":problem
                }] #对话列表
            }
        response=requests.post(url,json=data,headers=headers,timeout=60)
        res=response.json()
        var = res['message']['content']
        return var
    def message_ollama(self,problem):
        res = ollama.chat(model="deepseek-r1:7b", stream=False, messages=[{"role": "user", "content": problem}],
                          options={"temperature": 0})
        print(res['message']['content'], end='', flush=True)
        print("\n")


    def use_pyttsx3(self,word):
        # 创建对象
        engine = pyttsx3.init()
        # 获取当前语音速率
        rate = engine.getProperty('rate')
        # print(f'语音速率：{rate}')
        # 设置新的语音速率
        engine.setProperty('rate', 200)
        # 获取当前语音音量
        volume = engine.getProperty('volume')
        # print(f'语音音量：{volume}')
        # 设置新的语音音量，音量最小为 0，最大为 1
        engine.setProperty('volume', 1.0)
        # 获取当前语音声音的详细信息
        voices = engine.getProperty('voices')
        # print(f'语音声音详细信息：{voices}')
        # 设置当前语音声音为女性，当前声音不能读中文
        engine.setProperty('voice', voices[1].id)
        # 设置当前语音声音为男性，当前声音可以读中文
        engine.setProperty('voice', voices[0].id)
        # 获取当前语音声音
        voice = engine.getProperty('voice')
        # print(f'语音声音：{voice}')
        # 语音文本
        # path = 'test.txt'
        # with open(path, encoding='utf-8') as f_name:
        #     words = str(f_name.readlines()).replace(r'\n', '')
        # 将语音文本说出来
        engine.say(word)
        engine.runAndWait()
        engine.stop()
    def chat_with_ollama(self):
        # 初始化一个列表来存储对话历史，每个元素是一个包含用户输入和模型回复的元组
        history = []
        while True:
            # 获取用户输入，并转换为小写，方便后续判断退出条件
            user_input = input("\nUser: ")
            # 判断用户是否想要退出对话
            if user_input.lower() in ["exit", "quit", "stop", "baibai", "拜拜"]:
                break

            # 将用户输入和一个空字符串（用于后续存储模型回复）作为元组添加到历史记录中
            history.append([user_input, ""])

            # 初始化一个列表来存储整理后的对话消息，用于请求模型生成回复
            messages = []
            # 遍历历史记录，整理对话消息
            for idx, (user_msg, model_msg) in enumerate(history):
                # 如果当前对话为最新的一条且未收到模型回复，则只添加用户消息
                if idx == len(history) - 1 and not model_msg:
                    messages.append({"role": "user", "content": user_msg})
                    break
                # 如果是用户消息，则添加到消息列表中
                if user_msg:
                    messages.append({"role": "user", "content": user_msg})
                # 如果是模型回复，则添加到消息列表中
                if model_msg:
                    messages.append({"role": "assistant", "content": model_msg})

            # 调用模型生成回复
            output = ollama.chat(
                model="deepseek-r1:7b",
                messages=messages
            )
            print('模型回复:', output['message']['content'])
            word = str(output['message']['content'])
            word = word.replace("<think>", "")
            word = word.replace("</think>", "")
            word = word.replace('\n', "")
            w = [word]
            s1.use_pyttsx3(w)
            # 写一首诗
            # print(w) #字符串
            # 更新history中最新用户输入的模型回复
            history[-1][1] = output['message']['content']


s1 = Solution()


s1.chat_with_ollama()

# while(1):
#     problem = input("请输入问题：")
#     if problem == '':
#         break
#     else:
#         word = s1.message(problem)
#         print(word)
#         word = str(word)
#         word = word.replace("<think>","")
#         word = word.replace("</think>","")
#         word = word.replace('\n', "")
#         w = [word]
#         #写一首诗
#         # print(w) #字符串
#         s1.use_pyttsx3(w)
#         # answer = s1.message(problem)
#         # print(answer)


