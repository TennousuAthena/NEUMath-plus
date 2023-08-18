import os

dataPath = os.path.join(os.path.dirname(__file__), 'data/')
problemIndexPath = os.path.join(os.path.dirname(__file__), 'data/index.json')
problemStorePath = os.path.join(os.path.dirname(__file__), 'data/chapter')

Authorization = ""

APIbase = "https://api.neumathe.cn/"
ImgBase = "https://www.neumathe.cn/pic/"

SubMap = {
    "高等数学": 1,
    "线性代数": 2,
    "概率统计": 3,
    "复变函数": 4
}

picMap = {
    1: "高等数学_GS",
    2: "线性代数_XD",
    3: "概率统计_GL",
    4: "复变函数_FB"
}