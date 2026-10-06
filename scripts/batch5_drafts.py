"""Original batch-5 dictionary candidates; writes candidate files only."""

import json
from pathlib import Path
from pilot_drafts import sense as s

OUT = Path(__file__).resolve().parents[1] / "content" / "candidates" / "batch5"


def head(word, phonetic, syllables, pos, meanings, senses, shift="", etymology=""):
    return {
        "word": word, "phonetic": phonetic, "syllables": syllables,
        "pos": pos, "core_meanings": meanings, "etymology": etymology,
        "semantic_shift": shift, "senses": senses,
    }


ENTRIES = {
    "account": head("account", "/əˈkaʊnt/", ["ac", "count"], ["n.", "v."], ["账户", "记述", "解释", "占比"], [
        s(1, "n.", "an arrangement with a bank or online service for keeping money or information", "用于存钱或使用线上服务的账户", "账户", [("open a bank account", "开银行账户"), ("create an account", "注册账户")], [("She opened a bank account yesterday.", "她昨天开了一个银行账户。"), ("You need an account to use the app.", "使用这个应用需要注册账户。")], "profile：常指账户中的个人资料；account 指使用服务的账户。", "close an account：关闭账户。", "bank account 存钱；online account 用来登录服务。"),
        s(2, "n.", "a written or spoken description of what happened", "对发生的事情所作的口头或书面描述", "记述", [("a detailed account", "详细记述"), ("an account of the event", "对事件的记述")], [("He gave a detailed account of the accident.", "他详细讲述了这场事故。"), ("I read an account of her journey.", "我读了一篇关于她旅程的记述。")], "report：常指正式报告；account 可是个人讲述。", "", "an account of 后接所记述的事情。"),
        s(3, "v.", "to explain the reason for something", "说明某事发生的原因", "解释", [("account for the delay", "解释延误原因"), ("account for the change", "解释变化原因")], [("Bad weather accounts for the delay.", "恶劣天气是延误的原因。"), ("How do you account for this change?", "你如何解释这个变化？")], "explain：直接表示解释；account for 常强调原因。", "", "account for 后接需要解释的事情。"),
        s(4, "v.", "to make up a particular part of a total", "占整体中的某一部分", "占比", [("account for half", "占一半"), ("account for most sales", "占大部分销量")], [("Online orders account for half our sales.", "线上订单占我们销量的一半。"), ("Women account for most of the team.", "女性占团队的大多数。")], "make up：也表示构成某个比例，更口语。", "", "account for 在这里表示占比，不是解释原因。"),
    ]),
    "act": head("act", "/ækt/", ["act"], ["v.", "n."], ["行动", "表演", "行为", "法案"], [
        s(1, "v.", "to do something in response to a situation", "面对情况采取行动", "行动", [("act quickly", "迅速行动"), ("act on advice", "根据建议行动")], [("We must act quickly to help them.", "我们必须迅速行动帮助他们。"), ("She acted on her doctor's advice.", "她按医生的建议采取了行动。")], "respond：强调作出回应；act 强调真正采取行动。", "do nothing：不采取行动。", "act on advice 是照建议行动，不是表演建议。"),
        s(2, "v.", "to perform as a character in a play or film", "在戏剧或电影中扮演角色", "表演", [("act in a film", "参演电影"), ("act on stage", "在舞台上表演")], [("He acted in a school play.", "他参演了学校的话剧。"), ("She has acted on stage for years.", "她在舞台上表演多年了。")], "perform：泛指演出；act 特指扮演角色。", "", "act in a film 指参演，不是对电影采取行动。"),
        s(3, "n.", "a particular thing that someone does", "某人做出的一次具体行为", "行为", [("an act of kindness", "一次善举"), ("a brave act", "勇敢的举动")], [("Helping her was an act of kindness.", "帮助她是一次善举。"), ("The rescue was a brave act.", "这次救援是勇敢的举动。")], "action：泛指行动；act 常指可单独评价的一件行为。", "", "an act of 后接行为的性质。"),
        s(4, "n.", "a law passed by a government", "政府通过的一项法律", "法案", [("pass an act", "通过法案"), ("a new act", "一项新法案")], [("Parliament passed a new act.", "议会通过了一项新法案。"), ("The act protects workers.", "这项法律保护劳动者。")], "law：泛指法律；act 常指正式通过的具体法律。", "repeal an act：废除法案。", "大写 Act 常出现在正式法案名称中。"),
    ]),
    "add": head("add", "/æd/", ["add"], ["v."], ["增加", "相加", "补充说"], [
        s(1, "v.", "to put something with something else", "把某物放进或加到另一物中", "添加", [("add sugar", "加糖"), ("add a name to the list", "把名字加进名单")], [("Add some salt to the soup.", "在汤里加点盐。"), ("Please add my name to the list.", "请把我的名字加进名单。")], "include：表示包含；add 强调现在把东西加进去。", "remove：移除。", "add something to something 中的 to 引出加入的地方。"),
        s(2, "v.", "to calculate the total of numbers", "计算几个数字的总和", "相加", [("add two numbers", "把两个数相加"), ("add up the costs", "把费用加起来")], [("Add five and three to get eight.", "五加三等于八。"), ("We added up all the costs.", "我们把所有费用加了起来。")], "sum：也表示求总和，较正式。", "subtract：减去。", "add up 可表示把多项金额加起来。"),
        s(3, "v.", "to say something more after speaking", "说完后再补充一句", "补充说", [("add a comment", "补充一句评论"), ("add that ...", "补充说……")], [("I forgot to add that the meeting is online.", "我忘了补充说会议在线上举行。"), ("She added a short comment at the end.", "她最后补充了一句简短的评论。")], "mention：提及；add 强调在已有话语后再说。", "", "add that 后可接完整句子。"),
    ]),
    "admit": head("admit", "/ədˈmɪt/", ["ad", "mit"], ["v."], ["承认", "准许进入", "收治"], [
        s(1, "v.", "to agree that something is true, especially reluctantly", "承认某事属实，尤其是不情愿时", "承认", [("admit a mistake", "承认错误"), ("admit the truth", "承认事实")], [("He admitted his mistake.", "他承认了自己的错误。"), ("She admitted that she was afraid.", "她承认自己害怕。")], "confess：常指承认过错；admit 可用于一般事实。", "deny：否认。", "admit that 后接完整句子。"),
        s(2, "v.", "to allow someone to enter a place or join an organization", "允许某人进入场所或加入机构", "准许进入", [("admit visitors", "准许访客进入"), ("admit students", "录取学生")], [("The museum admits children for free.", "这家博物馆允许儿童免费入内。"), ("The school admitted fifty new students.", "学校录取了五十名新生。")], "allow in：表示允许进入；admit 较正式。", "refuse entry：拒绝进入。", "admit students 在学校语境中表示录取。"),
        s(3, "v.", "to accept a patient into a hospital", "接收病人住院治疗", "收治", [("admit a patient", "收治病人"), ("be admitted to the hospital", "被收入院")], [("The hospital admitted him last night.", "医院昨晚收治了他。"), ("She was admitted to the hospital on Monday.", "她周一住院了。")], "hospitalize：指让病人住院；admit 强调办理接收入院。", "discharge：准许病人出院。", "美式英语通常说 be admitted to the hospital。"),
    ]),
    "advance": head("advance", "/ədˈvæns/", ["ad", "vance"], ["v.", "n.", "adj."], ["前进", "进展", "提前的"], [
        s(1, "v.", "to move forward", "向前移动", "前进", [("advance slowly", "缓慢前进"), ("advance toward the city", "向城市推进")], [("The soldiers advanced slowly.", "士兵们缓慢前进。"), ("The crowd advanced toward the gate.", "人群向大门走去。")], "move forward：更日常；advance 稍正式。", "retreat：后退。", "advance toward 后接前进的目标。"),
        s(2, "v.", "to help an idea or plan develop", "推动想法或计划向前发展", "推动", [("advance a plan", "推进计划"), ("advance research", "推动研究")], [("The new funding advanced the project.", "新资金推动了项目进展。"), ("Her work advanced our understanding.", "她的工作增进了我们的理解。")], "promote：也指促进；advance 强调向下一阶段推进。", "hinder：阻碍。", "advance research 表示推动研究，不是让研究走路。"),
        s(3, "n.", "progress or an improvement", "取得的进展或改进", "进展", [("an advance in medicine", "医学进展"), ("a major advance", "重大进展")], [("This was a major advance in treatment.", "这是治疗方面的一项重大进展。"), ("We have seen advances in technology.", "我们见证了技术进步。")], "progress：泛指进步；an advance 常指一项具体突破。", "setback：挫折。", "an advance in 后接取得进展的领域。"),
        s(4, "adj.", "done or given before the usual time", "比通常时间更早进行或提供的", "提前的", [("advance notice", "提前通知"), ("advance payment", "预付款")], [("We need advance notice of any changes.", "如有变更，我们需要提前获知。"), ("The hotel asks for advance payment.", "这家酒店要求预先付款。")], "early：泛指早；advance 常作定语修饰通知或付款。", "late：迟的。", "advance notice 是提前通知，不是先进的通知。"),
    ]),
}

ENTRIES.update({
    "aid": head("aid", "/eɪd/", ["aid"], ["n.", "v."], ["援助", "帮助"], [
        s(1, "n.", "help given to someone who needs it", "向有需要的人提供的帮助", "援助", [("provide aid", "提供援助"), ("emergency aid", "紧急援助")], [("The town sent aid after the flood.", "洪水过后，这座城镇送去了援助物资。"), ("The charity provides aid to families.", "这家慈善机构为家庭提供援助。")], "help：日常用词；aid 多见于正式援助或救济。", "", "aid 在此常不可数，指援助整体。"),
        s(2, "v.", "to help someone do something", "帮助某人做某事", "帮助", [("aid a student", "帮助学生"), ("aid recovery", "帮助康复")], [("The nurse aided his recovery.", "护士帮助他康复。"), ("These notes will aid your study.", "这些笔记会帮助你学习。")], "help：更常用；aid 作动词较正式。", "hinder：妨碍。", "aid recovery 中的 aid 是动词，不是名词。"),
    ]),
    "aim": head("aim", "/eɪm/", ["aim"], ["n.", "v."], ["目标", "旨在", "瞄准"], [
        s(1, "n.", "something that you want to achieve", "希望实现的目标", "目标", [("a clear aim", "明确的目标"), ("the main aim", "主要目的")], [("Our main aim is to help children read.", "我们的主要目标是帮助孩子阅读。"), ("She has a clear aim for this year.", "她今年有一个明确的目标。")], "goal：也指目标；aim 更强调做事的目的。", "", "the aim of 后接活动，说明活动目的。"),
        s(2, "v.", "to intend to achieve something", "打算实现某个目标", "旨在", [("aim to improve", "旨在改进"), ("aim for a high score", "争取高分")], [("The project aims to reduce waste.", "这个项目旨在减少浪费。"), ("He is aiming for a higher score.", "他正争取更高的分数。")], "intend：强调打算；aim 强调目标方向。", "", "aim to 后接动词，aim for 后接目标名词。"),
        s(3, "v.", "to point something at a target", "把某物对准目标", "瞄准", [("aim at a target", "瞄准靶子"), ("aim a camera", "把相机对准目标")], [("She aimed at the center of the target.", "她瞄准了靶心。"), ("He aimed the camera at the bird.", "他把相机对准那只鸟。")], "point：泛指指向；aim 暗含目标。", "", "aim something at a target 表示把某物对准目标。"),
    ]),
    "air": head("air", "/er/", ["air"], ["n.", "v."], ["空气", "空中", "播出"], [
        s(1, "n.", "the mixture of gases that people breathe", "人呼吸的气体混合物", "空气", [("fresh air", "新鲜空气"), ("clean air", "清洁空气")], [("Open the window to let in fresh air.", "打开窗户，让新鲜空气进来。"), ("We need clean air to stay healthy.", "我们需要清洁空气来保持健康。")], "oxygen：氧气只是空气的一种成分。", "polluted air：被污染的空气。", "air 表示空气时通常不可数。"),
        s(2, "n.", "the space above the ground", "地面以上的空间", "空中", [("in the air", "在空中"), ("through the air", "穿过空中")], [("The kite rose high in the air.", "风筝升到了高空。"), ("A bird flew through the air.", "一只鸟从空中飞过。")], "sky：通常指看到的天空；air 是地面以上的空间或空气。", "on the ground：在地上。", "in the air 可指真的在空中，也可比喻气氛。"),
        s(3, "v.", "to broadcast a program on radio or television", "通过广播或电视播出节目", "播出", [("air a program", "播出节目"), ("air tonight", "今晚播出")], [("The station will air the show tonight.", "电视台今晚会播出这个节目。"), ("The interview aired last week.", "那次访谈上周播出了。")], "broadcast：也指播出；air 在媒体报道中很常见。", "", "节目作主语时可说 The show aired。"),
    ]),
    "alarm": head("alarm", "/əˈlɑːrm/", ["a", "larm"], ["n.", "v."], ["警报", "闹钟", "惊恐"], [
        s(1, "n.", "a warning sound or device that signals danger", "提示危险的声音或装置", "警报", [("sound the alarm", "拉响警报"), ("a fire alarm", "火灾警报器")], [("The fire alarm went off at noon.", "中午火灾警报响了。"), ("Someone sounded the alarm.", "有人拉响了警报。")], "warning：泛指警告；alarm 常指响起的警报或装置。", "", "an alarm goes off 表示警报响起。"),
        s(2, "n.", "a device that wakes someone at a set time", "在设定时间叫醒人的装置", "闹钟", [("set an alarm", "设闹钟"), ("turn off the alarm", "关掉闹钟")], [("I set my alarm for seven.", "我把闹钟设在七点。"), ("The alarm woke me up early.", "闹钟很早就把我叫醒了。")], "clock：显示时间；alarm 用来提醒或叫醒人。", "", "set an alarm for seven 表示设在七点响。"),
        s(3, "v.", "to make someone suddenly worried or frightened", "使某人突然担忧或害怕", "使惊恐", [("alarm the family", "使家人惊慌"), ("be alarmed by", "因……而惊慌")], [("The loud noise alarmed the children.", "巨响吓到了孩子们。"), ("We were alarmed by the smoke.", "看到烟雾，我们很惊慌。")], "frighten：强调害怕；alarm 也包含对危险的担忧。", "reassure：使人安心。", "be alarmed by 表示因某事而担心或惊恐。"),
    ]),
    "answer": head("answer", "/ˈænsər/", ["an", "swer"], ["n.", "v."], ["回答", "答案", "接听"], [
        s(1, "v.", "to reply to a question", "对问题作出回应", "回答", [("answer a question", "回答问题"), ("answer honestly", "诚实回答")], [("Please answer the question clearly.", "请清楚地回答这个问题。"), ("She answered honestly.", "她如实回答了。")], "reply：可单独表示回应；answer 常直接接问题。", "", "answer a question 不需在 question 前加 to。"),
        s(2, "n.", "a response to a question or problem", "对问题给出的回应或解法", "答案", [("the right answer", "正确答案"), ("find an answer", "找到答案")], [("What is the answer to question three?", "第三题的答案是什么？"), ("We still need an answer to this problem.", "这个问题我们仍需要一个答案。")], "solution：强调问题的解决办法；answer 也可指普通问答。", "question：问题。", "the answer to 后接问题，而不是 answer of。"),
        s(3, "v.", "to pick up a ringing telephone", "接起正在响的电话", "接电话", [("answer the phone", "接电话"), ("answer a call", "接听来电")], [("Can you answer the phone?", "你能接一下电话吗？"), ("He did not answer my call.", "他没有接我的电话。")], "pick up：口语中也可表示接电话。", "ignore a call：不接电话。", "answer the phone 指接听，不只是给问题写答案。"),
    ]),
})

ENTRIES.update({
    "beat": head("beat", "/biːt/", ["beat"], ["v.", "n."], ["击打", "打败", "跳动", "节拍"], [
        s(1, "v.", "to hit something repeatedly", "连续击打某物", "敲打", [("beat a drum", "敲鼓"), ("beat the carpet", "拍打地毯")], [("He beat the drum loudly.", "他大声敲鼓。"), ("She beat the dust out of the carpet.", "她拍掉了地毯上的灰尘。")], "hit：可以只打一下；beat 通常表示反复击打。", "", "beat a drum 是敲鼓，不是打败鼓。"),
        s(2, "v.", "to defeat someone in a game or competition", "在比赛中战胜某人", "打败", [("beat a team", "打败一支队伍"), ("beat someone in a race", "在赛跑中胜过某人")], [("Our team beat theirs by two points.", "我们队以两分优势打败了他们队。"), ("She beat me in the final race.", "她在最后一场赛跑中赢了我。")], "win：通常接比赛或奖品；beat 直接接被打败的人或队伍。", "lose to：输给。", "beat an opponent；win a match。"),
        s(3, "v.", "to move with a regular rhythm, as a heart does", "像心脏一样有规律地跳动", "跳动", [("the heart beats", "心脏跳动"), ("beat faster", "跳得更快")], [("His heart beat faster as he ran.", "他跑步时心跳加快了。"), ("My heart was beating hard.", "我的心跳得很快。")], "pulse：可指脉搏跳动；beat 是心脏跳动的普通说法。", "stop beating：停止跳动。", "心脏作主语时 beat 不表示打人。"),
        s(4, "n.", "a regular sound or movement in music", "音乐中有规律的声音或动作", "节拍", [("keep the beat", "跟上节拍"), ("a strong beat", "鲜明的节拍")], [("Try to keep the beat with your hands.", "试着用手打出节拍。"), ("The song has a strong beat.", "这首歌的节拍很鲜明。")], "rhythm：指整体节奏；beat 是其中反复出现的拍点。", "", "the beat of a song 指歌的节拍。"),
    ]),
    "bend": head("bend", "/bend/", ["bend"], ["v.", "n."], ["弯曲", "弯腰", "弯道"], [
        s(1, "v.", "to make something curved or become curved", "使某物弯曲或自行弯曲", "弯曲", [("bend a wire", "弯曲铁丝"), ("bend easily", "容易弯曲")], [("He bent the wire into a circle.", "他把铁丝弯成了一个圈。"), ("This plastic bends easily.", "这种塑料很容易弯曲。")], "curve：强调形成弧形；bend 可以是一次折弯。", "straighten：弄直。", "bend into 后接弯成的形状。"),
        s(2, "v.", "to move your body or a part of it downward", "身体或身体部位向下弯", "弯腰", [("bend down", "弯下腰"), ("bend your knees", "屈膝")], [("She bent down to pick up the book.", "她弯腰捡起书。"), ("Bend your knees when you lift the box.", "抬箱子时要屈膝。")], "stoop：也指弯腰；bend 可用于身体不同部位。", "stand straight：站直。", "bend down 指身体向下弯，不一定跪下。"),
        s(3, "n.", "a curved part of a road or river", "道路或河流弯曲的一段", "弯道", [("a sharp bend", "急弯"), ("around the bend", "绕过弯道")], [("Slow down before the sharp bend.", "到急弯前请减速。"), ("The river turns around a wide bend.", "河流绕过一个大弯。")], "curve：也指弯曲处；bend 常指道路或河流的一个弯。", "straight section：直道。", "a bend in the road 表示路上的弯道。"),
    ]),
    "bill": head("bill", "/bɪl/", ["bill"], ["n.", "v."], ["账单", "钞票", "法案", "鸟嘴"], [
        s(1, "n.", "a written statement of money you owe", "列明应付款项的单据", "账单", [("pay the bill", "付账"), ("an electricity bill", "电费账单")], [("We paid the bill after dinner.", "我们饭后付了账。"), ("The electricity bill arrived today.", "电费账单今天寄到了。")], "receipt：是付款后的收据；bill 是等待支付的账单。", "", "pay the bill 指付账，不是支付法案。"),
        s(2, "n.", "a piece of paper money, especially in American English", "纸币，尤见于美式英语", "钞票", [("a ten-dollar bill", "一张十美元钞票"), ("a hundred-dollar bill", "一张百元钞票")], [("She gave me a ten-dollar bill.", "她给了我一张十美元钞票。"), ("I only have a hundred-dollar bill.", "我只有一张百元钞票。")], "banknote：较正式的纸币说法。", "coin：硬币。", "a bill 在美国英语中可指纸币；英国英语多说 note。"),
        s(3, "n.", "a proposed law being discussed by lawmakers", "立法机构正在讨论的法律草案", "法案", [("pass a bill", "通过法案"), ("introduce a bill", "提出法案")], [("Lawmakers discussed the new bill.", "立法者讨论了新法案。"), ("The committee introduced a bill on housing.", "委员会提出了一项住房法案。")], "act：通常指已经通过的法律；bill 还在立法过程中。", "reject a bill：否决法案。", "bill 作为法案时，不是要付款的账单。"),
        s(4, "n.", "the hard projecting mouth of a bird", "鸟向前突出的坚硬嘴部", "鸟嘴", [("a duck's bill", "鸭嘴"), ("a long bill", "长鸟嘴")], [("The duck has a wide bill.", "这只鸭子的嘴很宽。"), ("The bird used its bill to pick up food.", "那只鸟用嘴叼起食物。")], "beak：也指鸟喙；bill 常用于鸭等嘴较扁的鸟。", "", "这里的 bill 与账单、法案按语境区分。"),
    ]),
    "block": head("block", "/blɑːk/", ["block"], ["n.", "v."], ["块", "街区", "阻挡"], [
        s(1, "n.", "a solid piece of material with flat sides", "侧面较平的一整块材料", "块", [("a block of wood", "一块木头"), ("a block of ice", "一块冰")], [("He cut a block of wood.", "他切下一块木头。"), ("The children built a tower with blocks.", "孩子们用积木搭了一座塔。")], "piece：泛指一块；block 通常较厚且形状规则。", "", "building blocks 指积木。"),
        s(2, "n.", "the area of a street between two crossings", "两处路口之间的一段街道或街区", "街区", [("walk two blocks", "走两个街区"), ("the next block", "下一个街区")], [("The store is two blocks away.", "商店在两个街区外。"), ("The library is on the next block.", "图书馆在下一个街区。")], "neighborhood：指更大的邻里地区；block 是较小的一段街区。", "", "two blocks away 常用于美国城市中的距离描述。"),
        s(3, "v.", "to stop movement or prevent access", "阻止通行或进入", "阻挡", [("block the road", "堵住道路"), ("block the entrance", "挡住入口")], [("A fallen tree blocked the road.", "一棵倒下的树堵住了路。"), ("Do not block the entrance.", "不要挡住入口。")], "obstruct：也指阻挡，较正式；block 更常用。", "clear：清除障碍。", "block access to 后接被阻断的地方或服务。"),
        s(4, "v.", "to prevent someone from contacting you online", "在网络服务中阻止某人联系自己", "拉黑", [("block a user", "屏蔽用户"), ("block someone online", "在网上拉黑某人")], [("She blocked the account after the messages.", "收到那些消息后，她屏蔽了那个账号。"), ("You can block users who send spam.", "你可以屏蔽发送垃圾信息的用户。")], "mute：通常只是不看消息；block 会阻止联系。", "unblock：取消屏蔽。", "block a user 指在平台上屏蔽，不是挡住道路。"),
    ]),
    "blow": head("blow", "/bloʊ/", ["blow"], ["v.", "n."], ["吹", "刮风", "爆炸", "打击"], [
        s(1, "v.", "to send air out of your mouth", "从嘴里呼出气流", "吹", [("blow on soup", "对着汤吹气"), ("blow out a candle", "吹灭蜡烛")], [("Blow on the soup before you eat it.", "吃汤前先吹一吹。"), ("She blew out the candle.", "她吹灭了蜡烛。")], "breathe out：指呼气；blow 常有意向某物送气。", "breathe in：吸气。", "blow out a candle 表示吹灭蜡烛。"),
        s(2, "v.", "to move as wind does", "风吹动或流动", "刮", [("the wind blows", "刮风"), ("blow strongly", "猛烈地刮")], [("The wind blew all night.", "风刮了一整夜。"), ("A cold wind was blowing from the sea.", "一阵冷风从海上吹来。")], "gust：指一阵突然的风；blow 可说风持续吹。", "", "风作主语时 blow 不需要人来吹。"),
        s(3, "v.", "to explode or be destroyed by an explosion", "爆炸或被爆炸毁坏", "爆炸", [("blow up", "爆炸"), ("blow up a building", "炸毁建筑")], [("The old factory blew up at night.", "那座旧工厂夜里爆炸了。"), ("They blew up the empty building.", "他们炸毁了那座空楼。")], "explode：直接表示爆炸；blow up 还可接被炸毁的东西。", "", "blow up 也可指把气球吹大，须看语境。"),
        s(4, "n.", "an event that causes harm or disappointment", "造成伤害或失望的事件", "打击", [("a heavy blow", "沉重打击"), ("a blow to confidence", "对信心的打击")], [("Losing the game was a heavy blow.", "输掉比赛是沉重的打击。"), ("The news was a blow to his confidence.", "这个消息打击了他的信心。")], "setback：指挫折；blow 强调打击的感受。", "", "a blow to 后接受打击的人或事物。"),
    ]),
})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for word, entry in ENTRIES.items():
        (OUT / f"{word}.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRIES)} batch-5 candidates")



ENTRIES.update({
    "balance": head("balance", "/ˈbæləns/", ["bal", "ance"], ["n.", "v."], ["平衡", "余额", "权衡"], [
        s(1, "n.", "a state in which weight or different parts are even", "重量或各部分保持均衡的状态", "平衡", [("keep your balance", "保持平衡"), ("lose your balance", "失去平衡")], [("She lost her balance on the ice.", "她在冰上失去了平衡。"), ("The child learned to keep his balance.", "那孩子学会了保持平衡。")], "stability：强调稳定不动；balance 强调两边或身体保持均衡。", "imbalance：失衡。", "lose your balance 常指身体站不稳。"),
        s(2, "v.", "to keep something steady by arranging weight evenly", "通过均匀分配重量使某物稳定", "使保持平衡", [("balance on one foot", "单脚保持平衡"), ("balance a tray", "稳稳端住托盘")], [("He balanced on one foot.", "他单脚站稳。"), ("She balanced the tray on one hand.", "她用一只手稳稳托住托盘。")], "steady：使稳定；balance 强调重心或重量均衡。", "tip over：倾倒。", "balance on 后接支撑物。"),
        s(3, "n.", "the amount of money left in an account", "账户里剩下的金额", "余额", [("check your balance", "查询余额"), ("a low balance", "余额较低")], [("I checked my balance online.", "我在网上查了余额。"), ("The account has a low balance.", "这个账户的余额很少。")], "remaining amount：泛指剩余量；balance 在银行语境中指余额。", "", "bank balance 是银行账户余额，不是身体平衡。"),
        s(4, "v.", "to give proper attention to two different needs", "兼顾两种不同需求", "权衡兼顾", [("balance work and life", "兼顾工作与生活"), ("balance cost and quality", "权衡成本与质量")], [("She balances work and family life.", "她兼顾工作和家庭生活。"), ("We must balance cost and quality.", "我们必须权衡成本与质量。")], "weigh：强调比较利弊；balance 强调让两方都得到照顾。", "", "balance A and B 表示兼顾两方面。"),
    ]),
    "bank": head("bank", "/bæŋk/", ["bank"], ["n.", "v."], ["银行", "河岸", "存款"], [
        s(1, "n.", "an organization that keeps and lends money", "保管和借贷资金的机构", "银行", [("go to the bank", "去银行"), ("a bank account", "银行账户")], [("She works at a bank.", "她在一家银行工作。"), ("I opened a bank account today.", "我今天开了银行账户。")], "credit union：也提供金融服务，但组织方式不同。", "", "bank account 是银行账户，不是河岸账户。"),
        s(2, "n.", "the land along the side of a river", "河流两侧的陆地", "河岸", [("a river bank", "河岸"), ("on the bank", "在岸边")], [("We sat on the bank of the river.", "我们坐在河岸上。"), ("Trees grow along the river bank.", "河岸边长着树。")], "shore：多指海、湖岸边；bank 常指河岸。", "", "river bank 与存钱的 bank 是同形词，按语境判断。"),
        s(3, "v.", "to put money in a bank", "把钱存入银行", "存款", [("bank a check", "把支票存入银行"), ("bank the money", "把钱存入银行")], [("She banked the money she earned.", "她把赚来的钱存进了银行。"), ("I banked the check yesterday.", "我昨天把支票存进银行了。")], "deposit：也指存款，较正式。", "withdraw：取款。", "bank 作动词直接接存入的款项。"),
    ]),
    "bar": head("bar", "/bɑːr/", ["bar"], ["n.", "v."], ["条状物", "酒吧", "障碍", "禁止"], [
        s(1, "n.", "a long narrow piece of solid material", "狭长的固体物品", "条状物", [("a bar of chocolate", "一条巧克力"), ("a metal bar", "金属条")], [("She bought a bar of chocolate.", "她买了一条巧克力。"), ("A metal bar held the gate shut.", "一根金属条把门挡住了。")], "rod：通常指细长的杆；bar 可以更粗、更扁。", "", "a bar of chocolate 中的 bar 是成条的形状。"),
        s(2, "n.", "a place where alcoholic drinks are served", "出售酒精饮料的场所", "酒吧", [("go to a bar", "去酒吧"), ("a hotel bar", "酒店酒吧")], [("We met at a small bar.", "我们在一家小酒吧见面。"), ("The hotel bar closes at midnight.", "酒店酒吧在午夜关门。")], "pub：多见于英国英语；bar 用法更广。", "", "bar 也可指柜台；这里特指喝酒的场所。"),
        s(3, "n.", "something that stops people from making progress", "阻碍人取得进展的事物", "障碍", [("a bar to success", "成功的障碍"), ("a legal bar", "法律障碍")], [("Cost is a bar to further study.", "费用是继续求学的障碍。"), ("There is no legal bar to the plan.", "这项计划没有法律障碍。")], "barrier：也指障碍；bar 在此较正式。", "", "a bar to 后接受阻的目标。"),
        s(4, "v.", "to officially prevent someone from doing or entering something", "正式禁止某人做某事或进入某地", "禁止", [("bar entry", "禁止进入"), ("bar someone from a place", "禁止某人进入某地")], [("The rule bars entry after ten.", "规定禁止十点后入内。"), ("He was barred from the club.", "他被禁止进入俱乐部。")], "ban：也表示禁止；bar 常搭配 from。", "allow：允许。", "bar someone from doing something 是禁止某人做某事。"),
    ]),
    "base": head("base", "/beɪs/", ["base"], ["n.", "v."], ["底部", "基地", "依据"], [
        s(1, "n.", "the bottom part that supports something", "支撑某物的底部", "底座", [("the base of a lamp", "台灯底座"), ("a strong base", "结实的底座")], [("The lamp has a heavy base.", "这盏台灯有个沉重的底座。"), ("The statue stands on a stone base.", "这座雕像立在石头底座上。")], "bottom：泛指底部；base 往往承担支撑作用。", "top：物体上部，与承担支撑作用的 base 相对。", "the base of 后接被支撑的物品。"),
        s(2, "n.", "a place used as the center of an activity", "作为活动中心的地点", "基地", [("a military base", "军事基地"), ("a research base", "研究基地")], [("They built a research base in the mountains.", "他们在山里建了一座研究基地。"), ("The team returned to its base.", "团队回到了基地。")], "headquarters：常指组织总部；base 可是临时活动地点。", "", "base 在此指开展活动的地点，不是物体底座。"),
        s(3, "v.", "to use something as the starting point for an idea or decision", "以某事为想法或决定的依据", "以……为依据", [("base a plan on facts", "以事实为依据制订计划"), ("be based on a book", "根据一本书改编")], [("We based our decision on the facts.", "我们根据事实作出决定。"), ("The film is based on a true story.", "这部电影根据真实故事改编。")], "found：也指以……为基础；base on 更常见。", "", "base A on B 表示以 B 为依据形成 A。"),
    ]),
    "bear": head("bear", "/ber/", ["bear"], ["n.", "v."], ["熊", "承受", "承担", "结出"], [
        s(1, "n.", "a large wild animal with thick fur", "体型大、毛皮厚的野生动物", "熊", [("a brown bear", "棕熊"), ("a polar bear", "北极熊")], [("We saw a bear from a safe distance.", "我们在安全距离外看到一只熊。"), ("Polar bears live in the Arctic.", "北极熊生活在北极地区。")], "panda：是熊科动物的一种，不等同于所有 bear。", "", "bear 作名词指动物；作动词有其他义项，须按句子区分。"),
        s(2, "v.", "to accept or deal with pain or difficulty", "忍受痛苦或困难", "承受", [("bear the pain", "忍受疼痛"), ("cannot bear the noise", "受不了噪声")], [("She could not bear the pain.", "她无法忍受疼痛。"), ("I can't bear this noise any longer.", "我再也受不了这噪声了。")], "endure：也指忍受，较正式；bear 日常也常用。", "", "can't bear 后可接名词或 doing。"),
        s(3, "v.", "to take responsibility or the cost of something", "承担责任或费用", "承担", [("bear responsibility", "承担责任"), ("bear the cost", "承担费用")], [("Parents bear responsibility for their children.", "父母对孩子负有责任。"), ("The company will bear the cost.", "这家公司将承担费用。")], "shoulder：也指承担重担；bear 可接责任或费用。", "avoid responsibility：逃避责任。", "bear responsibility for 后接应负责的事情。"),
        s(4, "v.", "to produce fruit or flowers", "植物长出果实或花朵", "结出", [("bear fruit", "结果"), ("bear flowers", "开花")], [("The apple tree bears fruit each year.", "这棵苹果树每年都结果。"), ("These plants bear white flowers.", "这些植物开白色的花。")], "produce：泛指生产；bear 在这里用于植物结果或开花。", "", "bear fruit 可直指结果，也可比喻努力见效。"),
    ]),
})

ENTRIES.update({
    "appeal": head("appeal", "/əˈpiːl/", ["ap", "peal"], ["n.", "v."], ["吸引力", "呼吁", "上诉"], [
        s(1, "n.", "a quality that attracts people", "吸引人的特质", "吸引力", [("have wide appeal", "广受欢迎"), ("the appeal of a place", "一个地方的吸引力")], [("The town has great appeal for tourists.", "这座小镇对游客很有吸引力。"), ("I understand the appeal of living here.", "我明白住在这里有什么吸引力。")], "attraction：也指吸引力；appeal 常指让人愿意选择某物的特点。", "", "have appeal for someone 表示对某人有吸引力。"),
        s(2, "v.", "to attract or interest someone", "引起某人的兴趣", "吸引", [("appeal to children", "吸引儿童"), ("appeal to many people", "吸引许多人")], [("The idea appeals to me.", "这个主意很吸引我。"), ("This game appeals to young children.", "这个游戏很吸引年幼的孩子。")], "attract：强调吸引；appeal to 常表示符合兴趣或喜好。", "", "appeal to 后接被吸引的人。"),
        s(3, "n.", "a serious public request for help", "向公众发出的郑重求助", "呼吁", [("make an appeal", "发出呼吁"), ("an appeal for help", "求助呼吁")], [("The group made an appeal for food.", "这个团体呼吁捐赠食物。"), ("Her appeal for help reached many people.", "她的求助呼吁传到了许多人那里。")], "request：一般请求；appeal 常较紧急或公开。", "", "an appeal for 后接所请求的东西。"),
        s(4, "v.", "to ask a higher court to change a decision", "请求上级法院改变裁决", "上诉", [("appeal a decision", "对裁决提出上诉"), ("appeal to a higher court", "向上级法院上诉")], [("The lawyer appealed the decision.", "律师对这项裁决提出了上诉。"), ("She appealed to a higher court.", "她向上级法院提出了上诉。")], "challenge：泛指质疑；appeal 在法律中指正式上诉。", "accept the ruling：接受裁决。", "法律义的 appeal 与吸引力无关，需按语境判断。"),
    ]),
    "arm": head("arm", "/ɑːrm/", ["arm"], ["n.", "v."], ["手臂", "扶手", "武器", "武装"], [
        s(1, "n.", "the part of the body from shoulder to hand", "从肩到手的身体部分", "手臂", [("raise your arm", "抬起手臂"), ("a broken arm", "骨折的手臂")], [("Raise your arm if you know.", "如果你知道，就举起手臂。"), ("He hurt his arm playing basketball.", "他打篮球时伤了手臂。")], "hand：指手；arm 包括肩到手之间的部位。", "", "in my arms 可表示抱在怀里。"),
        s(2, "n.", "a side support for a chair", "椅子两侧供手臂倚靠的部分", "扶手", [("the arm of a chair", "椅子扶手"), ("rest on the arm", "靠在扶手上")], [("She rested her hand on the arm of the chair.", "她把手放在椅子扶手上。"), ("This chair has wide arms.", "这把椅子的扶手很宽。")], "armrest：专指扶手；arm 也可指椅子的侧边。", "", "chair arms 指扶手，不是人体手臂。"),
        s(3, "n.", "weapons, especially when discussed as a group", "作为一类统称的武器", "武器", [("carry arms", "携带武器"), ("arms control", "军备控制")], [("The group agreed to lay down its arms.", "这个团体同意放下武器。"), ("The countries discussed arms control.", "这些国家讨论了军备控制。")], "weapons：泛指武器；arms 多用于军事或法律语境。", "disarmament：裁军。", "表示武器时通常用复数 arms，不要与身体的 arm 混淆。"),
        s(4, "v.", "to provide someone with weapons", "给某人提供武器", "武装", [("arm the police", "给警察配备武器"), ("be armed with", "配备有……武器")], [("The guards were armed with rifles.", "警卫配备了步枪。"), ("The government armed the soldiers.", "政府给士兵配备了武器。")], "equip：泛指配备装备；arm 特指配备武器。", "disarm：解除武装。", "be armed with 后接武器名称。"),
    ]),
    "attack": head("attack", "/əˈtæk/", ["at", "tack"], ["n.", "v."], ["攻击", "抨击", "发作"], [
        s(1, "v.", "to use violence against someone or something", "对人或事物使用暴力", "攻击", [("attack a city", "进攻城市"), ("attack an animal", "攻击动物")], [("The dog attacked the stranger.", "那只狗袭击了陌生人。"), ("The army attacked the city at dawn.", "军队在黎明进攻了这座城市。")], "strike：指打击一次；attack 可指持续攻击。", "defend：防卫。", "attack 直接接受攻击者，不需 on。"),
        s(2, "n.", "a violent attempt to hurt someone or something", "一次意图伤害的暴力行为", "袭击", [("an attack on a village", "对村庄的袭击"), ("under attack", "遭到攻击")], [("The village came under attack.", "村庄遭到了袭击。"), ("The attack injured two people.", "这次袭击造成两人受伤。")], "assault：常指针对人的暴力袭击；attack 范围更广。", "defense：防御。", "an attack on 后接受攻击的对象。"),
        s(3, "v.", "to strongly criticize a person or idea", "严厉批评某人或某种观点", "抨击", [("attack a proposal", "抨击提案"), ("attack a policy", "抨击政策")], [("The speaker attacked the new policy.", "发言人严厉批评了新政策。"), ("She attacked the idea as unfair.", "她抨击这个想法不公平。")], "criticize：泛指批评；attack 语气更强烈。", "praise：赞扬。", "这里的 attack 是言语批评，不是身体袭击。"),
        s(4, "n.", "a sudden episode of an illness or strong feeling", "疾病或强烈感受的突然发作", "发作", [("a heart attack", "心脏病发作"), ("an asthma attack", "哮喘发作")], [("He had a heart attack last year.", "他去年心脏病发作过。"), ("She carries medicine for asthma attacks.", "她随身带着应对哮喘发作的药。")], "episode：也指一次发作；attack 强调突然且严重。", "", "heart attack 是固定表达，不是心脏受到外部攻击。"),
    ]),
    "average": head("average", "/ˈævərɪdʒ/", ["av", "er", "age"], ["n.", "adj.", "v."], ["平均数", "平均的", "普通的"], [
        s(1, "n.", "a number found by dividing a total by the number of items", "把总数除以项目数得到的数字", "平均数", [("calculate the average", "计算平均数"), ("an average of ten", "平均为十")], [("The average of four and six is five.", "四和六的平均数是五。"), ("We calculated the average score.", "我们算出了平均分。")], "mean：数学中常指算术平均数；average 日常使用更广。", "", "the average of 后接参与计算的数值。"),
        s(2, "adj.", "usual or typical in amount or quality", "数量或质量处于通常水平的", "平均的或普通的", [("average income", "平均收入"), ("an average day", "平常的一天")], [("The average temperature is twenty degrees.", "平均气温是二十度。"), ("It was an average day at school.", "那是普通的一个上学日。")], "typical：强调有代表性；average 可指统计平均或普通水平。", "unusual：不寻常的。", "average person 不必指经过计算的一个人。"),
        s(3, "v.", "to have a particular amount as an average", "平均达到某个数量", "平均为", [("average ten hours", "平均十小时"), ("average a score of eighty", "平均得八十分")], [("The train averages sixty miles an hour.", "这列火车平均时速六十英里。"), ("The class averaged eighty on the test.", "全班这次考试平均得八十分。")], "amount to：也可表示总计或达到；average 特指平均值。", "", "average 作动词后可直接接数字。"),
    ]),
})

ENTRIES.update({
    "award": head("award", "/əˈwɔːrd/", ["a", "ward"], ["n.", "v."], ["奖项", "授予"], [
        s(1, "n.", "a prize given for an achievement", "为成就而颁发的奖项", "奖项", [("win an award", "获奖"), ("an award for writing", "写作奖")], [("She won an award for her story.", "她的故事获得了一个奖项。"), ("The school gives an award each year.", "学校每年颁发一个奖项。")], "prize：泛指竞赛奖品；award 常是正式颁发的荣誉。", "", "award for 后接获奖的原因或领域。"),
        s(2, "v.", "to officially give someone a prize or something they deserve", "正式把奖品或应得之物授予某人", "授予", [("award a prize", "颁奖"), ("award a scholarship", "授予奖学金")], [("The judges awarded her first prize.", "评委给她颁发了一等奖。"), ("The university awarded him a scholarship.", "大学授予了他奖学金。")], "give：泛指给予；award 强调正式决定并授予。", "", "award someone something 表示授予某人某物。"),
    ]),
})


if __name__ == "__main__":
    main()
