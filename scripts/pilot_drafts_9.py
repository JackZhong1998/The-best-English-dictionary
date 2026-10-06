"""Original pilot candidates: contain, continue, control, create, culture."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "contain": {
        "phonetic": "/kənˈteɪn/", "syllables": ["con", "tain"], "pos": ["v."],
        "core_meanings": ["容纳", "包含", "控制蔓延"],
        "etymology": "经古法语 contenir，来自拉丁语 continere“合在一起、围住”。",
        "semantic_shift": "从把东西围在一个范围里，发展为容器装有东西、整体包含部分，也可指把危险限制在范围内。",
        "senses": [
            sense(1, "v.", "to have something inside", "内部装有某物", "容纳", [("contain water", "装水"), ("a box containing books", "装着书的箱子")], [("This bottle contains water.", "这个瓶子里装着水。"), ("The box contains old photos.", "盒子里装着旧照片。")], "hold：也指容纳；contain 强调内容物在内部。", "", "contain 的主语常是容器，宾语是里面的东西。"),
            sense(2, "v.", "to include something as a part", "把某物作为组成部分包括在内", "包含成分", [("contain sugar", "含糖"), ("contain useful information", "包含有用信息")], [("This drink contains no sugar.", "这种饮料不含糖。"), ("The report contains useful information.", "报告包含有用的信息。")], "include：强调把某项算在内；contain 常强调它是内容或成分。", "exclude：不包括。", "contain sugar 说的是成分，不是瓶子里装着一袋糖。"),
            sense(3, "v.", "to stop something dangerous from spreading", "阻止危险事物向外扩散", "控制蔓延", [("contain a fire", "控制火势"), ("contain the spread", "遏制扩散")], [("Firefighters contained the fire by morning.", "消防员在早上控制住了火势。"), ("The town acted quickly to contain the spread.", "镇上迅速采取行动遏制扩散。")], "limit：泛指限制范围；contain 更强调不让它向外蔓延。", "let it spread：任其扩散。", "contain a fire 是阻止火势扩散，不是把火放进盒子。"),
        ],
    },
    "continue": {
        "phonetic": "/kənˈtɪnjuː/", "syllables": ["con", "tin", "ue"], "pos": ["v."],
        "core_meanings": ["继续", "持续", "接着做"],
        "etymology": "经古法语 continuer，来自拉丁语 continuare“使连续不断”。",
        "semantic_shift": "从一段接着一段而不断开，发展为动作继续、状态持续；短暂停下后也可接着做。",
        "senses": [
            sense(1, "v.", "to keep doing something", "不中断地继续做某事", "继续做", [("continue working", "继续工作"), ("continue to study", "继续学习")], [("Please continue reading the story.", "请继续读这个故事。"), ("She continued to work after lunch.", "午饭后她继续工作。")], "keep：口语中也表示继续；continue 较中性、正式。", "stop：停止。", "continue 后可接 doing 或 to do，两者常都可用。"),
            sense(2, "v.", "to remain in the same state for a period", "某种状态持续一段时间", "持续", [("the rain continues", "雨仍在下"), ("continue for hours", "持续数小时")], [("The rain continued all night.", "雨下了一整夜。"), ("The noise continued for hours.", "噪声持续了好几个小时。")], "last：强调持续时间；continue 强调没有结束。", "end：指事件或状态终止，与 continue 表示持续相对。", "The rain continued 中的 continue 没有宾语。"),
            sense(3, "v.", "to begin again after a pause", "暂停后接着进行", "暂停后继续", [("continue after a break", "休息后继续"), ("continue the lesson", "接着上课")], [("We continued the game after the rain.", "雨停后我们接着比赛。"), ("The teacher continued the lesson after lunch.", "午饭后老师接着上课。")], "resume：明确指暂停后恢复；continue 也可表示从停下处接着做。", "pause：暂停。", "continue 在这里暗示前面已经开始过，不是首次开始。"),
        ],
    },
    "control": {
        "phonetic": "/kənˈtroʊl/", "syllables": ["con", "trol"], "pos": ["v.", "n."],
        "core_meanings": ["控制", "管理", "控制权", "控制装置"],
        "etymology": "经法语词形进入英语，早期与用副本核对账目有关，后来发展出管理、支配义。",
        "semantic_shift": "从检查、核对，扩展到指挥事物如何运行，再到对过程或情绪施加约束。",
        "senses": [
            sense(1, "v.", "to direct how someone or something acts", "决定人或事物如何行动", "控制或管理", [("control a machine", "控制机器"), ("control traffic", "指挥交通")], [("This button controls the machine.", "这个按钮控制机器。"), ("The police controlled traffic near the school.", "警察在学校附近指挥交通。")], "manage：强调负责安排；control 更强调决定或限制运行方式。", "lose control：失去控制。", "control 作动词直接接对象，如 control a machine。"),
            sense(2, "v.", "to limit the strength or spread of something", "限制某种力量或事物的蔓延", "抑制", [("control your anger", "控制怒气"), ("control a fire", "控制火势")], [("He tried to control his anger.", "他努力控制自己的怒气。"), ("The crew controlled the fire quickly.", "消防队很快控制住了火势。")], "restrain：常指克制冲动；control 适用范围更广。", "let loose：放任不管。", "control a fire 是控制火势，不是让火按指令行动。"),
            sense(3, "n.", "the power to direct a situation", "指挥或决定局势的权力", "控制权", [("have control over", "对……有控制权"), ("take control of", "掌控……")], [("She has control over the budget.", "她掌握预算的决定权。"), ("The team took control of the project.", "团队接管了这个项目。")], "authority：强调正式权力；control 也可以是实际掌控力。", "loss of control：失去控制权。", "have control over 中的 over 后接被控制的事物。"),
            sense(4, "n.", "a device used to operate a machine", "操作机器的装置", "控制装置", [("remote control", "遥控器"), ("volume control", "音量控制键")], [("I cannot find the remote control.", "我找不到遥控器。"), ("Use this control to lower the volume.", "用这个控制键调低音量。")], "switch：通常是开关；control 可用于调节多种功能。", "", "remote control 指遥控器，和“控制权”不是同一具体物品。"),
        ],
    },
    "create": {
        "phonetic": "/kriˈeɪt/", "syllables": ["cre", "ate"], "pos": ["v."],
        "core_meanings": ["创造", "创建", "造成"],
        "etymology": "来自拉丁语 creare“产生、造出”，与生长相关的词族有关。",
        "semantic_shift": "从使新事物产生，扩展到制作作品或建立组织；抽象结果也可以被“造成”。",
        "senses": [
            sense(1, "v.", "to make something new", "创造出新的东西", "创造", [("create a story", "创作故事"), ("create art", "创作艺术作品")], [("She created a story for the children.", "她为孩子们创作了一个故事。"), ("The students created their own games.", "学生们设计了自己的游戏。")], "make：泛指制作；create 更强调产生新的想法或作品。", "destroy：毁掉已经存在的东西。", "create 常强调新意，make 的使用范围更广。"),
            sense(2, "v.", "to establish a new organization or system", "建立新的组织或系统", "创建", [("create a website", "创建网站"), ("create a team", "组建团队")], [("They created a website for the club.", "他们为俱乐部创建了网站。"), ("We created a small study group.", "我们组建了一个小学习小组。")], "set up：也指建立，较口语；create 常强调从无到有。", "close down：关闭组织或系统。", "create an account 是创建账号，不是创作一篇文章。"),
            sense(3, "v.", "to cause a situation or feeling", "造成某种局面或感受", "造成", [("create problems", "制造问题"), ("create interest", "引起兴趣")], [("The delay created problems for us.", "延误给我们造成了麻烦。"), ("The pictures created interest in the show.", "这些图片激起了人们对演出的兴趣。")], "cause：直接表示导致；create 强调新的局面由此出现。", "prevent：防止某事出现。", "create problems 不是设计一个实体产品，而是造成问题。"),
        ],
    },
    "culture": {
        "phonetic": "/ˈkʌltʃər/", "syllables": ["cul", "ture"], "pos": ["n."],
        "core_meanings": ["文化", "群体风气"],
        "etymology": "来自拉丁语 cultura“耕作、培育”，后来用于人的教育和社会生活。",
        "semantic_shift": "从培育土地转为培育心智，再指一个群体共有的习惯、观念与艺术。",
        "senses": [
            sense(1, "n.", "the ideas, customs, and art of a society", "一个社会共有的观念、习俗和艺术", "社会文化", [("local culture", "当地文化"), ("learn about a culture", "了解一种文化")], [("Food is part of local culture.", "饮食是当地文化的一部分。"), ("She studies the culture of the region.", "她研究这个地区的文化。")], "tradition：强调代代相传的做法；culture 范围更广。", "", "culture 不只指艺术，也包括日常习俗和观念。"),
            sense(2, "n.", "the shared way people behave in a group", "群体成员共有的行事方式", "群体风气", [("school culture", "学校风气"), ("workplace culture", "职场文化")], [("The school has a culture of teamwork.", "这所学校有重视合作的风气。"), ("A healthy workplace culture helps everyone.", "健康的职场氛围对大家都有帮助。")], "atmosphere：偏重当下氛围；culture 指较稳定的共同习惯。", "", "workplace culture 是工作场所的共同风气，不是一个国家的文化。"),
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
