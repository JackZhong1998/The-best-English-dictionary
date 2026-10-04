"""Fourth group of original pilot candidates: appear through argue."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "appear": {
        "phonetic": "/əˈpɪr/", "syllables": ["ap", "pear"], "pos": ["v."],
        "core_meanings": ["出现", "似乎", "出场"],
        "etymology": "经古法语 aparoir，最终来自拉丁语 apparere“出现、显现”。",
        "semantic_shift": "从进入视野，扩展到在公众面前出现；事情呈现某种样子时，也可以表示“似乎”。",
        "senses": [
            sense(1, "v.", "to come into sight", "进入视野，出现", "出现", [("appear suddenly", "突然出现"), ("appear in the sky", "出现在天空中")], [("A rainbow appeared after the rain.", "雨后出现了一道彩虹。"), ("The sun appeared from behind the clouds.", "太阳从云后露了出来。")], "emerge：强调从隐藏处显露出来；appear 泛指进入视野。", "disappear：消失。", "appear 是出现；disappear 是消失，前缀 dis- 改变了意思。"),
            sense(2, "v.", "to seem to be true or to have a quality", "看起来似乎如此", "似乎", [("appear to be tired", "看起来很累"), ("it appears that", "看起来似乎……")], [("She appears to be tired.", "她看起来很累。"), ("It appears that we are late.", "看起来我们迟到了。")], "seem：也表示似乎；appear 稍正式，常基于可观察到的迹象。", "", "appear to do 表示看起来会做某事，不一定真的如此。"),
            sense(3, "v.", "to take part in a show or public event", "在节目或公众活动中出场", "出场", [("appear on television", "上电视"), ("appear in a film", "出演电影")], [("He appeared on television last night.", "他昨晚出现在电视节目中。"), ("She appeared in several films.", "她出演过几部电影。")], "perform：强调表演行为；appear 只强调在节目中出场。", "be absent：没有出场。", "appear in a film 是参演电影，不只是偶然出现在画面里。"),
        ],
    },
    "apply": {
        "phonetic": "/əˈplaɪ/", "syllables": ["ap", "ply"], "pos": ["v."],
        "core_meanings": ["申请", "应用", "涂抹", "适用"],
        "etymology": "经古法语 aploiier，来自拉丁语 applicare“贴近、连接”。",
        "semantic_shift": "从把一物贴到另一物，发展为把方法用到问题上、把药膏涂到皮肤上；申请则是把自己的请求提交给机构。",
        "senses": [
            sense(1, "v.", "to formally ask for a job or place", "正式申请职位或名额", "申请", [("apply for a job", "申请工作"), ("apply to a university", "向大学申请")], [("I applied for a summer job.", "我申请了一份暑期工作。"), ("She applied to three universities.", "她向三所大学提交了申请。")], "request：泛指提出请求；apply 通常要遵循正式申请程序。", "withdraw an application：撤回申请。", "apply for 后接职位或机会；apply to 后接接收申请的机构。"),
            sense(2, "v.", "to use a rule or method in a situation", "把规则或方法用于某种情况", "应用", [("apply a method", "应用一种方法"), ("apply a rule to a case", "把规则用于一个具体情况")], [("We can apply this method to the problem.", "我们可以把这种方法用于这个问题。"), ("The teacher applied the same rule to everyone.", "老师把同一条规则用于每个人。")], "use：泛指使用；apply 更强调把方法或规则用在具体对象上。", "ignore a rule：不采用某项规则。", "apply something to something 中的 to 指应用对象。"),
            sense(3, "v.", "to put a substance on a surface", "把物质涂在表面上", "涂抹", [("apply sunscreen", "涂防晒霜"), ("apply cream to the skin", "把乳霜涂在皮肤上")], [("Apply sunscreen before you go out.", "出门前涂防晒霜。"), ("She applied cream to her hands.", "她在手上涂了乳霜。")], "spread：强调把东西摊开；apply 强调把它涂到指定表面。", "remove：从表面移除。", "apply cream to your hands 是把乳霜涂到手上，不是“申请乳霜”。"),
            sense(4, "v.", "to be relevant to a person or situation", "对某人或某种情况适用", "适用", [("the rule applies to everyone", "规则适用于所有人"), ("this does not apply", "这一点不适用")], [("This rule applies to all students.", "这条规则适用于所有学生。"), ("The discount does not apply here.", "这里不适用这项折扣。")], "be relevant to：指与某事有关；apply to 还表示规则可具体使用。", "be exempt from：不受某项规则约束。", "此义的 apply 不及物，常说 a rule applies to someone。"),
        ],
    },
    "approach": {
        "phonetic": "/əˈproʊtʃ/", "syllables": ["ap", "proach"], "pos": ["v.", "n."],
        "core_meanings": ["靠近", "着手处理", "方法"],
        "etymology": "经古法语 aprochier，最终与拉丁语 prope“近”有关。",
        "semantic_shift": "从空间上靠近，扩展到时间临近；接近一个难题时，可以表示开始处理它的方式。",
        "senses": [
            sense(1, "v.", "to move nearer to someone or something", "在空间上接近人或物", "靠近", [("approach the door", "走近门"), ("approach someone carefully", "小心地走近某人")], [("The train approached the station.", "火车驶近车站。"), ("A stranger approached me on the street.", "一位陌生人在街上向我走来。")], "come near：直接说靠近；approach 语气稍正式。", "move away：移开，远离。", "approach 作动词直接接地点，不说 approach to the station。"),
            sense(2, "v.", "to come near in time", "在时间上临近", "临近", [("winter approaches", "冬天临近"), ("as the deadline approaches", "随着截止日期临近")], [("The exam is approaching quickly.", "考试很快就要到了。"), ("As winter approaches, days get shorter.", "随着冬天临近，白天变短了。")], "draw near：也表示临近；approach 稍正式。", "", "the exam approaches 指考试快到了，考试不会真的移动。"),
            sense(3, "n.", "a way of dealing with a problem", "处理问题的一种方法", "方法", [("a new approach", "一种新方法"), ("an approach to learning", "一种学习方法")], [("We need a different approach to this problem.", "我们需要用不同的方法处理这个问题。"), ("Her approach to learning is practical.", "她的学习方法很务实。")], "method：常指具体步骤；approach 更强调总体思路。", "", "名词 approach to 后常接问题或活动；动词 approach 直接接宾语。"),
            sense(4, "v.", "to start dealing with a task or problem", "着手处理任务或问题", "着手处理", [("approach a problem", "着手处理问题"), ("approach a task carefully", "谨慎地处理任务")], [("Let's approach this problem calmly.", "我们冷静地处理这个问题吧。"), ("She approached the task with care.", "她认真地着手处理这项任务。")], "tackle：更强调积极解决难题；approach 强调采取何种方式着手。", "avoid：回避问题。", "approach a problem 在此不是走近一个实体物体。"),
        ],
    },
    "area": {
        "phonetic": "/ˈeriə/", "syllables": ["ar", "e", "a"], "pos": ["n."],
        "core_meanings": ["地区", "面积", "领域"],
        "etymology": "直接来自拉丁语 area“平地、空地”；更早来源不确定。",
        "semantic_shift": "从一块具体的地面，扩展到有边界的地区；再用于抽象的研究或工作领域。",
        "senses": [
            sense(1, "n.", "a particular part of a place", "某个地方的一片区域", "地区", [("a quiet area", "安静的区域"), ("the local area", "当地地区")], [("This area is quiet at night.", "这一带夜里很安静。"), ("Many families live in the area.", "许多家庭住在这一带。")], "region：常指较大的地区；area 大小更灵活。", "", "area 可以是城市的一小片地方，不一定是很大的地区。"),
            sense(2, "n.", "the size of a surface", "平面所占的大小", "面积", [("measure the area", "测量面积"), ("a large area", "大面积")], [("We measured the area of the room.", "我们测量了房间的面积。"), ("The park covers a large area.", "这座公园占地很广。")], "size：泛指大小；area 专指平面的面积。", "", "面积用 area；体积用 volume，两者不是同一量。"),
            sense(3, "n.", "a subject or field of work", "工作或研究的一个领域", "领域", [("an area of study", "一个研究领域"), ("areas of interest", "感兴趣的领域")], [("Language is her main area of study.", "语言是她的主要研究领域。"), ("We work in different areas of science.", "我们在科学的不同领域工作。")], "field：也表示学科或领域；area 可指其中较具体的部分。", "", "area of study 是研究领域，不是实验室的地面面积。"),
        ],
    },
    "argue": {
        "phonetic": "/ˈɑːrɡjuː/", "syllables": ["ar", "gue"], "pos": ["v."],
        "core_meanings": ["争论", "论证", "主张"],
        "etymology": "经古法语 arguer，最终与拉丁语 arguere“说明、证明”有关。",
        "semantic_shift": "从用理由说明观点，发展出与人意见相左时的争论；在正式语境中仍保留提出论据的意思。",
        "senses": [
            sense(1, "v.", "to disagree with someone, often angrily", "与人意见不合并发生争论，常带怒气", "争论", [("argue with a friend", "与朋友争论"), ("argue about money", "为钱争吵")], [("They argued about the price.", "他们为价格争论起来。"), ("I do not want to argue with you.", "我不想和你争吵。")], "quarrel：更强调不愉快的争吵；argue 也可指理性讨论。", "agree：意见一致。", "argue with 后接争论对象；argue about 后接争论话题。"),
            sense(2, "v.", "to give reasons for a position", "提出理由支持某个观点", "论证", [("argue for change", "提出理由支持改变"), ("argue against a plan", "提出反对计划的理由")], [("She argued for a change in the rules.", "她提出了修改规则的理由。"), ("He argued against the new plan.", "他提出理由反对新计划。")], "reason：偏重推理过程；argue 强调提出一套理由。", "accept without question：不经质疑就接受。", "argue for 是提出支持理由，不一定是吵架。"),
            sense(3, "v.", "to say that something is true and give reasons", "有理由地主张某事属实", "主张", [("argue that something is true", "论证某事属实"), ("argue the case", "为某个主张提出理由")], [("The writer argues that reading builds empathy.", "作者主张阅读能培养同理心。"), ("Some experts argue that the rule is unfair.", "一些专家认为这项规定不公平，并提出了理由。")], "claim：仅表示声称；argue 暗示会给出理由。", "concede：承认对方观点有道理。", "argue that 后接完整句子，常用于文章和正式讨论。"),
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
