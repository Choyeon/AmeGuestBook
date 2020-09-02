# AmeGuestBook

**基于Flask框架开发的留言板网站**

#### 快速开始

```shell
git clone https://github.com/Choyeon/AmeGuestBook.git
cd AmeGuestBook
# 确保安装了Python3.X
# 如果没有pipenv使用pip3 install pipenv 安装
pipenv install # 自动下载依赖包和创建虚拟环境 
pipenv shell # 切换到虚拟环境 
flask run # 直接运行Flask服务器即可查看效果 内置了本地的SQLite数据库不需要配置
```

#### 效果图![1](https://github-photo-1252181153.cos.ap-shanghai.myqcloud.com/1.png)

![2](https://github-photo-1252181153.cos.ap-shanghai.myqcloud.com/2.png)

#### 目录结构

```shell
├── app # 应用入口
│   ├── static # 储存静态文件
│   │   ├── css # 储存CSS样式
│   │   └── js # 储存JavaScript脚本
│   └── templates # 储存网页模版
│       └── errors # 储存错误页面
├── assets # 储存readme图片
└── migrations # 数据库迁移文件 不迁移不会生成
```



#### 数据库

```python
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
```

| 字段名    | 类型     | 长度 | 描述         |
| --------- | -------- | ---- | ------------ |
| id        | int      | ♾    | 主键         |
| body      | varchar  | 255  | 留言内容     |
| name      | String   | 20   | 留言昵称     |
| timestamp | datetime | ♾    | 内容发布时间 |

#### 开源协议

MIT License

Copyright (c) 2020 choyeon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
