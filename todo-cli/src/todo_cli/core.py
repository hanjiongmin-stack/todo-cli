import json
import os

File_Name = "task.json"
def load_tasks():
    if not os.path.exists(File_Name):
        return []
    with open(File_Name, "r",encoding="utf-8") as f:
        return json.load(f)
def save_tasks(task):
    with open(File_Name, "w",encoding="utf-8") as f:
        json.dump(task, f,indent=2,ensure_ascii=False)
def add_tasks(content):
    tasks = load_tasks()
    tasks.append({"content": content , "done": False})
    save_tasks(tasks)
    return "添加成功"
def list_tasks():
    return load_tasks()
def mark_done(index):
    tasks = load_tasks()
    if 1<=index<=len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        return f"任务{index}已完成"
    else:
        raise ValueError("无效任务编号")
def delete_tasks(index):
    tasks = load_tasks()
    if 1<=index<=len(tasks):
        removed = tasks.pop(index-1)
        #把 tasks 里第 index-1 个任务删掉,同时把被删掉的那个任务当成结果返回
        save_tasks(tasks)
        return f"已删除任务:{removed['content']}"
    else:
        raise  ValueError("无效任务编号")