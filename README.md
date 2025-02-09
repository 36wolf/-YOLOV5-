

# DeepSeek-Chat

[![GitHub license](https://img.shields.io/github/license/yourusername/deepseek-chat)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/deepseek-chat)](https://pypi.org/project/deepseek-chat)

一个基于本地部署的 DeepSeek 模型实现的智能对话机器人，支持记忆功能、循环对话和语音输出。

## 特性

- **本地运行**：直接调用本地部署的 DeepSeek 模型，无需依赖云服务。
- **记忆功能**：能够记住之前的对话内容，保持上下文连贯。
- **循环对话**：支持持续对话模式，可以进行多轮交互。
- **语音输出**：集成语音合成技术，支持将对话内容转换为语音输出。

## 项目简介

`DeepSeek-Chat` 是一个 Python 库，旨在提供一个简单易用的接口来调用本地部署的 DeepSeek 模型，并通过记忆功能和循环对话实现智能化交互。此外，该项目还集成了语音合成功能，支持将对话内容以语音形式输出。

## 快速上手

### 安装依赖

```bash
pip install deepseek-chat pydub edge-tts
```

### 下载模型（可选）

根据 DeepSeek 模型的要求下载并配置本地模型文件。

### 示例代码

```python
from deepseek_chat import DeepSeekChat

# 初始化对话机器人
chat = DeepSeekChat(memory=True)

# 开始循环对话
while True:
    user_input = input("你：")
    if user_input == "退出":
        break
    response = chat.chat(user_input)
    print(f"AI：{response}")
    # 调用语音输出模块播放响应内容（可选）
    chat.tts_speak(response)
```

## 实现细节

### 加载模型

```python
from deepseek_chat.models import DeepSeekModel

# 加载本地 DeepSeek 模型
model = DeepSeekModel(
    model_path="path/to/deepseek/model",
    device="cpu"  # 或者 "cuda" 如果使用 GPU
)
```

### 对话管理

```python
from deepseek_chat.conversation import ConversationManager

# 初始化对话管理器（支持记忆功能）
manager = ConversationManager(memory=True)

# 添加对话内容
manager.add_message("用户：你好！")
manager.add_message("AI：你好！很高兴见到你。")

# 获取完整的对话历史
print(manager.get_messages())
```

### 语音输出

```python
from deepseek_chat.tts import TTSProcessor

# 初始化语音处理器（支持多种语音合成工具）
processor = TTSProcessor(engine="edge-tts")  # 或者 "pyttsx3"

# 将文本转换为语音并播放
processor.speak("这是 DeepSeek-Chat 的语音输出功能。")
```

## 示例

以下是一个完整的示例，展示如何使用 `DeepSeek-Chat` 进行循环对话：

```python
from deepseek_chat import DeepSeekChat

# 初始化聊天机器人（支持记忆和语音输出）
chat = DeepSeekChat(memory=True, enable_voice=True)

# 开始对话循环
while True:
    try:
        user_input = input("你：")
        if user_input.strip() == "退出":
            break
        response = chat.chat(user_input)
        print(f"AI：{response}")
        # 调用语音输出模块播放响应内容（可选）
        chat.tts_speak(response)
    except KeyboardInterrupt:
        print("\n对话已终止。")
        break
```

## 支持的模型

- DeepSeek 默认模型
- 其他兼容接口的模型

## LICENSE

[MIT License](LICENSE)

---
