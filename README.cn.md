<h1 align="center">AutoUpdater</h1>
<div align="center">

[English](./README.md) | 简体中文

[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![测试状态](https://github.com/www778878net/AutoUpdater/actions/workflows/BuildandTest.yml/badge.svg?branch=main)](https://github.com/www778878net/AutoUpdater/actions/workflows/BuildandTest.yml)
[![QQ群](https://img.shields.io/badge/QQ群-323397913-blue.svg?style=flat-square&color=12b7f5&logo=qq)](https://qm.qq.com/cgi-bin/qm/qr?k=it9gUUVdBEDWiTOH21NsoRHAbE9IAzAO&jump_from=webapi&authKey=KQwSXEPwpAlzAFvanFURm0Foec9G9Dak0DmThWCexhqUFbWzlGjAFC7t0jrjdKdL)
</div>

## 反馈QQ群（点击加入）：[323397913](https://qm.qq.com/cgi-bin/qm/qr?k=it9gUUVdBEDWiTOH21NsoRHAbE9IAzAO&jump_from=webapi&authKey=KQwSXEPwpAlzAFvanFURm0Foec9G9Dak0DmThWCexhqUFbWzlGjAFC7t0jrjdKdL)

## 1. `AutoUpdater` 类文档 

### 概述

`AutoUpdater` 是一个用Python编写的自动更新工具，用于比较本地和远程文件的MD5值，并下载更新的文件。它支持初始化本地目录、生成MD5文件列表、更新文件等功能。

### 安装

克隆仓库到本地：

~~~
git clone https://github.com/www778878net/AutoUpdater.git
cd AutoUpdater
~~~

### 快速开始

以下是如何使用 `AutoUpdater` 的基本示例：

~~~python
from autoupdater import AutoUpdater, initialize_directory

# 初始化本地目录
local_dir = "/path/to/local/directory"
remote_url = "http://example.com/remote/"
result = initialize_directory(local_dir, remote_url)
print(result)

# 创建 AutoUpdater 实例并更新文件
updater = AutoUpdater(local_dir, remote_url)
update_result = updater.update_files()
print(update_result)
~~~

### 主要方法

- `initialize_directory(local_directory, remote_base_url)`: 初始化本地目录。
- `update_files()`: 更新本地文件。
- `get_file_list_with_md5(directory)`: 获取指定目录下所有文件的MD5值。
- `save_md5_json(output_file="md5.json")`: 生成并保存包含文件MD5值的JSON文件。

### 示例：初始化目录

~~~python
from autoupdater import initialize_directory

local_dir = "/path/to/local/directory"
remote_url = "http://example.com/remote/"
result = initialize_directory(local_dir, remote_url)
print(result)
~~~

### 示例：更新文件

~~~python
from autoupdater import AutoUpdater

updater = AutoUpdater("/path/to/local/directory", "http://example.com/remote/")
result = updater.update_files()
print(result)
~~~

### 运行测试

要运行测试，请在项目根目录下执行以下命令：

~~~
python -m unittest discover tests
~~~

### 其他

更多详细信息，请参阅项目的 [GitHub 仓库](https://github.com/www778878net/AutoUpdater) 或 API 文档。
