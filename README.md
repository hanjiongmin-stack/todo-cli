```markdown
# 🎯 todo-cli
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/No%20Dependencies-Yes-success.svg" alt="No Dependencies">
  <br>
  <img src="https://img.shields.io/github/stars/hanjiongmin-stack/todo-cli.svg" alt="GitHub Stars">
  <img src="https://img.shields.io/github/last-commit/hanjiongmin-stack/todo-cli.svg" alt="Last Commit">
  <img src="https://img.shields.io/tokei/lines/github/hanjiongmin-stack/todo-cli" alt="Lines of Code">
</p>

<p align="center">我的第一个完整 Python 开源项目 🎉</p>

---

## ✨ 项目介绍
一个轻量、简单、无任何依赖的 **命令行待办任务管理器**。
只需在终端输入命令，即可快速管理任务，所有数据本地保存，重启不丢失。

---

## 🚀 安装方法
### 方式一：从 GitHub 一键安装
```bash
pip install git+https://github.com/hanjiongmin-stack/todo-cli.git
```

### 方式二：本地开发模式安装
```bash
git clone https://github.com/hanjiongmin-stack/todo-cli.git
cd todo-cli
pip install -e .
```

---

## 📖 使用教程
### 1. 查看所有任务
```bash
todo list
```

### 2. 添加新任务
```bash
todo add "学习Python"
todo add "完成项目作业"
```

### 3. 标记任务完成
```bash
todo done 1
```

### 4. 删除任务
```bash
todo delete 1
```

---

## 📁 项目结构
```
todo-cli/
├── src/
│   └── todo_cli/
│       ├── __init__.py  # 项目版本
│       ├── core.py      # 任务核心逻辑
│       └── main.py      # 命令行入口
├── pyproject.toml       # 项目配置
├── .gitignore           # Git 忽略文件
├── LICENSE.txt          # 开源协议
└── README.md            # 项目说明
```

---

## 🧩 技术亮点
- 纯 Python 标准库开发，**零第三方依赖**
- 命令行交互基于 argparse
- 任务数据使用 JSON 本地持久化
- 全平台兼容：Windows / macOS / Linux

---

## 💡 常用命令总结
| 命令 | 功能 |
|------|------|
| `todo list` | 查看所有任务 |
| `todo add "任务内容"` | 添加任务 |
| `todo done 编号` | 标记完成 |
| `todo delete 编号` | 删除任务 |

---

## 📄 开源协议
MIT License — 可自由使用、修改、分享

---

## 🎯 关于作者
这是我的第一个 Python 开源项目！
GitHub：[hanjiongmin-stack](https://github.com/hanjiongmin-stack)
