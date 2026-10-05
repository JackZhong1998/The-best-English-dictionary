"""Original pilot candidates: common, compare, complete, concern, consider."""

import json
from pilot_drafts import OUT, sense

ENTRIES = {
    "common": {
        "phonetic": "/ˈkɑːmən/", "syllables": ["com", "mon"], "pos": ["adj."],
        "core_meanings": ["常见的", "共同的"],
        "etymology": "经古法语 comun，来自拉丁语 communis“共同的、共享的”。",
        "semantic_shift": "从多人共同拥有，发展为很多人都知道或经常遇见的事情。",
        "senses": [
            sense(1, "adj.", "happening or seen often", "经常发生或经常见到的", "常见的", [("a common mistake", "常见错误"), ("a common problem", "常见问题")], [("This is a common mistake in English.", "这是英语中的常见错误。"), ("Rain is common here in summer.", "这里夏天常下雨。")], "usual：强调按惯例会发生；common 强调发生或出现得多。", "rare：罕见的。", "common 不一定表示好或坏，只表示常见。"),
            sense(2, "adj.", "shared by two or more people", "由两个或更多人共同拥有的", "共同的", [("a common goal", "共同目标"), ("have much in common", "有很多共同点")], [("We share a common goal.", "我们有共同的目标。"), ("The two friends have much in common.", "这两个朋友有很多共同点。")], "shared：直接强调共同拥有；common 还可表示多人共有的特征。", "individual：属于个人的。", "have something in common 是有共同点，不是“有常见的东西”。"),
        ],
    },
    "compare": {
        "phonetic": "/kəmˈper/", "syllables": ["com", "pare"], "pos": ["v."],
        "core_meanings": ["比较", "比作"],
        "etymology": "经古法语 comparer，来自拉丁语 comparare，与 par“相等”有关。",
        "semantic_shift": "从把两者放在一起看是否相当，发展为比较异同，也可把一件事比作另一件事。",
        "senses": [
            sense(1, "v.", "to examine how two things are similar or different", "考察两者的相同与不同", "比较异同", [("compare prices", "比较价格"), ("compare two plans", "比较两个方案")], [("Compare the two pictures carefully.", "仔细比较这两幅画。"), ("We compared prices before buying the phone.", "买手机前我们比较了价格。")], "contrast：偏重指出差异；compare 可以同时看相同和不同。", "", "compare A with B 常用于比较异同；不要漏掉比较对象。"),
            sense(2, "v.", "to describe one thing as similar to another", "把一件事物说成像另一件事物", "比作", [("compare life to a journey", "把人生比作旅程"), ("compare someone to a hero", "把某人比作英雄")], [("She compared life to a journey.", "她把人生比作一段旅程。"), ("The writer compared the city to a garden.", "作者把这座城市比作花园。")], "liken：明确表示比作，语气较正式；compare to 更常见。", "", "compare A to B 在此是作比喻，不一定逐项分析异同。"),
        ],
    },
    "complete": {
        "phonetic": "/kəmˈpliːt/", "syllables": ["com", "plete"], "pos": ["adj.", "v."],
        "core_meanings": ["完整的", "完成的", "完成"],
        "etymology": "经古法语 complet 或直接来自拉丁语 completus，原有“填满、没有缺项”之意。",
        "semantic_shift": "从没有缺少部分，发展为工作各环节都已做完；动词表示把余下部分补齐。",
        "senses": [
            sense(1, "adj.", "having all its parts", "具备所有组成部分的", "完整的", [("a complete set", "完整的一套"), ("a complete list", "完整清单")], [("I have a complete set of the books.", "我有完整的一套书。"), ("Please send me the complete list.", "请把完整清单发给我。")], "whole：强调作为一个整体；complete 强调没有缺失部分。", "incomplete：不完整的。", "a complete list 指项目齐全，不一定是很长的清单。"),
            sense(2, "adj.", "finished and needing no more work", "已经结束且不需再做的", "完成的", [("the work is complete", "工作已完成"), ("the project is complete", "项目已完成")], [("The project is now complete.", "这个项目现在已经完成。"), ("The report will be complete tomorrow.", "报告明天就能完成。")], "finished：直接指结束；complete 强调所有必要工作都完成。", "unfinished：尚未完成的。", "complete 在这里描述完成状态，不是让人去完成。"),
            sense(3, "v.", "to finish a task or process", "完成任务或过程", "完成", [("complete a form", "填完表格"), ("complete a course", "完成课程")], [("Please complete the form today.", "请今天填完这张表。"), ("She completed the course last month.", "她上个月完成了这门课程。")], "finish：意思相近；complete 稍正式，也强调完成所有部分。", "leave unfinished：没有完成。", "complete 是动词时直接接任务：complete the form。"),
        ],
    },
    "concern": {
        "phonetic": "/kənˈsɜːrn/", "syllables": ["con", "cern"], "pos": ["n.", "v."],
        "core_meanings": ["担忧", "使担心", "涉及", "重要的事"],
        "etymology": "经古法语 concerner，与拉丁语 concernere“涉及、与……有关”有关。",
        "semantic_shift": "从与某事有关、值得注意，发展为关心其结果，进而产生担忧。",
        "senses": [
            sense(1, "n.", "a feeling of worry about something", "对某事感到担心", "担忧", [("express concern", "表示担忧"), ("cause concern", "引起担忧")], [("Parents expressed concern about the plan.", "家长们对这个计划表示担忧。"), ("The news caused great concern.", "这则消息引起了很大担忧。")], "worry：更日常，也可指具体烦恼；concern 稍正式。", "reassurance：让人安心的保证。", "concern about 后接担忧的事情，不是关心某人的同义结构。"),
            sense(2, "v.", "to make someone feel worried", "使某人感到担心", "使担心", [("concern the parents", "让家长担心"), ("be concerned about safety", "担心安全问题")], [("The delay concerns me.", "这次延误让我担心。"), ("We are concerned about the children.", "我们担心孩子们。")], "worry：更口语；concern 作动词稍正式。", "reassure：使人安心。", "be concerned about 表示担心；be concerned with 常表示涉及。"),
            sense(3, "v.", "to be about or involve someone or something", "与某人或某事有关或涉及它", "涉及", [("concern all students", "涉及所有学生"), ("a matter concerning health", "涉及健康的事情")], [("The new rule concerns all students.", "新规定涉及所有学生。"), ("This letter concerns your application.", "这封信与你的申请有关。")], "involve：强调包含或牵涉；concern 强调与某人或主题有关。", "", "The rule concerns you 可能只是“与你有关”，不一定令你担心。"),
            sense(4, "n.", "a matter that is important to someone", "对某人重要的一件事", "关心的事", [("a main concern", "主要关注点"), ("a matter of concern", "值得关注的事")], [("Safety is our main concern.", "安全是我们最关心的事。"), ("Cost is an important concern for families.", "费用是许多家庭关注的重要问题。")], "priority：强调优先处理的事；concern 强调在意的事。", "", "main concern 在此是主要关注点，不一定意味着害怕。"),
        ],
    },
    "consider": {
        "phonetic": "/kənˈsɪdər/", "syllables": ["con", "sid", "er"], "pos": ["v."],
        "core_meanings": ["仔细考虑", "认为", "顾及"],
        "etymology": "经古法语 considerer，来自拉丁语 considerare“仔细观察”；其更早构词解释尚有争议。",
        "semantic_shift": "从仔细观察，发展为认真思考选择；思考后也可表达对人或事的判断。",
        "senses": [
            sense(1, "v.", "to think carefully before deciding", "作决定前仔细思考", "仔细考虑", [("consider a plan", "考虑一个计划"), ("consider doing something", "考虑做某事")], [("Please consider the plan carefully.", "请认真考虑这个计划。"), ("She is considering changing jobs.", "她正在考虑换工作。")], "think about：泛指想一想；consider 暗示较认真地权衡。", "ignore：不予考虑。", "consider doing 后接动名词，不说 consider to do。"),
            sense(2, "v.", "to regard someone or something in a particular way", "把某人或某事看作某种情况", "认为", [("consider it important", "认为它重要"), ("consider someone a friend", "把某人当朋友")], [("I consider this result important.", "我认为这个结果很重要。"), ("They consider her a good leader.", "他们认为她是位好领导。")], "regard as：意思相近，但要有 as；consider 后常直接接名词或形容词。", "", "consider her a friend 不用加 as；regard her as a friend 要加 as。"),
            sense(3, "v.", "to take someone's needs or feelings into account", "做事时顾及他人的需要或感受", "顾及", [("consider other people's feelings", "顾及他人的感受"), ("consider everyone's needs", "考虑每个人的需要")], [("Please consider other people's feelings.", "请顾及他人的感受。"), ("We considered everyone's needs in the plan.", "制定计划时我们顾及了每个人的需要。")], "take into account：明确表示纳入考虑；consider 更简洁。", "disregard：不顾及。", "consider people 在这里是顾及他们，不是判断他们是什么人。"),
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
