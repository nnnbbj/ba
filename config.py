# 蔚蓝档案抽卡机器人配置

# 角色数据
CHARACTERS = {
    "3星": {
        "概率": 0.025,  # 2.5%
        "角色": [
            {"名称": "阿露", "图片": "https://baimg.bigjackson.top/img/alu.jpg"},
            {"名称": "白子", "图片": "https://baimg.bigjackson.top/img/baizi.png"},
            {"名称": "日富美", "图片": "https://baimg.bigjackson.top/img/rifumei.png"},
            {"名称": "优香", "图片": "https://baimg.bigjackson.top/img/youxiang.png"},
            {"名称": "星野", "图片": "https://baimg.bigjackson.top/img/xingye.png"},
            {"名称": "千世", "图片": "https://baimg.bigjackson.top/img/qianshi.png"},
            {"名称": "明日奈", "图片": "https://baimg.bigjackson.top/img/mingrinai.png"},
            {"名称": "花凛", "图片": "https://baimg.bigjackson.top/img/hualing.png"},
            {"名称": "睦月", "图片": "https://baimg.bigjackson.top/img/xiyue.png"},
            {"名称": "芹香", "图片": "https://baimg.bigjackson.top/img/qinxiang.png"},
            {"名称": "亚子", "图片": "https://baimg.bigjackson.top/img/yazi.png"},
        ]
    },
    "2星": {
        "概率": 0.185,  # 18.5%
        "角色": [
            {"名称": "小玉", "图片": "https://baimg.bigjackson.top/img/xiaoyu.png"},
            {"名称": "绿", "图片": "https://baimg.bigjackson.top/img/lv.png"},
            {"名称": "茜", "图片": "https://baimg.bigjackson.top/img/xi.png"},
            {"名称": "桃井", "图片": "https://baimg.bigjackson.top/img/taojing.png"},
            {"名称": "野宫", "图片": "https://baimg.bigjackson.top/img/yegong.png"},
            {"名称": "千夏", "图片": "https://baimg.bigjackson.top/img/qianxia.png"},
            {"名称": "佳代子", "图片": "https://baimg.bigjackson.top/img/jiadaizi.png"},
            {"名称": "铃美", "图片": "https://baimg.bigjackson.top/img/lingmei.png"},
            {"名称": "莲见", "图片": "https://baimg.bigjackson.top/img/lianjian.png"},
            {"名称": "泉", "图片": "https://baimg.bigjackson.top/img/quan.png"},
        ]
    },
    "1星": {
        "概率": 0.79,  # 79%
        "角色": [
            {"名称": "爱丽丝", "图片": "https://baimg.bigjackson.top/img/ailisi.png"},
            {"名称": "小春", "图片": "https://baimg.bigjackson.top/img/xiaocun.png"},
            {"名称": "小满", "图片": "https://baimg.bigjackson.top/img/xiaoman.png"},
            {"名称": "小桃", "图片": "https://baimg.bigjackson.top/img/taojing.png"},
            {"名称": "小绿", "图片": "https://baimg.bigjackson.top/img/lv.png"},
        ]
    }
}

# 抽卡设置
GACHA_SETTINGS = {
    "单抽价格": 120,  # 钻石
    "十连价格": 1200,  # 钻石
    "保底机制": {
        "3星保底": 200,  # 200抽保底3星
        "2星保底": 10,   # 10抽保底2星
    }
}

# 欢迎消息
WELCOME_MESSAGE = """
🎮 欢迎来到蔚蓝档案抽卡模拟器！

可用命令：
/start - 开始使用
/gacha - 单抽 (120钻石)
/tenpull - 十连抽 (1200钻石)
/balance - 查看钻石余额
/stats - 查看抽卡统计
/sign - 每日签到 (10000钻石)
/code - 兑换码兑换
/help - 显示帮助信息

祝你抽卡欧气满满！✨
"""

# 帮助消息
HELP_MESSAGE = """
📖 蔚蓝档案抽卡机器人使用指南

🎯 抽卡概率：
• 3星角色：2.5%
• 2星角色：18.5%
• 1星角色：79%

💰 抽卡费用：
• 单抽：120钻石
• 十连：1200钻石

🎁 保底机制：
• 200抽内必定获得3星角色
• 10抽内必定获得2星角色

📊 统计功能：
• 查看抽卡历史
• 统计各稀有度获得数量
• 计算抽卡花费

🎁 每日签到：
• 使用 /sign 每日签到
• 每次签到获得10000钻石

🎫 兑换码功能：
• 使用 /code 输入兑换码
• 兑换码：群中获取
• 每个兑换码每个用户只能使用一次

开始你的抽卡之旅吧！🎲
""" 