import requests
import json

class DoubanSpider:
    """
    爬取豆瓣电视 ，美剧、韩剧、国产剧
    """
    def __init__(self): #1.start_url
        self.url_temp_list = ["https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}",
                         "https://movie.douban.com/j/search_subjects?type=tv&tag=%E9%9F%A9%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                         "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}"]
        self.headers = {
                        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"
        }

    def parser_url(self,url):  #2.发送请求
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self,json_str):  #3.提取数据
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subjects"]
        print(content_list)
        print(len(content_list))
        return content_list

    def save_content_list(self,content_list):  #4.保存
        with open("douban.txt","a",encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
            print("保存成功")

    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            while True:
                #1.start_url
                url = url_temp.format(num)
                #2.发送请求
                json_str = self.parser_url(url)
                #3.提取数据
                content_list = self.get_content_list(json_str)
                #4.保存
                self.save_content_list(content_list)
                if len(content_list)<20:
                    break
                #5.构造下一页url，进入循环
                num += 20
if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()