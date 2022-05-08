startUrl = "http://news.yahoo.com/news/topics/"
print(startUrl.split("/")) # ['http:', '', 'news.yahoo.com', 'news', 'topics', '']
print(startUrl.split("/")[:3]) # ['http:', '', 'news.yahoo.com']


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """
       pass


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser'):
        host_name = "/".join(startUrl.split("/")[:3])

        ans_set = {startUrl, }
        check_set = {startUrl, }
        while check_set:
            next_check = set()
            for url in check_set:
                for next_url in htmlParser.getUrls(url):
                    if next_url.startswith(host_name) and next_url not in ans_set:
                        next_check.add(next_url)
                        ans_set.add(next_url)
            check_set = next_check
        return list(ans_set)
