"""Original pilot candidates: arrange, arrive, article, attend, avoid."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "arrange": {
        "phonetic": "/əˈreɪndʒ/", "syllables": ["ar", "range"], "pos": ["v."],
        "core_meanings": ["整理", "安排", "筹备"],
        "etymology": "经古法语 arengier 进入英语，早期指“排成队列”。",
        "semantic_shift": "从把人或物排成有序的队列，扩展到整理物品和事先安排活动。",
        "senses": [
            sense(1, "v.", "to put things in a particular order or position", "把物品按一定顺序或位置摆好", "整理摆放", [("arrange the books", "整理书籍"), ("arrange flowers", "插花")], [("She arranged the books by subject.", "她按主题整理了书籍。"), ("We arranged the chairs in a circle.", "我们把椅子摆成一圈。")], "organize：可指整理物品或工作；arrange 更强调摆放次序。", "scatter：把东西撒乱。", "arrange 是动词“排列”；range 作名词常指“范围”，如 a range of books。"),
            sense(2, "v.", "to plan the details of an event or meeting", "计划活动或会面的具体事项", "安排活动", [("arrange a meeting", "安排会议"), ("arrange a visit", "安排参观")], [("Can we arrange a meeting for Friday?", "我们能把会议安排在星期五吗？"), ("They arranged a visit to the museum.", "他们安排了参观博物馆。")], "plan：偏重制定计划；arrange 常指落实时间、地点等细节。", "cancel：取消已安排的活动。", "arrange to meet someone 是安排见面；arrange a meeting 是安排会议。"),
            sense(3, "v.", "to make sure something is provided or done", "设法确保某事得到提供或完成", "筹备所需事项", [("arrange transportation", "安排交通"), ("arrange for a taxi", "安排一辆出租车")], [("I arranged transportation for the guests.", "我为客人安排了交通。"), ("We arranged for a taxi to pick her up.", "我们安排了一辆出租车接她。")], "organize：也指组织协调；arrange for 强调让某项服务实现。", "", "arrange for a taxi 是安排车辆，不是把出租车排成一列。"),
        ],
    },
    "arrive": {
        "phonetic": "/əˈraɪv/", "syllables": ["ar", "rive"], "pos": ["v."],
        "core_meanings": ["到达", "来临", "得出"],
        "etymology": "经古法语 ariver，原指船只“抵达岸边”，最终与拉丁语 ripa“岸”有关。",
        "semantic_shift": "从船靠岸，扩展到人或交通工具到达目的地；时间和事件也可以比喻为“到来”。",
        "senses": [
            sense(1, "v.", "to reach a place at the end of a journey", "旅程结束时到达一个地点", "到达地点", [("arrive at the station", "到达车站"), ("arrive in London", "到达伦敦")], [("The train arrived at noon.", "火车中午到站。"), ("We arrived in London yesterday.", "我们昨天抵达伦敦。")], "reach：也指抵达，后面直接接地点；arrive 常配 at 或 in。", "depart：离开出发地。", "arrive at 常接较小地点；arrive in 常接城市或国家。"),
            sense(2, "v.", "to come or happen at a certain time", "在某个时候到来或发生", "来临", [("spring arrives", "春天到来"), ("the day arrives", "那一天来临")], [("Spring arrived early this year.", "今年春天来得早。"), ("The long-awaited day finally arrived.", "期待已久的那一天终于到来。")], "come：更日常；arrive 更突出某个时刻终于到了。", "", "这里的 arrive 是时间来临，不是人乘车抵达。"),
            sense(3, "v.", "to reach a decision after thinking", "经过思考得出决定", "得出结论", [("arrive at a decision", "作出决定"), ("arrive at a conclusion", "得出结论")], [("We arrived at a decision together.", "我们一起作出了决定。"), ("The team arrived at a clear conclusion.", "团队得出了明确结论。")], "reach a decision：意思相近；arrive at 强调经过过程后得出结果。", "remain undecided：仍未作出决定。", "arrive at a conclusion 是得出结论，没有实际旅行。"),
        ],
    },
    "article": {
        "phonetic": "/ˈɑːrtɪkəl/", "syllables": ["ar", "ti", "cle"], "pos": ["n."],
        "core_meanings": ["文章", "物品", "冠词"],
        "etymology": "经古法语 article，来自拉丁语 articulus“一个部分、关节”。",
        "semantic_shift": "从整体中的一小部分，发展为报刊中的一篇文章、清单中的一件物品，也用于语法中的冠词。",
        "senses": [
            sense(1, "n.", "a piece of writing in a newspaper or website", "报纸或网站上的一篇文章", "文章", [("read an article", "读一篇文章"), ("a news article", "新闻报道")], [("I read an article about sleep.", "我读了一篇关于睡眠的文章。"), ("Her article appeared in the school paper.", "她的文章刊登在校报上。")], "essay：常指较完整的论述文章；article 常见于报刊或网站。", "", "article 是一篇文章，不等于整本杂志。"),
            sense(2, "n.", "a single object, especially one in a list", "一件物品，尤指清单中的一项", "物品", [("an article of clothing", "一件衣物"), ("household articles", "家居用品")], [("Each article has a price tag.", "每件商品都有价格标签。"), ("She packed a few articles of clothing.", "她打包了几件衣服。")], "item：也指一件物品；article 在商品或清单语境中较正式。", "", "an article of clothing 指一件衣物，不是一篇关于衣服的文章。"),
            sense(3, "n.", "a word such as a, an, or the used before a noun", "名词前使用的 a、an 或 the", "冠词", [("the definite article", "定冠词"), ("the indefinite article", "不定冠词")], [("The word 'the' is an article.", "the 这个词是冠词。"), ("Use an article before this noun.", "在这个名词前使用冠词。")], "determiner：范围更广的限定词；article 只指 a、an、the 等冠词。", "", "语法中的 article 不是“文章”；需看讨论的是词还是文本。"),
        ],
    },
    "attend": {
        "phonetic": "/əˈtend/", "syllables": ["at", "tend"], "pos": ["v."],
        "core_meanings": ["出席", "上学", "处理或照料"],
        "etymology": "经古法语 atendre，最终来自拉丁语 attendere，字面上与“把注意力伸向某处”有关。",
        "semantic_shift": "从把注意力放在某事上，发展为到场参与，以及认真处理某人或某事的需要。",
        "senses": [
            sense(1, "v.", "to be present at an event", "出席活动", "出席", [("attend a meeting", "出席会议"), ("attend a concert", "参加音乐会")], [("I attended the meeting yesterday.", "我昨天出席了会议。"), ("Many parents attended the concert.", "许多家长参加了音乐会。")], "go to：一般说去某地；attend 强调到场参与活动。", "miss：错过或缺席。", "attend 直接接活动名词，通常不说 attend to a meeting。"),
            sense(2, "v.", "to go regularly to a school or course", "定期到学校或课程学习", "上学或上课", [("attend school", "上学"), ("attend classes", "上课")], [("She attends school near her home.", "她在家附近上学。"), ("He attended evening classes last year.", "他去年上过夜校课程。")], "study at：强调在某校学习；attend 强调实际去上课。", "skip class：逃课或缺课。", "attend school 不表示去学校一次，而是经常在那里上学。"),
            sense(3, "v.", "to deal with or care for someone or something", "处理事情或照顾某人", "处理或照料", [("attend to a problem", "处理问题"), ("attend to a patient", "照料病人")], [("Please attend to this problem today.", "请今天处理这个问题。"), ("A nurse attended to the patient.", "一名护士照料了病人。")], "deal with：表示处理；attend to 还可强调给予关注和照料。", "neglect：忽视，不予照料。", "attend to a patient 是照料病人；attend a meeting 是出席会议。"),
        ],
    },
    "avoid": {
        "phonetic": "/əˈvɔɪd/", "syllables": ["a", "void"], "pos": ["v."],
        "core_meanings": ["避开", "避免"],
        "etymology": "经法语相关词形进入英语，早期与“离开、使空”有关。",
        "semantic_shift": "从离开某个人或地方，扩展到采取行动使不希望发生的事不出现。",
        "senses": [
            sense(1, "v.", "to stay away from a person or place", "有意不接近某人或某地", "避开人或地点", [("avoid someone", "躲开某人"), ("avoid crowded places", "避开拥挤的地方")], [("I avoided the busy road.", "我避开了那条繁忙的路。"), ("She avoided him after the argument.", "争论后她一直躲着他。")], "keep away from：也表示远离；avoid 强调有意避开。", "approach：靠近。", "avoid someone 是躲开某人，不一定表示讨厌他。"),
            sense(2, "v.", "to prevent something bad from happening", "设法使不好的事情不发生", "避免事情发生", [("avoid mistakes", "避免错误"), ("avoid delays", "避免延误")], [("Check your work to avoid mistakes.", "检查作业以避免出错。"), ("We left early to avoid delays.", "我们提早出发，以免耽搁。")], "prevent：强调阻止发生；avoid 常强调通过选择或行动绕开风险。", "cause：引起某事。", "avoid 后面可直接接名词；avoid doing 中用动名词。"),
            sense(3, "v.", "to choose not to do something", "有意不做某事", "避免某种行为", [("avoid eating late", "避免太晚吃东西"), ("avoid making noise", "避免制造噪音")], [("Try to avoid eating too late.", "尽量不要太晚吃东西。"), ("Please avoid making noise here.", "请不要在这里制造噪音。")], "refrain from：同样指克制不做，语气更正式。", "", "avoid 后接动词 ing 形式，不说 avoid to do。"),
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
