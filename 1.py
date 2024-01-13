#-*- coding: utf-8 -*-
# 文件名：app.py
import web    # 引入web.py库

# 表明访问的URL，这里表示的是所有响应，均由 class 对象 index 来响应
# 注：/(.*) 代表的是正则匹配url后面的所有路径，也就是响应任何请求
urls = (
     '/(.*)', 'index'
)

# 声明一个名叫app的“应用”
app = web.application(urls, globals())

# 表示 class 对象 index
# 传递参数：self，name（name指url路径/后面的内容）
class index:
    # 响应GET请求（声明函数）
    def GET(self,name):
        # 使用只读，二进制方式打开文件，读取到变量 index_text 中
        index_text = open('index.html','rb').read()
        # 输出变量 index_text 内的内容，也就是 index.html 内的HTML代码
        return index_text

# 当该.py文件被直接运行时，if __name__ == "__main__": 下的代码将被运行
# 当该.py文件作为模块被引入时，if __name__ == "__main__": 下的代码不会被运行
if __name__ == "__main__":
    # 运行这个服务器
    app.run()
