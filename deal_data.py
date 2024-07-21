import json
import re


def all_chinese(chinese):
    """判断字符串是否全为中文"""
    # pattern = re.compile(r'^[\u4e00-\u9fa5\u3000-\u303F\uFF00-\uFFEF\u2000-\u206F]*$')
    # return bool(pattern.match(chinese))
    return True

path = r"C:\Users\Nas\Downloads\百科类问答json版\baike_qa_valid.json"
# path = r"C:\Users\Nas\Downloads\百科类问答json版\baike_qa_train.json"
# 读取文件
result = []
with open(path, 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        title = data["title"]
        answer = data["answer"]
        if len(answer) > 0 and len(title) > 0 and all_chinese(answer) and all_chinese(title):
            user = {"role": "user", "content": title}
            assistant = {"role": "assistant", "content": answer}
            result.append(user)
            result.append(assistant)
end_data = {"messages": result}
# print(end_data)
with open(r"C:\Users\Nas\Downloads\百科类问答json版\dev.jsonl", 'w', encoding='utf8') as f:
    f.write(json.dumps([end_data], ensure_ascii=False, indent=4))
