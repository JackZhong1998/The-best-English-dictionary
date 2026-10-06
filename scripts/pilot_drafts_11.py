"""Original candidates for the next ten basic pilot headwords.

Writes candidate files only. Editorial review and publication are separate.
"""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "enough": {
        "phonetic": "/ɪˈnʌf/", "syllables": ["e", "nough"], "pos": ["det.", "adv.", "pron."],
        "core_meanings": ["足够的", "足够地", "足够的量"], "etymology": "",
        "semantic_shift": "表示数量达到需要的程度，也可表示动作或性质达到要求的程度。",
        "senses": [
            sense(1, "det.", "as much or as many as needed", "数量达到需要的程度", "足够的", [("enough time", "足够的时间"), ("enough money", "足够的钱")], [("We have enough time to walk there.", "我们有足够的时间走过去。"), ("Is there enough food for everyone?", "食物够每个人吃吗？")], "sufficient：也指足够，语气较正式。", "not enough：不足的。", "enough 放在名词前：enough time；不能说 time enough。"),
            sense(2, "adv.", "to the degree that is needed", "达到所需的程度", "足够地", [("old enough", "年龄足够大"), ("quickly enough", "足够快地")], [("She is old enough to travel alone.", "她已经大到可以独自旅行了。"), ("I did not run fast enough to catch the bus.", "我跑得不够快，没赶上公交车。")], "sufficiently：意思接近，但更正式。", "too：表示过度，与 enough 的足够程度不同。", "enough 放在形容词或副词后：old enough、fast enough。"),
            sense(3, "pron.", "the amount that is needed", "所需的数量", "足够的量", [("have enough", "有足够的量"), ("enough for everyone", "够每个人用的量")], [("We have enough for lunch.", "我们有足够的东西吃午饭。"), ("That is enough for today.", "今天就到这里吧。")], "plenty：表示充裕，往往超过刚好够用的程度。", "too little：太少。", "enough 单独使用时，后面不用再接名词。"),
        ],
    },
    "enter": {
        "phonetic": "/ˈentər/", "syllables": ["en", "ter"], "pos": ["v."],
        "core_meanings": ["进入", "参加", "输入"], "etymology": "",
        "semantic_shift": "从进入一个地方，扩展到加入活动；在计算机语境中表示将信息放入系统。",
        "senses": [
            sense(1, "v.", "to go or come into a place", "走进或来到某处", "进入", [("enter a room", "进入房间"), ("enter the building", "进入大楼")], [("She entered the room quietly.", "她悄悄走进房间。"), ("Visitors must enter through the front door.", "访客必须从前门进入。")], "go in：口语中表示走进去；enter 较正式。", "leave：离开。", "enter 直接接地点，不说 enter into the room。"),
            sense(2, "v.", "to take part in a competition or activity", "报名参加比赛或活动", "参加", [("enter a competition", "报名参加比赛"), ("enter the race", "参加赛跑")], [("Our class entered the singing competition.", "我们班报名参加了歌唱比赛。"), ("He entered the race at the last minute.", "他在最后一刻报名参加赛跑。")], "join：泛指加入组织或活动；enter 常用于比赛报名。", "withdraw：退出比赛。", "enter a competition 指报名参赛，不是走进比赛场地。"),
            sense(3, "v.", "to put information into a computer or form", "把信息写入表格或系统", "输入", [("enter a password", "输入密码"), ("enter your name", "填写姓名")], [("Enter your password to open the file.", "输入密码后即可打开文件。"), ("Please enter your name on the form.", "请在表格上填写你的姓名。")], "type：强调按键输入；enter 强调把信息填进系统。", "delete：删除已输入的信息。", "enter information into a system 中的 into 指进入系统。"),
        ],
    },
    "environment": {
        "phonetic": "/ɪnˈvaɪrənmənt/", "syllables": ["en", "vi", "ron", "ment"], "pos": ["n."],
        "core_meanings": ["自然环境", "周围条件"], "etymology": "",
        "semantic_shift": "从事物周围的一切条件，具体指自然界，也可指影响生活、学习或工作的场所与氛围。",
        "senses": [
            sense(1, "n.", "the natural world around people, plants, and animals", "人、植物和动物所处的自然世界", "自然环境", [("protect the environment", "保护环境"), ("damage the environment", "破坏环境")], [("We should protect the environment.", "我们应该保护环境。"), ("Plastic waste can damage the environment.", "塑料垃圾可能破坏环境。")], "nature：强调自然界本身；environment 常强调其受到人类活动的影响。", "", "the environment 常指整体自然环境，通常用单数。"),
            sense(2, "n.", "the conditions in which someone lives, learns, or works", "生活、学习或工作的周围条件", "环境", [("a learning environment", "学习环境"), ("a safe environment", "安全的环境")], [("A quiet environment helps me study.", "安静的环境有助于我学习。"), ("Children need a safe environment to grow.", "孩子们需要安全的成长环境。")], "setting：指事情发生的场所或背景；environment 还包括氛围和条件。", "", "此义可说 an environment，指一个具体的学习或工作环境。"),
        ],
    },
    "example": {
        "phonetic": "/ɪɡˈzæmpəl/", "syllables": ["ex", "am", "ple"], "pos": ["n."],
        "core_meanings": ["例子", "榜样"], "etymology": "",
        "semantic_shift": "具体事物可用来说明一般情况，也可作为他人仿效的样本。",
        "senses": [
            sense(1, "n.", "something that shows what a group or idea is like", "用来说明一类事物或观点的具体事物", "例子", [("give an example", "举例"), ("for example", "例如")], [("Can you give me an example?", "你能给我举个例子吗？"), ("Some fruits, for example oranges, contain vitamin C.", "有些水果，例如橙子，含有维生素 C。")], "instance：也指具体事例，语气稍正式。", "", "for example 用于引出例子；example 是可数名词。"),
            sense(2, "n.", "a person or action that others should copy", "值得他人学习的人或做法", "榜样", [("set an example", "树立榜样"), ("a good example", "好榜样")], [("Parents should set a good example.", "父母应该树立好榜样。"), ("Her honesty is an example to us all.", "她的诚实是我们大家的榜样。")], "role model：通常指值得效仿的人；example 也可指具体行为。", "a bad example：坏榜样。", "set an example 指用自己的行为示范，不是列举例句。"),
        ],
    },
    "expect": {
        "phonetic": "/ɪkˈspekt/", "syllables": ["ex", "pect"], "pos": ["v."],
        "core_meanings": ["预料", "期望"], "etymology": "",
        "semantic_shift": "对尚未发生的事形成判断，也可表示希望别人按预期行动。",
        "senses": [
            sense(1, "v.", "to think something will happen", "认为某事将会发生", "预料", [("expect rain", "预计会下雨"), ("expect a reply", "预计会收到回复")], [("We expect rain tomorrow.", "我们预计明天会下雨。"), ("I did not expect the train to be late.", "我没料到火车会晚点。")], "predict：强调根据证据作预测；expect 也可凭经验作判断。", "be surprised by：对某事感到意外。", "expect something to happen 表示预计某事会发生。"),
            sense(2, "v.", "to want or require someone to do something", "希望或要求某人做某事", "期望", [("expect someone to help", "期望某人帮忙"), ("expect good results", "期待好结果")], [("My parents expect me to study hard.", "父母希望我认真学习。"), ("The coach expects everyone to arrive on time.", "教练要求所有人准时到达。")], "hope：强调希望发生；expect 往往还带有认为应该如此的意思。", "", "expect someone to do something 后接人，再接动词不定式。"),
        ],
    },
    "experience": {
        "phonetic": "/ɪkˈspɪriəns/", "syllables": ["ex", "pe", "ri", "ence"], "pos": ["n.", "v."],
        "core_meanings": ["经验", "经历", "亲身经历"], "etymology": "",
        "semantic_shift": "亲身做过的事可以积累为知识，也可以指一次具体事件；作动词时表示亲自遭遇。",
        "senses": [
            sense(1, "n.", "knowledge or skill gained by doing something", "通过亲自做事获得的知识或技能", "经验", [("work experience", "工作经验"), ("gain experience", "积累经验")], [("She has years of teaching experience.", "她有多年的教学经验。"), ("You can gain experience by volunteering.", "做志愿者可以积累经验。")], "practice：强调练习过程；experience 强调实践后积累的所得。", "lack of experience：缺乏经验。", "表示经验总量时，experience 通常不可数。"),
            sense(2, "n.", "an event that happens to someone", "某人亲身遇到的一件事", "经历", [("a new experience", "一次新体验"), ("a pleasant experience", "一次愉快的经历")], [("The trip was a wonderful experience.", "这次旅行是一段美好的经历。"), ("Moving to a new city was a new experience for me.", "搬到新城市对我是一次新体验。")], "event：指发生的事件；experience 强调亲身感受。", "", "指一次具体经历时，experience 可数。"),
            sense(3, "v.", "to have something happen to you", "亲身遭遇某事", "经历", [("experience difficulties", "经历困难"), ("experience change", "经历变化")], [("Many students experience stress before exams.", "许多学生在考试前会感到压力。"), ("The city experienced rapid growth.", "这座城市经历了快速发展。")], "undergo：也指经历，常用于较重大的变化或过程。", "", "experience 作动词直接接经历的事，不接 of。"),
        ],
    },
    "explain": {
        "phonetic": "/ɪkˈspleɪn/", "syllables": ["ex", "plain"], "pos": ["v."],
        "core_meanings": ["解释清楚", "说明原因"], "etymology": "",
        "semantic_shift": "从把事情讲明白，扩展为说明某事发生的原因。",
        "senses": [
            sense(1, "v.", "to make something clear by giving details", "通过说明细节让人明白", "解释清楚", [("explain a rule", "解释规则"), ("explain how it works", "解释它如何运作")], [("Can you explain this word to me?", "你能给我解释这个词吗？"), ("The teacher explained the rule again.", "老师又解释了一遍规则。")], "describe：描述事物是什么样；explain 还要让人理解。", "", "说 explain something to someone，不说 explain someone something。"),
            sense(2, "v.", "to give the reason for something", "说明某事发生的原因", "说明原因", [("explain the delay", "解释延误原因"), ("explain why", "说明为什么")], [("How do you explain the delay?", "你如何解释这次延误？"), ("She explained why she was late.", "她解释了自己迟到的原因。")], "account for：也指解释原因，语气较正式。", "", "explain why 后接完整句子；explain the delay 后接名词。"),
        ],
    },
    "express": {
        "phonetic": "/ɪkˈspres/", "syllables": ["ex", "press"], "pos": ["v.", "adj."],
        "core_meanings": ["表达", "特快的"], "etymology": "",
        "semantic_shift": "把想法或感受清楚地表达出来；在运输和寄送语境中，express 表示优先、快速办理。",
        "senses": [
            sense(1, "v.", "to show a thought or feeling in words or actions", "用语言或行动表现想法、感受", "表达", [("express an opinion", "表达意见"), ("express thanks", "表达感谢")], [("She expressed her opinion clearly.", "她清楚地表达了自己的意见。"), ("He expressed his thanks in a letter.", "他在信中表达了谢意。")], "say：泛指说出；express 强调把内心想法或感受传达出来。", "hide one's feelings：隐藏感受。", "express 作动词后直接接 opinion、thanks 等宾语。"),
            sense(2, "adj.", "traveling or delivered faster than usual", "比普通服务更快的", "特快的", [("an express train", "特快列车"), ("express delivery", "快递服务")], [("We took the express train to the city.", "我们乘特快列车进了城。"), ("Express delivery costs more.", "快递服务收费更高。")], "fast：泛指速度快；express 常指有专门安排的快速服务。", "standard delivery：普通配送。", "express 在这里是形容词，不是“表达”的意思。"),
        ],
    },
    "fact": {
        "phonetic": "/fækt/", "syllables": ["fact"], "pos": ["n."],
        "core_meanings": ["事实", "实际上"], "etymology": "",
        "semantic_shift": "从可证实的事情，发展出 in fact 用于补充真实情况或纠正印象的用法。",
        "senses": [
            sense(1, "n.", "something that is known to be true", "已经证实为真的事情", "事实", [("check the facts", "核实事实"), ("a well-known fact", "众所周知的事实")], [("Please check the facts before writing.", "动笔前请核实事实。"), ("It is a fact that water freezes at zero degrees Celsius.", "水在零摄氏度结冰是事实。")], "truth：强调真实本身；fact 指一条可核实的事实。", "fiction：虚构的事情。", "fact 是可数名词；a fact 指一条事实。"),
            sense(2, "n.", "used in the phrase in fact to add or correct information", "用于 in fact，补充或纠正实际情况", "实际上", [("in fact", "事实上"), ("in actual fact", "实际上")], [("I thought she was tired; in fact, she was ill.", "我以为她累了；其实她生病了。"), ("The test looked hard. In fact, it was easy.", "考试看起来难，其实很简单。")], "actually：也表示实际上；in fact 常用于纠正前面的印象。", "", "in fact 是固定短语，后面常加逗号。"),
        ],
    },
    "fail": {
        "phonetic": "/feɪl/", "syllables": ["fail"], "pos": ["v."],
        "core_meanings": ["未能做到", "考试不及格", "失灵"], "etymology": "",
        "semantic_shift": "从没有达到目标，具体用于考试不合格，也用于机器停止正常工作。",
        "senses": [
            sense(1, "v.", "to be unsuccessful in doing something", "没有成功做到某事", "未能做到", [("fail to finish", "未能完成"), ("fail to notice", "未能注意到")], [("We failed to finish the work on time.", "我们没能按时完成工作。"), ("I failed to notice the sign.", "我没注意到那个标志。")], "be unable to：表示无法做到；fail to 强调结果没有实现。", "succeed：成功做到。", "fail to 后接动词原形。"),
            sense(2, "v.", "to not pass a test or examination", "考试或测验没有及格", "不及格", [("fail an exam", "考试不及格"), ("fail a driving test", "驾照考试没通过")], [("He failed the math exam.", "他数学考试不及格。"), ("I failed my first driving test.", "我第一次驾照考试没通过。")], "not pass：也表示没通过；fail 更直接。", "pass：通过考试。", "fail an exam 直接接考试名称；不要说 fail in an exam。"),
            sense(3, "v.", "to stop working properly", "停止正常运转", "失灵", [("the engine fails", "发动机失灵"), ("the system fails", "系统故障")], [("The engine failed during the trip.", "旅途中发动机出了故障。"), ("The computer system failed this morning.", "今天早上电脑系统出了故障。")], "break down：机器或车辆出故障的常见说法。", "keep working：继续正常运转。", "机器作主语时，fail 表示失灵，不是考试不及格。"),
        ],
    },
}


def main():
    OUT.mkdir(exist_ok=True)
    for word, data in ENTRIES.items():
        (OUT / f"{word}.json").write_text(json.dumps({"word": word, **data}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRIES)} candidates")


if __name__ == "__main__":
    main()
