"""Original pilot candidates: basic, become, begin, believe, benefit."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "basic": {
        "phonetic": "/ˈbeɪsɪk/", "syllables": ["ba", "sic"], "pos": ["adj.", "n."],
        "core_meanings": ["基本的", "基础的", "基础知识"],
        "etymology": "由 base“基础”加形容词后缀 -ic 构成；最早的英语用法与化学有关。",
        "semantic_shift": "从“与基础有关”，发展为最重要、最初步或最简单的层次；复数 basics 指一门事的基础知识。",
        "senses": [
            sense(1, "adj.", "forming the most important or necessary part", "构成最重要或必需的部分", "基本的", [("basic needs", "基本需求"), ("a basic rule", "基本规则")], [("Food is a basic human need.", "食物是人的基本需求。"), ("Please follow the basic safety rules.", "请遵守基本安全规则。")], "essential：强调必不可少；basic 强调处在基础层次。", "optional：可选择的，并非必需。", "basic 不一定表示“容易”，basic needs 是根本需求。"),
            sense(2, "adj.", "simple and suitable for a beginner", "简单、适合初学者的", "初级的", [("basic English", "基础英语"), ("basic skills", "基础技能")], [("I learned basic English at school.", "我在学校学了基础英语。"), ("This course teaches basic computer skills.", "这门课教授基础电脑技能。")], "elementary：也指初级，常用于学习阶段；basic 范围更广。", "advanced：高级的。", "basic skills 是基础技能，不等于能力低下。"),
            sense(3, "n.", "the simplest and most important parts of a subject", "一门学科最简单也最重要的部分", "基础知识", [("learn the basics", "学习基础知识"), ("back to basics", "回归基本功")], [("Let's learn the basics first.", "我们先学基础知识。"), ("She knows the basics of cooking.", "她懂得烹饪的基础知识。")], "fundamentals：也指基本原理，语气较正式。", "", "此义通常用复数 the basics；basic 单数一般是形容词。"),
        ],
    },
    "become": {
        "phonetic": "/bɪˈkʌm/", "syllables": ["be", "come"], "pos": ["v."],
        "core_meanings": ["变成", "成为", "后来怎样"],
        "etymology": "源自古英语 becuman，由 be- 与 come 的旧形式组合，早期有“到来、发生”之意。",
        "semantic_shift": "从进入一个新状态或发生变化，发展为“变成、成为”；what became of ... 保留了“后来发生什么”的问法。",
        "senses": [
            sense(1, "v.", "to start to be in a new state", "进入新的状态", "变得", [("become tired", "变累"), ("become clear", "变得清楚")], [("The sky became dark.", "天空变暗了。"), ("She became more confident with practice.", "经过练习，她变得更自信了。")], "get：也可表示变得，语气更口语；become 较中性。", "remain：保持原状。", "become 后可直接接形容词，不用 become to be tired。"),
            sense(2, "v.", "to gain a new role or identity", "获得新的身份或角色", "成为", [("become a teacher", "成为老师"), ("become a member", "成为成员")], [("He became a doctor last year.", "他去年成为一名医生。"), ("She became the team leader.", "她成为了团队负责人。")], "turn into：强调转变成另一事物；become 常用于身份变化。", "stop being：不再是。", "become a doctor 后接名词；become confident 后接形容词。"),
            sense(3, "v.", "to happen to someone or something later", "某人或某物后来遭遇什么", "后来怎样", [("what became of him", "他后来怎么样了"), ("what became of the plan", "那个计划后来怎样了")], [("What became of your old bike?", "你的旧自行车后来怎么样了？"), ("Nobody knows what became of the plan.", "没人知道那个计划后来怎么样了。")], "happen to：也可问后来发生了什么；become of 常见于疑问句。", "", "what became of 不是“变成什么材料”，而是问后续结果。"),
        ],
    },
    "begin": {
        "phonetic": "/bɪˈɡɪn/", "syllables": ["be", "gin"], "pos": ["v."],
        "core_meanings": ["开始", "起初"],
        "etymology": "源自古英语 beginnan；后半部分更早词源不确定。",
        "semantic_shift": "从迈出第一步，泛指活动、过程或事件的开端。",
        "senses": [
            sense(1, "v.", "to start doing something", "开始做某事", "开始行动", [("begin to read", "开始阅读"), ("begin working", "开始工作")], [("Let's begin the lesson now.", "我们现在开始上课吧。"), ("She began to read the letter.", "她开始读那封信。")], "start：意思接近，口语更常见；begin 稍正式。", "finish：完成。", "begin 可接 to do 或 doing；过去式是 began。"),
            sense(2, "v.", "to have a starting point in time or place", "在某时或某地开始", "开始发生", [("the show begins", "演出开始"), ("begin at nine", "九点开始")], [("The movie begins at seven.", "电影七点开始。"), ("The path begins near the bridge.", "小路从桥附近开始。")], "start：也可表示事件开始；begin 常用于较正式的说明。", "end：结束。", "此义 begin 不需要宾语：The movie begins at seven。"),
            sense(3, "v.", "to have something as the first part", "以某事作为开头", "以……开头", [("begin with a question", "以一个问题开头"), ("begin by saying hello", "先打招呼")], [("The book begins with a short story.", "这本书以一个短故事开头。"), ("She began by thanking the audience.", "她首先感谢了观众。")], "open with：也表示以某事开场；begin with 更通用。", "end with：以某事结尾。", "begin with 后接事物；begin by 后常接 doing。"),
        ],
    },
    "believe": {
        "phonetic": "/bɪˈliːv/", "syllables": ["be", "lieve"], "pos": ["v."],
        "core_meanings": ["相信属实", "信任", "相信某种价值"],
        "etymology": "源自古英语表示“信任、相信”的词形；与日耳曼语系中的“珍视、喜爱”词根有关。",
        "semantic_shift": "从信任某人，扩展为认为某句话属实，以及认同某种理念或可能性。",
        "senses": [
            sense(1, "v.", "to think that something is true", "认为某件事属实", "相信事实", [("believe the story", "相信这个故事"), ("believe that it is true", "相信这是真的")], [("I believe your story.", "我相信你的说法。"), ("She believes that the plan will work.", "她相信这个计划会奏效。")], "think：可表示认为；believe 更强调把某事当作真实的。", "doubt：怀疑。", "believe someone 是相信对方说的话；believe in someone 是信任其能力。"),
            sense(2, "v.", "to trust a person's ability or character", "信任一个人的能力或品格", "信任某人", [("believe in yourself", "相信自己"), ("believe in a friend", "信任朋友")], [("I believe in your ability to succeed.", "我相信你有成功的能力。"), ("Her parents always believed in her.", "她的父母一直信任她。")], "trust：直接指信任；believe in 还强调相信对方的潜力。", "distrust：不信任。", "believe her 是相信她的话；believe in her 是相信她这个人。"),
            sense(3, "v.", "to accept an idea or principle as important", "认同某种理念或原则", "信奉理念", [("believe in fairness", "信奉公平"), ("believe in hard work", "相信努力的价值")], [("He believes in equal chances for all.", "他认同人人机会均等的理念。"), ("We believe in working together.", "我们相信合作的价值。")], "value：表示重视；believe in 强调信奉或认同。", "reject a principle：拒绝某种原则。", "believe in fairness 是认同公平的价值，不是在判断公平是否存在。"),
        ],
    },
    "benefit": {
        "phonetic": "/ˈbenəfɪt/", "syllables": ["ben", "e", "fit"], "pos": ["n.", "v."],
        "core_meanings": ["好处", "福利", "受益"],
        "etymology": "经法语相关词形来自拉丁语 benefactum“善行”，由 bene“好”与 facere“做”构成。",
        "semantic_shift": "从对人有益的行为，扩展到得到的好处；动词表示某人因此受益。",
        "senses": [
            sense(1, "n.", "something good that helps a person or situation", "对人或情况有帮助的好处", "好处", [("health benefits", "健康益处"), ("the main benefit", "主要好处")], [("Exercise has many health benefits.", "运动对健康有很多好处。"), ("The main benefit is more free time.", "主要好处是有更多空闲时间。")], "advantage：常强调相对优势；benefit 强调实际得到的好处。", "drawback：缺点或不利之处。", "benefit 可数时指一项具体好处；泛指受益也可不可数。"),
            sense(2, "n.", "money or services provided through a job or program", "工作或计划提供的补贴或服务", "福利待遇", [("employee benefits", "员工福利"), ("medical benefits", "医疗福利")], [("This job offers good benefits.", "这份工作提供不错的福利。"), ("Her medical benefits cover the visit.", "她的医疗福利支付这次就诊的费用。")], "perk：常指额外的小福利；benefits 可包括正式医疗等保障。", "", "此义常用复数 benefits，通常不指一般性的“好处”。"),
            sense(3, "v.", "to gain something helpful from an action or situation", "从行动或情况中得到好处", "受益", [("benefit from practice", "从练习中受益"), ("benefit from exercise", "从运动中受益")], [("Students benefit from regular practice.", "学生能从经常练习中受益。"), ("The town benefited from the new road.", "这座小镇因新路而受益。")], "gain from：也指从中获得好处；benefit 更简洁。", "suffer from：因某事受损。", "benefit from 后接好处来源；benefit someone 是使某人受益。"),
            sense(4, "v.", "to make someone or something better off", "使某人或某事获益", "使……受益", [("benefit local people", "让当地居民受益"), ("benefit the environment", "有益于环境")], [("The new library benefits local people.", "新图书馆让当地居民受益。"), ("This change will benefit the environment.", "这项改变将有益于环境。")], "help：泛指帮助；benefit 强调带来实际好处。", "harm：造成损害。", "benefit people 直接接受益者；people benefit from something 用 from。"),
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
