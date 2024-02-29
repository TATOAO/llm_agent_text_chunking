
from os import write
import time
from openai import OpenAI
from collections import deque

client = OpenAI(api_key="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")

system_prompt = """ 
请你充当一个关于保险的专家，我会不停的给你一些文字的片段，现在我需要你帮我做一些笔记。这些文字每次都会以['文字', '文字2'] 这样的形式给你。你每次都需要把之前全部的笔记打印出来。 如果你觉得你记录的知识点是有层级关系的，请用 
1. 知识点1
1.1. 子知识点1
1.2. 子知识点2

这样的小标题表示出来。

注意: 你不需要回答关于我给你的知识点是否正确。 你可以修改你历史的笔记：包括融合相似的知识，格式优化等等。

现在开始, 第一个片段：

"""




def get_merge_prompt(already_done) -> str:

    merge_promp = f"""
    请你充当一个关于保险条款的文字专家，我会给你一些零散的文字片段, 类似这样的格式：
    ['文字', '文字2']
    请把这些文字拼接起来，拼接成便于阅读的形式。

    这是已经梳理好文字片段:
    ```
    {already_done}
    ```

    请你根据你对保险条款和专业性的理解，把文字串起来。

    注意：
    1. 请尽可能保证拼接之后文字的流畅度。
    2. 尽可能保留文字里关于标题的结构信息。你可以根据自己的理解增加额外的标题。
    3. 尽量少的删减文字。


    """
    return merge_promp 

note_taken = ""

i = 0
temp_list = deque(maxlen=20)
already_done = ""
for line in open('list.txt', 'r'):
    i += 1

    temp_list.append(line)
    if i == 10:

        messages = [
            {"role": "system", "content": get_merge_prompt(already_done)},
            {"role": "user", "content": f"文字片段： {str(list(temp_list))}"}
        ]
 
        print(messages)
        import ipdb;ipdb.set_trace()
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages
        )
        already_done += response.choices[0].message.content
        print("---------------\n", already_done)
        records = open('fluent.txt', 'a')
        records.write(already_done + '\n')
        records.close()
        time.sleep(1)

        i = 0
        temp_list = []




