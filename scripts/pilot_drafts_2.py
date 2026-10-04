"""Second group of five original, unreviewed pilot candidates."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "activity": {
        "phonetic": "/ækˈtɪvəti/", "syllables": ["ac", "tiv", "i", "ty"], "pos": ["n."],
        "core_meanings": ["活动", "活跃状态"],
        "etymology": "经古法语 activité，最终与拉丁语 activus“行动的”有关。",
        "semantic_shift": "从行动的状态，扩展到一项具体安排好的活动。",
        "senses": [
            sense(1, "n.", "things that people do, especially organized events", "人们参加的活动，尤指有组织的活动", "具体活动", [("school activities", "学校活动"), ("outdoor activities", "户外活动")], [("The school offers many activities.", "学校提供许多活动。"), ("Walking is a simple outdoor activity.", "散步是一项简单的户外活动。")], "event：通常是一场特定事件；activity 可以是持续或重复的活动。", "inactivity：缺少活动的状态。", "activity 可数时指一项活动；activities 是其复数。"),
            sense(2, "n.", "a state of movement or action", "活动或活跃的状态", "活动状态", [("physical activity", "身体活动"), ("a period of activity", "一段活跃期")], [("Regular physical activity is good for you.", "经常进行身体活动对你有好处。"), ("There was little activity in the street.", "街上几乎没有什么动静。")], "movement：偏重实际移动；activity 可泛指一切活动迹象。", "stillness：静止状态。", "此义的 activity 通常不可数，不说 many activities 来表示活动量。"),
        ],
    },
    "advantage": {
        "phonetic": "/ədˈvæntɪdʒ/", "syllables": ["ad", "van", "tage"], "pos": ["n."],
        "core_meanings": ["优势", "有利条件", "利用"],
        "etymology": "经古法语 avantage 进入英语，早期指“领先于他人的位置”。",
        "semantic_shift": "从站在前方的有利位置，扩展为帮助人取得好结果的条件。",
        "senses": [
            sense(1, "n.", "a condition that helps someone succeed", "有助于取得成功的条件", "优势", [("a clear advantage", "明显优势"), ("have an advantage over", "比……有优势")], [("Experience gives her an advantage.", "经验让她占有优势。"), ("Our team has an advantage over theirs.", "我们的队伍比他们的队伍更有优势。")], "benefit：强调得到的好处；advantage 常强调比较中的有利条件。", "disadvantage：不利条件。", "advantage over someone 表示相对于某人的优势。"),
            sense(2, "n.", "a useful feature of something", "某物的优点", "优点", [("the main advantage", "主要优点"), ("advantages and disadvantages", "优点与缺点")], [("The main advantage is its low price.", "它的主要优点是价格低。"), ("Every method has advantages and disadvantages.", "每种方法都有优缺点。")], "strength：可指人或事物的强项；advantage 更强调带来的好处。", "disadvantage：缺点或不利之处。", "advantage 是名词；advantageous 是形容词。"),
            sense(3, "n.", "a benefit gained by making use of an opportunity", "利用机会得到的好处", "利用机会", [("take advantage of a chance", "利用一次机会"), ("take advantage of free lessons", "利用免费课程")], [("We took advantage of the free lesson.", "我们利用了这节免费课。"), ("She took advantage of the break to call home.", "她趁休息时间给家里打了电话。")], "make use of：中性地表示利用；take advantage of 也强调由此得到好处。", "miss an opportunity：错过机会。", "take advantage of an opportunity 是利用机会，不一定含负面意思。"),
            sense(4, "n.", "an unfair benefit gained from another person", "从他人身上不公平地取得好处", "占人便宜", [("take advantage of someone", "占某人便宜"), ("take advantage of someone's kindness", "利用某人的善良")], [("Do not take advantage of her kindness.", "不要利用她的善良占便宜。"), ("The seller took advantage of tourists.", "那个商贩占了游客的便宜。")], "exploit：明确表示剥削或利用；take advantage of someone 是常用说法。", "treat someone fairly：公平对待某人。", "take advantage of someone 通常是负面的；利用机会则不一定。"),
        ],
    },
    "affect": {
        "phonetic": "/əˈfekt/", "syllables": ["af", "fect"], "pos": ["v."],
        "core_meanings": ["影响", "打动"],
        "etymology": "与拉丁语 afficere“对……产生作用”及其过去分词 affectus 有关。",
        "semantic_shift": "从外界对人或物施加作用，扩展到影响结果和触动感情。",
        "senses": [
            sense(1, "v.", "to cause a change in someone or something", "对人或事物产生影响", "影响", [("affect the result", "影响结果"), ("affect people's lives", "影响人们的生活")], [("The weather may affect our plans.", "天气可能影响我们的计划。"), ("This change will affect many students.", "这一变化将影响许多学生。")], "influence：也表示影响；affect 更直接指产生了作用或变化。", "leave unchanged：使保持原状。", "affect 通常是动词；effect 常是名词，表示结果或影响。"),
            sense(2, "v.", "to make someone feel a strong emotion", "深深触动某人的情绪", "打动", [("be deeply affected", "深受触动"), ("affect someone emotionally", "在情感上影响某人")], [("Her story deeply affected me.", "她的故事深深打动了我。"), ("The news affected him more than I expected.", "这个消息对他的触动比我预想的更大。")], "move：常表示使人感动；affect 可以指各种强烈情绪。", "leave unmoved：使人无动于衷。", "be affected by 可以表示受影响，不一定是“被感动”。"),
        ],
    },
    "afford": {
        "phonetic": "/əˈfɔːrd/", "syllables": ["af", "ford"], "pos": ["v."],
        "core_meanings": ["买得起", "承担得起", "提供"],
        "etymology": "源自古英语 geforðian“推动、完成”，后来产生“有能力承担费用”的用法。",
        "semantic_shift": "从有能力完成，发展为有足够的钱、时间或条件去做；也可说某物提供机会。",
        "senses": [
            sense(1, "v.", "to have enough money to pay for something", "有足够的钱支付", "买得起", [("afford a car", "买得起汽车"), ("cannot afford the rent", "付不起房租")], [("We cannot afford a new car.", "我们买不起新车。"), ("Can you afford the monthly rent?", "你付得起每月的房租吗？")], "pay for：只说付款；afford 强调有足够财力。", "be unable to afford：负担不起。", "afford 后直接接名词；说“买得起”时不用 afford for。"),
            sense(2, "v.", "to have enough time or resources for something", "有足够的时间或余力做某事", "承担得起", [("cannot afford to wait", "等不起"), ("can afford to be patient", "有余地耐心等待")], [("We cannot afford to waste time.", "我们浪费不起时间。"), ("I can afford to wait a week.", "我等得起一个星期。")], "spare：强调腾出时间或资源；afford 强调是否承担得起代价。", "", "afford to do 后接动词原形，常见于否定句。"),
            sense(3, "v.", "to provide someone with an opportunity", "为某人提供机会", "提供机会", [("afford an opportunity", "提供机会"), ("afford someone the opportunity to learn", "给某人学习的机会")], [("The course affords students new opportunities.", "这门课为学生提供了新机会。"), ("This trip afforded us a chance to talk.", "这次旅行给了我们交谈的机会。")], "provide：更常用的“提供”；afford 此义偏正式。", "deny an opportunity：不给予机会。", "此义中 afford 不涉及花钱，而是“提供”。"),
        ],
    },
    "agree": {
        "phonetic": "/əˈɡriː/", "syllables": ["a", "gree"], "pos": ["v."],
        "core_meanings": ["同意", "商定", "一致"],
        "etymology": "经古法语 agreer 进入英语，早期有“使满意、乐意接受”之意。",
        "semantic_shift": "从觉得某事合意，扩展到与人意见相同，或共同决定要做的事。",
        "senses": [
            sense(1, "v.", "to have the same opinion as someone", "与某人意见相同", "意见一致", [("agree with someone", "同意某人的看法"), ("agree on a point", "在一点上意见一致")], [("I agree with your idea.", "我同意你的想法。"), ("We agree on this point.", "我们在这一点上意见一致。")], "concur：也表示同意，语气更正式；agree 更日常。", "disagree：意见不同。", "agree with 后接人或观点；agree on 后接共同商定的事项。"),
            sense(2, "v.", "to say yes to a plan or request", "答应某个计划或请求", "答应", [("agree to help", "答应帮忙"), ("agree to a plan", "同意计划")], [("She agreed to help us.", "她答应帮助我们。"), ("They agreed to the new plan.", "他们同意了新计划。")], "accept：表示接受提议；agree to 侧重表示同意。", "refuse：拒绝答应。", "agree to do 后接动词；agree with someone 后接人。"),
            sense(3, "v.", "to match or be consistent with something", "与某事相符", "相符", [("agree with the facts", "与事实相符"), ("the figures agree", "数字一致")], [("The figures do not agree.", "这些数字对不上。"), ("His story agrees with the facts.", "他的说法与事实相符。")], "match：表示相互匹配；agree 常说数字、说法或证据相符。", "conflict：相互矛盾。", "两个数字 agree 时是“一致”，不是它们在表达意见。"),
        ],
    },
}


def main():
    OUT.mkdir(exist_ok=True)
    for word, data in ENTRIES.items():
        (OUT / f"{word}.json").write_text(json.dumps({"word": word, **data}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRIES)} second-group candidates")


if __name__ == "__main__":
    main()
