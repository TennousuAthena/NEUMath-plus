import re
import requests
from config import APIbase, Authorization


class Chapter(dict):
    def __init__(self, label: str, id :int, sub: int = 1):
        self.label = label
        self.id = id
        self.count = self._getNumFromName(label)
        self.problems = []
        self.sub = sub
        
        self._fetchProblems()
        dict.__init__(self, label=label, id=id, count=self.count, problems=self.problems, sub=sub)

    def _getNumFromName(self, name) -> int:
        pattern = r"\((\d+)题\)"  # 正则表达式模式，匹配括号内的数字部分
        match = re.search(pattern, name)  # 在字符串中查找匹配的部分
        if match:
            return int(match.group(1))
        else:
            return 0
        
    def _fetchProblems(self):
        if self.count == 0:
            return None
        pages = self.count // 10 + 1
        try:
            for page in range(pages):
                data = requests.get(APIbase + f'/paper/gett?sub={self.sub}&page={page}&cat={self.id}'
                                    ,headers={'Authorization': Authorization}).json()
                assert data['code'] == 200
                assert data['data']['data'] is not None
                for problem in data['data']['data']:
                    self.problems.append(Problem(problem))
        except:
            print(f"Error: Failed to fetch problem {self.label} on page {page} / {pages}")

class Problem(dict):
    def __init__(self, problem):
        self.acc = problem['Accuracy'].replace("%", "")
        self.answer = problem['answer']
        self.path = problem['text']

        dict.__init__(self, acc=self.acc, answer=self.answer, path=self.path)
