"""Original full-entry candidates for the final ten basic pilot headwords.

Writes candidate JSON only. It does not change the catalog or published words.
"""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "focus": {
        "phonetic": "/ˈfoʊkəs/", "syllables": ["fo", "cus"], "pos": ["n.", "v."],
        "core_meanings": ["注意力", "重点", "集中注意力"], "etymology": "来自拉丁语 focus“炉火、壁炉”；进入英语后先用于光线等汇聚的一点。",
        "semantic_shift": "从光线汇聚的一点，扩展到活动的中心，再到注意力集中的对象。",
        "senses": [
            sense(1, "n.", "attention given to one thing", "集中在某件事上的注意力", "注意力", [("lose focus", "分心"), ("keep your focus", "保持专注")], [("Noise makes me lose focus.", "噪声让我难以集中注意力。"), ("Try to keep your focus on the task.", "尽量把注意力放在任务上。")], "concentration：强调持续专注的能力；focus 也可指注意力所指的方向。", "distraction：使人分心的事物。", "focus on 后接注意的对象。"),
            sense(2, "n.", "the main subject or point of interest", "讨论或活动最关注的主题", "重点", [("the main focus", "主要重点"), ("the focus of the lesson", "这节课的重点")], [("The main focus today is listening.", "今天的重点是听力。"), ("Safety is the focus of this meeting.", "安全是这次会议的重点。")], "emphasis：强调的程度；focus 指注意力集中之处。", "", "the focus of 后接具体活动或讨论。"),
            sense(3, "v.", "to give your attention to one thing", "把注意力集中在一件事上", "专注", [("focus on a task", "专注于任务"), ("focus your attention", "集中注意力")], [("Please focus on your homework.", "请专心做作业。"), ("I need to focus my attention on the road.", "我需要集中注意力看路。")], "concentrate：也指专注；focus on 常直接指出关注对象。", "lose concentration：注意力涣散。", "focus on something；on 不能省略。"),
        ],
    },
    "follow": {
        "phonetic": "/ˈfɑːloʊ/", "syllables": ["fol", "low"], "pos": ["v."],
        "core_meanings": ["跟随", "遵循", "理解"], "etymology": "源自古英语 folgian、fylgian，早已用于跟在后面及遵从规则。",
        "semantic_shift": "跟随和遵从规则都见于早期用法；后来还可表示思路上跟得上。",
        "senses": [
            sense(1, "v.", "to move behind someone or along a route", "跟在某人后面或沿路线前进", "跟随", [("follow me", "跟着我"), ("follow a path", "沿着小路走")], [("The dog followed me home.", "那只狗跟着我回了家。"), ("Follow this path to the river.", "沿着这条小路走到河边。")], "come after：表示在后面到来；follow 强调一路跟随。", "lead：走在前面带路。", "follow someone home 不必加 to。"),
            sense(2, "v.", "to do what a rule or instruction says", "按照规则或指示去做", "遵循", [("follow the rules", "遵守规则"), ("follow instructions", "按说明操作")], [("Please follow the safety rules.", "请遵守安全规则。"), ("I followed the instructions on the box.", "我按照盒子上的说明操作了。")], "obey：强调服从权威；follow 也可用于说明书和步骤。", "ignore：不理会规则或指示。", "follow instructions 是按指示做，不是跟着纸张走。"),
            sense(3, "v.", "to understand what someone is saying or doing", "理解某人的话或做法", "听懂或理解", [("follow an explanation", "听懂解释"), ("follow the story", "跟上故事情节")], [("I could not follow his explanation.", "我听不懂他的解释。"), ("The story was easy to follow.", "这个故事很容易看懂。")], "understand：泛指理解；follow 强调跟上逐步展开的内容。", "lose track：跟不上进展。", "follow the story 是看懂情节，不是跟着人物走。"),
        ],
    },
    "improve": {
        "phonetic": "/ɪmˈpruːv/", "syllables": ["im", "prove"], "pos": ["v."],
        "core_meanings": ["改善", "提高"], "etymology": "经盎格鲁法语 emprouwer 进入英语，早期有“使之获益”之意。",
        "semantic_shift": "从使之获益，发展为使质量变好；后来也可指情况自行好转。",
        "senses": [
            sense(1, "v.", "to become better", "自身变得更好", "改善", [("health improves", "健康状况好转"), ("improve slowly", "慢慢好转")], [("Her health improved after the rest.", "休息后她的健康状况好转了。"), ("My English is improving slowly.", "我的英语在慢慢进步。")], "get better：日常说法；improve 较中性。", "worsen：恶化。", "此义 improve 不接宾语。"),
            sense(2, "v.", "to make something better", "使某事物变得更好", "提高或改进", [("improve your English", "提高英语水平"), ("improve a service", "改进服务")], [("Reading every day can improve your English.", "每天阅读能提高你的英语水平。"), ("The company improved its service.", "这家公司改进了服务。")], "enhance：也指提高，语气较正式。", "damage：损害。", "此义 improve 直接接需要改进的事物。"),
        ],
    },
    "include": {
        "phonetic": "/ɪnˈkluːd/", "syllables": ["in", "clude"], "pos": ["v."],
        "core_meanings": ["包括", "列入"], "etymology": "来自拉丁语 includere“关在里面、包在里面”，由 in-“在内”和 claudere“关闭”组成。",
        "semantic_shift": "从把某物包在里面，发展为把它视作整体的一部分。",
        "senses": [
            sense(1, "v.", "to have someone or something as part of a group", "整体中包含某人或某物", "包括", [("the price includes lunch", "价格包含午餐"), ("include several examples", "包含几个例子")], [("The price includes breakfast.", "这个价格包含早餐。"), ("The book includes several short stories.", "这本书收录了几个短篇故事。")], "contain：强调里面有某物；include 强调作为整体的一部分。", "exclude：不包括。", "including 可用于列举部分内容，不表示清单一定完整。"),
            sense(2, "v.", "to add someone or something to a group or plan", "主动把某人或某物列入群体或计划", "列入", [("include me in the plan", "把我列入计划"), ("include everyone", "让每个人都参与")], [("Please include me in the group chat.", "请把我加入群聊。"), ("We included everyone in the game.", "我们让每个人都参加了游戏。")], "add：指添上；include 强调成为整体的一部分。", "leave out：遗漏或不让参加。", "include someone in something 中的 in 引出群体或活动。"),
        ],
    },
    "increase": {
        "phonetic": "/ɪnˈkriːs/", "syllables": ["in", "crease"], "pos": ["v.", "n."],
        "core_meanings": ["增加", "增大", "增幅"], "etymology": "经古法语 encreistre，最终来自拉丁语 increscere“增长”。",
        "semantic_shift": "数量自身上升，或有人使数量上升；作名词时指上升本身或上升的幅度。",
        "senses": [
            sense(1, "v.", "to become greater in number or amount", "数量或程度自身变大", "增加", [("prices increase", "价格上涨"), ("increase rapidly", "迅速增长")], [("Food prices increased last month.", "上个月食品价格上涨了。"), ("The number of visitors is increasing.", "游客人数正在增加。")], "rise：也表示上升；increase 可用于数量和程度。", "decrease：减少。", "此义 increase 不接宾语。"),
            sense(2, "v.", "to make something greater in number or amount", "使数量或程度变大", "增加", [("increase production", "提高产量"), ("increase the price", "提高价格")], [("The factory increased production this year.", "工厂今年提高了产量。"), ("They increased the ticket price.", "他们提高了票价。")], "raise：也指提高；increase 常直接接数量或产量。", "reduce：减少。", "此义 increase 后直接接被提高的事物。"),
            sense(3, "n.", "a rise in number or amount", "数量或程度的上升", "增长或增幅", [("an increase in sales", "销量增长"), ("a small increase", "小幅增长")], [("There was an increase in sales.", "销量有所增长。"), ("We saw a small increase in cost.", "我们看到成本小幅增加。")], "rise：名词，也表示上升；increase 常搭配 in 指明增长的对象。", "decrease：下降。", "名词 increase 常读 /ˈɪnkriːs/，动词常读 /ɪnˈkriːs/；an increase in 后接增长的事物。"),
        ],
    },
    "influence": {
        "phonetic": "/ˈɪnfluəns/", "syllables": ["in", "flu", "ence"], "pos": ["n.", "v."],
        "core_meanings": ["影响", "影响力"], "etymology": "经古法语 influence，源于拉丁语 influere“流入”；早期曾用于描述星体被认为产生的作用。",
        "semantic_shift": "从某种力量“流入”并产生作用，发展为一般的影响力。",
        "senses": [
            sense(1, "n.", "the power to affect how someone thinks or acts", "改变他人想法或行为的力量", "影响力", [("have an influence on", "对……有影响"), ("a strong influence", "很大的影响力")], [("Friends can have a strong influence on us.", "朋友可能对我们有很大影响。"), ("Her teacher had an influence on her choice.", "老师影响了她的选择。")], "effect：强调造成的结果；influence 也可指影响的力量。", "", "influence on 后接受影响的人或事。"),
            sense(2, "v.", "to affect someone's thoughts or actions", "影响某人的想法或行为", "影响", [("influence a decision", "影响决定"), ("influence young people", "影响年轻人")], [("The weather influenced our decision.", "天气影响了我们的决定。"), ("Parents influence their children's habits.", "父母会影响孩子的习惯。")], "affect：泛指产生作用；influence 常强调对选择或行为的作用。", "", "influence 作动词直接接宾语，不说 influence on a decision。"),
        ],
    },
    "information": {
        "phonetic": "/ˌɪnfərˈmeɪʃən/", "syllables": ["in", "for", "ma", "tion"], "pos": ["n."],
        "core_meanings": ["信息", "资料"], "etymology": "经古法语 informacion，来自拉丁语 informatio，与“塑造、教导”有关。",
        "semantic_shift": "从教导或传达，发展为传递给人的事实与资料。",
        "senses": [
            sense(1, "n.", "facts or details that tell you about something", "帮助了解某事的事实或细节", "信息", [("get information", "获取信息"), ("share information", "分享信息")], [("I need more information about the course.", "我需要这门课程的更多信息。"), ("Please share this information with your team.", "请把这些信息分享给你的团队。")], "data：常指收集到的原始数据；information 是能帮助理解的内容。", "lack of information：信息不足。", "information 通常不可数；说 a piece of information，不说 an information。"),
            sense(2, "n.", "details supplied to help someone use a service or visit a place", "帮助使用服务或了解地点的说明资料", "资料", [("travel information", "旅行资料"), ("contact information", "联系信息")], [("The website has travel information for visitors.", "网站为游客提供旅行资料。"), ("Write your contact information on the form.", "请在表格上填写联系信息。")], "details：指具体细节；information 可统称这些资料。", "", "contact information 包括电话或邮箱等联系资料。"),
        ],
    },
    "involve": {
        "phonetic": "/ɪnˈvɑːlv/", "syllables": ["in", "volve"], "pos": ["v."],
        "core_meanings": ["包含", "使参与"], "etymology": "经古法语 involver，来自拉丁语 involvere“卷入、包裹”，字面有“卷到里面”之意。",
        "semantic_shift": "从把东西卷入其中，发展为事情包含某些部分，或让人参与。",
        "senses": [
            sense(1, "v.", "to include something as a necessary part", "把某事作为必要部分包含在内", "涉及", [("involve hard work", "需要努力工作"), ("involve several steps", "涉及几个步骤")], [("The job involves a lot of travel.", "这份工作需要经常出差。"), ("Making bread involves several steps.", "做面包涉及好几个步骤。")], "require：强调必须具备；involve 强调这件事包含哪些部分。", "", "involve doing something 可表示事情需要做某事。"),
            sense(2, "v.", "to make someone take part in something", "让某人参与某事", "使参与", [("involve students", "让学生参与"), ("involve the whole family", "让全家参与")], [("The teacher involved everyone in the game.", "老师让每个人都参与游戏。"), ("We should involve students in the decision.", "我们应该让学生参与这项决定。")], "include：表示把人列入；involve 更强调实际参与。", "exclude：排除在外。", "involve someone in something 中的 in 引出所参与的活动。"),
        ],
    },
    "issue": {
        "phonetic": "/ˈɪʃuː/", "syllables": ["is", "sue"], "pos": ["n.", "v."],
        "core_meanings": ["问题", "议题", "期刊的一期", "发布"], "etymology": "经古法语 issue“出口、出去”，最终来自拉丁语 exire“出去”。",
        "semantic_shift": "从出去，发展为发出或出版；事情产生的结果又引出待解决的议题。",
        "senses": [
            sense(1, "n.", "a problem that needs attention", "需要处理的问题", "问题", [("solve an issue", "解决问题"), ("a serious issue", "严重问题")], [("We need to solve this issue soon.", "我们需要尽快解决这个问题。"), ("There is an issue with my phone.", "我的手机出了点问题。")], "problem：一般的问题；issue 有时更委婉或正式。", "solution：解决办法。", "an issue with something 可表示某物出了问题。"),
            sense(2, "n.", "a subject that people discuss or disagree about", "供人讨论或存在分歧的话题", "议题", [("discuss an issue", "讨论议题"), ("a social issue", "社会议题")], [("The class discussed the issue of school uniforms.", "全班讨论了校服这一议题。"), ("Housing is an important social issue.", "住房是一个重要的社会议题。")], "topic：泛指话题；issue 往往需要讨论或决定。", "", "issue of 后接具体议题。"),
            sense(3, "n.", "one copy of a magazine or newspaper in a series", "连续出版的杂志或报纸中的一期", "期刊的一期", [("the latest issue", "最新一期"), ("this month's issue", "本月这一期")], [("The latest issue arrived today.", "最新一期今天送到了。"), ("I read the article in this month's issue.", "我在本月那期杂志里读了这篇文章。")], "edition：可指特定版本；issue 强调定期出版的某一期。", "", "an issue of a magazine 指杂志的一期。"),
            sense(4, "v.", "to officially give or publish something", "正式发放或公布某物", "发放或发布", [("issue a statement", "发表声明"), ("issue tickets", "发放票券")], [("The school issued a statement yesterday.", "学校昨天发表了一份声明。"), ("They issued tickets at the entrance.", "他们在入口处发放票券。")], "release：指发布或放出；issue 常带正式发放的意味。", "withdraw：撤回已发布的内容。", "issue a statement 是发表声明，不是讨论问题。"),
        ],
    },
    "knowledge": {
        "phonetic": "/ˈnɑːlɪdʒ/", "syllables": ["know", "ledge"], "pos": ["n."],
        "core_meanings": ["知识", "知晓"], "etymology": "英语早期形式 cnawlece 与 know 有关；词尾更早来源尚不确定。",
        "semantic_shift": "从承认或知晓，发展为掌握的事实与理解，也保留“知道某事”的用法。",
        "senses": [
            sense(1, "n.", "facts and understanding gained through learning or experience", "通过学习或经历获得的事实与理解", "知识", [("gain knowledge", "获得知识"), ("general knowledge", "常识")], [("Reading helps us gain knowledge.", "阅读帮助我们获得知识。"), ("She has a good knowledge of history.", "她有扎实的历史知识。")], "information：指资料或信息；knowledge 强调已经理解并掌握。", "ignorance：无知。", "knowledge 通常不可数；a knowledge of 表示对某领域有所了解。"),
            sense(2, "n.", "the state of knowing a particular fact", "知道某个具体事实的状态", "知晓", [("without my knowledge", "在我不知情时"), ("have knowledge of the plan", "知道这项计划")], [("They changed the plan without my knowledge.", "他们在我不知情时改了计划。"), ("I had no knowledge of the meeting.", "我不知道有这场会议。")], "awareness：强调意识到；knowledge 强调已经知道事实。", "lack of awareness：未察觉。", "without someone's knowledge 指对方不知情，不一定表示对方不同意。"),
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
