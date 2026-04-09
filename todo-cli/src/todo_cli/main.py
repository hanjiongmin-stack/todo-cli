import argparse
# 正确写法：包名用下划线，匹配文件夹名 todo_cli
from todo_cli.core import add_tasks, list_tasks, mark_done, delete_tasks
def main():
    parser = argparse.ArgumentParser(description="命令行代办任务管理器")
    subparsers = parser.add_subparsers(dest='command',required=True,help="可用命令")
    add_parser = subparsers.add_parser("add",help="添加新任务")
    add_parser.add_argument("content",nargs="+",help="任务内容支持空格")
    subparsers.add_parser("list",help="列出所有任务和状态")
    done_parser = subparsers.add_parser("done",help="标记任务以完成")
    done_parser.add_argument("index",type=int,help="任务编号，从一开始")
    delete_parser = subparsers.add_parser("delete",help="删除指定任务")
    delete_parser.add_argument("index",type=int,help="任务编号，从一开始")

    args = parser.parse_args()
    if args.command == "add":
        content = " ".join(args.content)
        print(add_tasks(content))
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("当前无任务")
        for idx, task in enumerate(tasks,1):
            status = "✓" if task["done"]else"×"
            print(f"{idx}.[{status}] {task['content']}")
    elif args.command == "done":
        try:
            print(mark_done(args.index))
        except IndexError as e:
            print(f"出错{e}")
    elif args.command == "delete":
        try:
            print(delete_tasks(args.index))
        except IndexError as e:
            print(f"出错{e}")

if __name__ == "__main__":
    main()