"""Third group of original pilot candidates: address through amount."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "address": {
        "phonetic": "/əˈdres/", "syllables": ["ad", "dress"], "pos": ["n.", "v."],
        "core_meanings": ["地址", "写地址", "向……讲话", "处理问题"],
        "etymology": "动词经古法语 adrecier 进入英语，原有“朝某方向引导”之意；名词由动词发展。",
        "semantic_shift": "从把人或物引向目标，扩展为标明送达地点、把话说给某人听，以及着手处理一个问题。",
        "senses": [
            sense(1, "n.", "the details of where someone lives or works", "住处或工作地点的具体地址", "邮寄地址", [("home address", "家庭住址"), ("mailing address", "邮寄地址")], [("Please write your address here.", "请在这里写下你的地址。"), ("I sent the book to her new address.", "我把书寄到了她的新地址。")], "location：泛指位置；address 是可用于联系或投递的具体信息。", "", "名词 address 也常读 /ˈædres/；电子邮件地址见下一义项。"),
            sense(2, "n.", "the identifying information for an email account or website", "电子邮箱或网站的地址信息", "数字地址", [("email address", "电子邮件地址"), ("web address", "网站地址")], [("Please enter your email address.", "请输入你的电子邮件地址。"), ("The web address is on the poster.", "网站地址印在海报上。")], "URL：专指网页地址；address 还可指电子邮箱地址。", "", "email address 是电子邮箱地址，不能用来邮寄包裹。"),
            sense(3, "v.", "to write a destination on a letter or package", "在信件或包裹上写收件地址", "写收件地址", [("address an envelope", "在信封上写地址"), ("address a package to someone", "在包裹上写某人为收件人")], [("She addressed the envelope carefully.", "她仔细写好信封上的地址。"), ("Address the package to my office.", "请在包裹上填写我的办公室地址。")], "label：泛指贴标签；address 特指写明投递目的地。", "leave unaddressed：不写收件地址。", "address a letter to someone 是写收件人，不是向此人讲话。"),
            sense(4, "v.", "to speak to a person or group", "对个人或群体讲话", "发表讲话", [("address the audience", "向观众讲话"), ("address a meeting", "在会议上讲话")], [("The principal addressed the students.", "校长向学生们讲话。"), ("She addressed the meeting in English.", "她用英语在会上发言。")], "speak to：一般说“对……说话”；address 常用于较正式的讲话。", "", "address someone 在此是对其讲话，不是写其地址。"),
            sense(5, "v.", "to deal with a problem or question", "处理问题或回应疑问", "处理问题", [("address a problem", "处理问题"), ("address a concern", "回应担忧")], [("We need to address this problem now.", "我们现在需要处理这个问题。"), ("The report addresses our main concerns.", "这份报告回应了我们主要的担忧。")], "deal with：泛指处理；address 强调正面着手处理或回应。", "ignore：置之不理。", "address a problem 是处理问题，不是给问题写地址。"),
        ],
    },
    "allow": {
        "phonetic": "/əˈlaʊ/", "syllables": ["al", "low"], "pos": ["v."],
        "core_meanings": ["允许", "使可能", "考虑到"],
        "etymology": "中古英语中相关法语词形相互融合，一支与拉丁语 allocare“分配”有关，另一支与“赞许”有关。",
        "semantic_shift": "从认可并给予，发展为准许某事；给予条件也可以让事情成为可能。",
        "senses": [
            sense(1, "v.", "to give someone permission to do something", "允许某人做某事", "允许", [("allow someone to enter", "允许某人进入"), ("not allowed", "不被允许")], [("My parents allow me to go out.", "父母允许我外出。"), ("Visitors are not allowed to park here.", "访客不得在这里停车。")], "permit：也表示允许，语气通常更正式；allow 更日常。", "forbid：禁止。", "allow someone to do 中必须有 to；不能说 allow someone do。"),
            sense(2, "v.", "to make something possible", "提供条件，使某事成为可能", "使可能", [("allow easy access", "方便进入或使用"), ("allow someone to learn", "使某人能够学习")], [("This app allows users to study anywhere.", "这款应用让用户能在任何地方学习。"), ("The new road allows faster travel.", "新路使出行更快捷。")], "enable：强调赋予能力或条件；allow 此处也表示使可能。", "prevent：阻止某事发生。", "allow 在这里不一定涉及批准或许可。"),
            sense(3, "v.", "to take possible needs into account and leave enough time or resources", "把可能情况考虑在内并留出所需时间或资源", "预留余地", [("allow for delays", "把延误考虑进去"), ("allow enough time", "留足时间")], [("Allow extra time for the journey.", "这趟行程要多留些时间。"), ("We must allow for possible delays.", "我们必须把可能的延误考虑进去。")], "plan for：指提前作计划；allow for 强调把可能情况算在内。", "overlook：忽略需要考虑的因素。", "allow for delays 是预留余地，不是“批准延误”。"),
        ],
    },
    "almost": {
        "phonetic": "/ˈɔːlmoʊst/", "syllables": ["al", "most"], "pos": ["adv."],
        "core_meanings": ["几乎", "差不多"],
        "etymology": "源自古英语 eallmæst，由表示“全部”的 all 与 most 组合而成。",
        "semantic_shift": "早期表示“几乎全部”，后来也用于数量、程度或动作快要达到某个点。",
        "senses": [
            sense(1, "adv.", "very nearly but not completely", "非常接近，但尚未完全达到", "几乎", [("almost ready", "差不多准备好了"), ("almost everyone", "几乎所有人")], [("We are almost ready to leave.", "我们差不多准备好出发了。"), ("Almost everyone agreed with her.", "几乎所有人都同意她的看法。")], "nearly：意思很接近；almost 可自然修饰 every、all、always 等词。", "exactly：表示恰好达到某个数字或程度。", "almost everyone 是“几乎所有人”，不能写 most almost people。"),
        ],
    },
    "among": {
        "phonetic": "/əˈmʌŋ/", "syllables": ["a", "mong"], "pos": ["prep."],
        "core_meanings": ["在……之中", "在……之间"],
        "etymology": "源自古英语 on gemang，字面上与“混在一群之中”有关。",
        "semantic_shift": "先表示处在一群人或物中间，也可说某人或某事属于这个群体。",
        "senses": [
            sense(1, "prep.", "surrounded by several people or things", "被一群人或物围在中间", "处在一群之中", [("among the trees", "在树丛中"), ("among friends", "在朋友当中")], [("We sat among the trees.", "我们坐在树丛中。"), ("She felt safe among friends.", "她在朋友中间感到安心。")], "amid：也表示处于其中，语气较书面；among 更常用于可数的人或物。", "outside：在……外面。", "among 常用于群体；between 也可用于两个以上对象之间的明确关系。"),
            sense(2, "prep.", "as one of a group", "作为群体中的一员", "属于其中", [("among the best", "名列前茅"), ("among those invited", "在受邀者之列")], [("This book is among my favorites.", "这本书是我最喜欢的书之一。"), ("He was among those invited.", "他也是受邀者之一。")], "one of：直接说是其中之一；among 强调身在某个群体里。", "excluded from：被排除在群体之外。", "among the best 表示优秀者之一，不一定是唯一最好的。"),
        ],
    },
    "amount": {
        "phonetic": "/əˈmaʊnt/", "syllables": ["a", "mount"], "pos": ["n.", "v."],
        "core_meanings": ["数量", "总额", "总计达到", "相当于"],
        "etymology": "源自古法语 amonter“向上升”；英语中的名词“数量、总额”由动词发展。",
        "semantic_shift": "从数量逐渐升高到某个点，发展为总计达到一个数；这个结果也可以比喻为相当于某种行为。",
        "senses": [
            sense(1, "n.", "a quantity of something", "某种事物的数量", "数量", [("a large amount of water", "大量的水"), ("a small amount of time", "一点时间")], [("Use a small amount of salt.", "用少量盐。"), ("The amount of rain surprised us.", "降雨量让我们感到意外。")], "quantity：也指数量；amount 常搭配不可数名词。", "none：一点也没有。", "a number of 后接可数名词复数；an amount of 常接不可数名词。"),
            sense(2, "n.", "a total sum of money", "钱款的总额", "金额", [("the total amount", "总金额"), ("an amount due", "应付金额")], [("Please check the amount on the bill.", "请核对账单上的金额。"), ("The full amount is due tomorrow.", "全款明天到期。")], "sum：可指一笔钱；amount 更强调合计后的数额。", "", "amount 在账单里通常是“金额”，不是物品的数量。"),
            sense(3, "v.", "to add up to a total", "合计达到某个数额", "总计达到", [("amount to $100", "总计一百美元"), ("amount to several hours", "总共持续几个小时")], [("The costs amount to $100.", "费用总计一百美元。"), ("The delays amounted to several hours.", "延误总共持续了好几个小时。")], "total：直接表示总计；amount to 强调加起来达到某个数。", "fall short of：没有达到某个总数。", "amount to 后接总数或程度，不直接接宾语。"),
            sense(4, "v.", "to be effectively the same as something", "实际上相当于某事", "相当于", [("amount to a refusal", "等于拒绝"), ("amount to a promise", "等于作出承诺")], [("His silence amounted to a refusal.", "他的沉默等于拒绝。"), ("That answer amounts to a promise.", "那个回答等于作出了承诺。")], "be equivalent to：更明确地表示等同；amount to 常指实际效果。", "differ from：与某事不同。", "此义的 amount to 不表示具体金额。"),
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
