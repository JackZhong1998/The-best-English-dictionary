"""Original pilot candidates: decide, develop, difference, effect, effort.

This script writes candidate JSON only. Staging and review are separate steps.
"""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "decide": {
        "phonetic": "/dɪˈsaɪd/", "syllables": ["de", "cide"], "pos": ["v."],
        "core_meanings": ["决定", "使结果确定"],
        "etymology": "经古法语 decider，来自拉丁语 decidere“切断、作出决定”。",
        "semantic_shift": "从把犹豫的可能性“切开”，发展为作出选择；决定性的因素也可以使结果确定。",
        "senses": [
            sense(1, "v.", "to choose after thinking about possibilities", "考虑各种可能后作出选择", "作出决定", [("decide to leave", "决定离开"), ("decide on a date", "定下日期")], [("We decided to take the train.", "我们决定坐火车。"), ("Have you decided on a date yet?", "你定好日期了吗？")], "choose：强调从选项中挑一个；decide 更强调最终作出决定。", "remain undecided：尚未决定。", "decide to 后接动词；decide on 后接所选事物。"),
            sense(2, "v.", "to determine the result of something", "使某事的结果得到确定", "决定结果", [("decide the winner", "决定胜者"), ("decide the outcome", "决定结果")], [("One goal decided the match.", "一个进球决定了比赛胜负。"), ("The final vote will decide the outcome.", "最后一轮投票将决定结果。")], "determine：也表示决定结果，语气较正式。", "", "此义的主语可以是进球或投票，不一定是作选择的人。"),
        ],
    },
    "develop": {
        "phonetic": "/dɪˈveləp/", "syllables": ["de", "vel", "op"], "pos": ["v."],
        "core_meanings": ["发展", "开发", "逐渐形成"],
        "etymology": "源自法语 développer“展开、揭开”；其中表示“包裹”的旧词部分更早来源不确定。",
        "semantic_shift": "从把包裹的东西展开，发展为让潜力逐渐显现，以及事物随时间形成。",
        "senses": [
            sense(1, "v.", "to grow or change over time", "随时间成长或变化", "发展", [("develop quickly", "快速发展"), ("develop into an adult", "长大成人")], [("The town developed quickly.", "这座小镇发展得很快。"), ("Children develop at different speeds.", "孩子们的发展速度各不相同。")], "grow：泛指生长或增大；develop 更强调逐步变化和成熟。", "stop developing：停止发展。", "develop 可不接宾语，表示事物自身逐渐发展。"),
            sense(2, "v.", "to design and make a new product or idea", "设计并制作新的产品或想法", "开发", [("develop an app", "开发应用"), ("develop a new method", "开发新方法")], [("They developed a new study app.", "他们开发了一款新的学习应用。"), ("Our team developed a safer method.", "我们团队开发了一种更安全的方法。")], "create：强调从无到有；develop 常包含反复设计和改进。", "", "develop an app 指开发应用，不是下载或安装应用。"),
            sense(3, "v.", "to begin to have a quality, habit, or illness", "逐渐形成特征、习惯或疾病", "逐渐形成", [("develop a habit", "养成习惯"), ("develop a fever", "开始发烧")], [("She developed a habit of reading daily.", "她养成了每天阅读的习惯。"), ("He developed a fever overnight.", "他一夜之间发烧了。")], "acquire：泛指获得；develop 更强调逐渐形成。", "lose a habit：失去某种习惯。", "develop a fever 是开始发烧，不是“研发发烧”。"),
        ],
    },
    "difference": {
        "phonetic": "/ˈdɪfərəns/", "syllables": ["dif", "fer", "ence"], "pos": ["n."],
        "core_meanings": ["差别", "差额", "影响"],
        "etymology": "经古法语 difference，来自拉丁语 differentia“差异、区别”。",
        "semantic_shift": "从两个事物不相同，发展为数值上的差额；make a difference 表示这种差异足以影响结果。",
        "senses": [
            sense(1, "n.", "a way in which two things are not the same", "两个事物不相同的地方", "差别", [("a big difference", "很大的差别"), ("the difference between A and B", "A 与 B 的差别")], [("I can see the difference between the two pictures.", "我能看出这两幅画的区别。"), ("There is a big difference in price.", "价格有很大差别。")], "distinction：也表示区别，常强调分类时的界线。", "similarity：相似之处。", "the difference between 后通常接两个被比较对象。"),
            sense(2, "n.", "the amount by which two numbers differ", "两个数字相差的数量", "差额", [("a difference of ten dollars", "十美元的差额"), ("calculate the difference", "算出差额")], [("The difference is only two dollars.", "两者只差两美元。"), ("Please calculate the difference between the totals.", "请算出两个总数的差额。")], "gap：也可指数量上的差距；difference 常指可计算的相差量。", "", "这里的 difference 是数值差，不只是外观不同。"),
            sense(3, "n.", "a noticeable effect on a situation", "对某种情况产生明显影响", "产生影响", [("make a difference", "产生影响"), ("make a big difference", "产生很大影响")], [("One kind word can make a difference.", "一句善意的话也能产生影响。"), ("The new road made a big difference.", "新路带来了很大改变。")], "impact：直接表示影响；make a difference 强调结果因之不同。", "make no difference：没有影响。", "make a difference 是固定搭配，不必出现两个可比较的物品。"),
        ],
    },
    "effect": {
        "phonetic": "/ɪˈfekt/", "syllables": ["ef", "fect"], "pos": ["n."],
        "core_meanings": ["结果", "影响", "特效"],
        "etymology": "经古法语 efet，来自拉丁语 effectus“完成、产生的结果”。",
        "semantic_shift": "从做成一件事，发展为行动造成的结果；在电影等语境中又指刻意制造的视觉或声音效果。",
        "senses": [
            sense(1, "n.", "a change produced by a cause", "某个原因带来的变化", "结果或影响", [("have an effect on", "对……有影响"), ("a positive effect", "积极影响")], [("Sleep has a strong effect on memory.", "睡眠对记忆有很大影响。"), ("The change had a positive effect.", "这项改变产生了积极效果。")], "result：强调最终结果；effect 可指原因造成的任何作用。", "cause：产生作用的原因。", "effect 常是名词；affect 常是表示“影响”的动词。"),
            sense(2, "n.", "a particular impression created deliberately", "刻意营造出的特定效果", "效果", [("create an effect", "营造效果"), ("a dramatic effect", "戏剧性效果")], [("The lighting created a warm effect.", "灯光营造出温暖的效果。"), ("The music added a dramatic effect to the scene.", "音乐给这一幕增添了戏剧效果。")], "impression：指给人的总体印象；effect 常强调设计产生的效果。", "", "此义的 effect 常与灯光、色彩、音乐等手段连用。"),
            sense(3, "n.", "a visual or sound feature added to a film or show", "为电影或演出制作的画面或声音效果", "特效", [("special effects", "特效"), ("sound effects", "音效")], [("The film has impressive special effects.", "这部电影的特效令人印象深刻。"), ("They added sound effects to the game.", "他们给游戏加入了音效。")], "animation：指动画制作；effects 也可用于真人影片。", "", "special effects 通常用复数，指具体制作出的特效。"),
        ],
    },
    "effort": {
        "phonetic": "/ˈefərt/", "syllables": ["ef", "fort"], "pos": ["n."],
        "core_meanings": ["努力", "尝试"],
        "etymology": "经法语 effort，来自表示“用力”的旧词，与拉丁语 fortis“强壮”有关。",
        "semantic_shift": "从用力，扩展到为目标投入的体力或心力；一次具体努力也可指一次尝试。",
        "senses": [
            sense(1, "n.", "physical or mental energy used to do something", "做事投入的体力或心力", "努力", [("make an effort", "作出努力"), ("a lot of effort", "大量心力")], [("Learning a language takes effort.", "学习一门语言需要付出努力。"), ("She put a lot of effort into the project.", "她在这个项目上投入了很多心力。")], "work：泛指工作；effort 强调投入的力量。", "lack of effort：缺乏努力。", "put effort into 后接投入心力的事情。"),
            sense(2, "n.", "an attempt to achieve something", "为达成目标而作的一次尝试", "尝试", [("an effort to save time", "为节省时间所作的努力"), ("a final effort", "最后一次努力")], [("Their effort to save the tree succeeded.", "他们努力保住这棵树，最后成功了。"), ("In a final effort, she called for help.", "最后她又试了一次，打电话求助。")], "attempt：强调试一试；effort 通常也强调投入的心力。", "give up：放弃尝试。", "an effort to do 后接动词原形；make an effort 是作出努力。"),
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
