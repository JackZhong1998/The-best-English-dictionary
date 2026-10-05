"""Original pilot candidates: build, business, cause, choose, collect."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "build": {
        "phonetic": "/bɪld/", "syllables": ["build"], "pos": ["v."],
        "core_meanings": ["建造", "建立", "逐渐增强"],
        "etymology": "源自古英语 byldan，早期指“建造房屋”。",
        "semantic_shift": "从一块块建成房屋，扩展为逐步建立关系、能力或信心。",
        "senses": [
            sense(1, "v.", "to make a structure by putting parts together", "把材料组合起来建成建筑物", "建造", [("build a house", "建房子"), ("build a bridge", "建桥")], [("They built a bridge over the river.", "他们在河上建了一座桥。"), ("My uncle built this small house.", "我叔叔建了这座小房子。")], "construct：也指建造，语气较正式；build 更常用。", "demolish：拆除建筑物。", "build 的过去式是 built，不是 builded。"),
            sense(2, "v.", "to develop something over time", "经过一段时间逐步建立某事物", "建立", [("build trust", "建立信任"), ("build a team", "组建团队")], [("It takes time to build trust.", "建立信任需要时间。"), ("She built a strong team at work.", "她在工作中组建了一支强大的团队。")], "develop：强调发展过程；build 常含逐步投入、建立基础的意思。", "destroy trust：破坏信任。", "build trust 不是建造有形物体，而是逐步建立关系。"),
            sense(3, "v.", "to increase gradually", "逐渐增加或增强", "逐渐增强", [("build up strength", "增强体力"), ("build up confidence", "增强信心")], [("Regular exercise builds up strength.", "经常锻炼能增强体力。"), ("Practice helped her build up confidence.", "练习帮助她逐渐建立信心。")], "increase：泛指增加；build up 强调逐步积累。", "weaken：变弱。", "build up 在这里是“逐渐增强”，不是把东西堆成楼。"),
        ],
    },
    "business": {
        "phonetic": "/ˈbɪznəs/", "syllables": ["busi", "ness"], "pos": ["n."],
        "core_meanings": ["商业", "企业", "事务"],
        "etymology": "源自古英语 busy 对应词形加 -ness，早期指忙碌或操心的状态。",
        "semantic_shift": "从使人忙碌的事情，发展为谋生工作与商业活动；具体经营单位也称 a business。",
        "senses": [
            sense(1, "n.", "the activity of buying and selling goods or services", "买卖商品或服务的商业活动", "商业", [("do business", "做生意"), ("business is growing", "生意在增长")], [("Her family has been in business for years.", "她家做生意很多年了。"), ("Business is slow this month.", "这个月生意清淡。")], "trade：强调买卖交易；business 的范围还包括经营和服务。", "", "此义 business 通常不可数；a business 常指一家公司。"),
            sense(2, "n.", "a company or shop", "一家公司或商店", "企业", [("a small business", "一家小企业"), ("start a business", "开办企业")], [("They started a small business together.", "他们一起创办了一家小企业。"), ("This business employs twenty people.", "这家企业雇用了二十个人。")], "company：多指公司；business 也可以是小店等经营单位。", "", "a business 可数；business 作商业活动时常不可数。"),
            sense(3, "n.", "a matter that concerns a person", "与某人有关的事情", "个人事务", [("personal business", "私事"), ("mind your own business", "管好你自己的事")], [("This is my personal business.", "这是我的私事。"), ("She told him to mind his own business.", "她叫他别管闲事。")], "matter：泛指一件事；business 在这里强调与某人有关。", "", "mind your own business 与经营企业无关，常是让人不要多管闲事。"),
        ],
    },
    "cause": {
        "phonetic": "/kɔːz/", "syllables": ["cause"], "pos": ["n.", "v."],
        "core_meanings": ["原因", "导致", "事业或目标"],
        "etymology": "经古法语 cause 来自拉丁语 causa“理由、诉讼”；拉丁语词更早来源不明。",
        "semantic_shift": "从解释行为或结果的理由，扩展到产生结果的因素；值得支持的目标也可称 a cause。",
        "senses": [
            sense(1, "n.", "the reason why something happens", "事情发生的原因", "原因", [("the main cause", "主要原因"), ("a cause of the problem", "问题的一个原因")], [("The police found the cause of the fire.", "警方找到了火灾原因。"), ("Stress can be a cause of poor sleep.", "压力可能是睡眠不佳的原因之一。")], "reason：也指原因；cause 更强调引出某个结果的因素。", "effect：原因造成的结果。", "cause 是原因；because 是连接原因从句的词。"),
            sense(2, "v.", "to make something happen", "使某事发生", "导致", [("cause a delay", "造成延误"), ("cause trouble", "引起麻烦")], [("Heavy rain caused a delay.", "大雨造成了延误。"), ("The mistake caused confusion.", "这个错误引起了混乱。")], "lead to：表示导致，后接结果；cause 直接接结果作宾语。", "prevent：防止发生。", "cause 是动词时直接接宾语：cause a problem。"),
            sense(3, "n.", "an aim that people support because they think it is important", "人们认为重要并愿意支持的目标或事业", "事业或目标", [("support a cause", "支持一项事业"), ("a good cause", "有意义的事业")], [("She gave money to a good cause.", "她向一项公益事业捐了款。"), ("They work for the cause of peace.", "他们为和平事业努力。")], "campaign：常指为目标开展的具体行动；cause 指所支持的目标。", "", "a good cause 是值得支持的事业，不是“好的原因”。"),
        ],
    },
    "choose": {
        "phonetic": "/tʃuːz/", "syllables": ["choose"], "pos": ["v."],
        "core_meanings": ["选择", "决定去做"],
        "etymology": "源自古英语 ceosan“挑选、选择”。",
        "semantic_shift": "核心是从几个可能项中挑出一个；选择的对象也可以是要采取的行动。",
        "senses": [
            sense(1, "v.", "to select a person or thing from several possibilities", "从若干人或物中选出一个", "选择人或物", [("choose a book", "挑一本书"), ("choose between two options", "在两个选项间选择")], [("Please choose a seat near the window.", "请选一个靠窗的座位。"), ("She chose the red dress.", "她选了那件红裙子。")], "select：也指挑选，语气更正式；choose 更日常。", "reject：拒绝选中某项。", "choose 的过去式是 chose，过去分词是 chosen。"),
            sense(2, "v.", "to decide to do something", "决定采取某种行动", "决定去做", [("choose to stay", "选择留下"), ("choose not to answer", "选择不回答")], [("He chose to walk home.", "他选择步行回家。"), ("I chose not to join the game.", "我选择不参加比赛。")], "decide：泛指作决定；choose 暗示存在其他可选行动。", "be forced to：被迫做某事。", "choose to do 后接动词原形，不说 choose doing。"),
        ],
    },
    "collect": {
        "phonetic": "/kəˈlekt/", "syllables": ["col", "lect"], "pos": ["v."],
        "core_meanings": ["收集", "采集", "收取"],
        "etymology": "经古法语 collecter，与拉丁语 colligere“聚集在一起”有关。",
        "semantic_shift": "从把分散的东西聚到一起，扩展到采集资料，以及收取分散的款项。",
        "senses": [
            sense(1, "v.", "to bring several things together, often as a hobby", "把若干物品收在一起，常作为爱好", "收集物品", [("collect stamps", "集邮"), ("collect old coins", "收集旧硬币")], [("My sister collects old postcards.", "我姐姐收集旧明信片。"), ("He collected shells on the beach.", "他在海滩上收集贝壳。")], "gather：泛指聚拢；collect 常带有有意收集并保存的意味。", "scatter：把东西散开。", "collect stamps 是收集邮票，不是寄出邮票。"),
            sense(2, "v.", "to gather information for a purpose", "为特定目的采集信息", "采集信息", [("collect data", "收集数据"), ("collect information", "收集信息")], [("The students collected data for the project.", "学生们为项目收集了数据。"), ("We collect information from volunteers.", "我们从志愿者那里收集信息。")], "record：强调把信息记下来；collect 强调从多处汇集。", "", "collect data 通常指采集，不能理解成“收藏数据”供欣赏。"),
            sense(3, "v.", "to receive money that is owed or donated", "收取应付或捐赠的钱款", "收取款项", [("collect a fee", "收取费用"), ("collect donations", "募集捐款")], [("The school collects a small fee.", "学校收取一笔小额费用。"), ("They collected donations for the shelter.", "他们为收容所募集了捐款。")], "receive：只表示收到；collect 常含主动收取或募集。", "pay：支付款项。", "collect donations 是募捐；donate 是捐出。"),
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
