"""Five original editorial candidates for the first CET4-level batch.

Run locally and stage the output with content_pipeline.py. These candidates
are intentionally not marked reviewed or published by this script.
"""

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "content" / "candidates"


def sense(number, pos, en, zh, usage, collocations, examples, synonym, antonym, confusable):
    return {
        "id": number,
        "part_of_speech": pos,
        "en_definition": en,
        "zh_definition": zh,
        "usages": [{
            "usage_label": usage,
            "collocations": [{"phrase": phrase, "translation": translation} for phrase, translation in collocations],
            "examples": [{"en": english, "zh": chinese} for english, chinese in examples],
        }],
        "synonyms": [synonym] if synonym else [],
        "antonyms": [antonym] if antonym else [],
        "confusables": [confusable] if confusable else [],
    }


ENTRIES = {
    "ability": {
        "phonetic": "/əˈbɪləti/",
        "syllables": ["a", "bil", "i", "ty"],
        "pos": ["n."],
        "core_meanings": ["能力", "才能"],
        "etymology": "经古法语 ableté，最终与拉丁语 habilitas“能力、适合”有关。",
        "semantic_shift": "先指能够做某事的总体能力；复数 abilities 常指一个人在某些方面的具体才能。",
        "senses": [
            sense(1, "n.", "the power to do something", "做某事的能力", "能力", [("the ability to learn", "学习能力"), ("lose the ability to walk", "失去行走能力")], [("She has the ability to lead.", "她有领导能力。"), ("Daily practice can improve your ability to understand spoken English.", "每天练习能提高你听懂英语口语的能力。")], "capacity：也指做事的能力；ability 更常直接说某人能做什么。", "inability：缺乏做某事的能力。", "ability to do something 后接动词原形，不能说 ability of do something。"),
            sense(2, "n.", "a skill or talent in a particular area", "某方面的才能", "才能", [("musical ability", "音乐才能"), ("natural ability", "天赋")], [("Her musical ability impressed us.", "她的音乐才能给我们留下了深刻印象。"), ("The team values different abilities.", "这个团队重视不同的才能。")], "talent：常强调天赋；ability 也可以靠学习和练习培养。", "lack of skill：表示缺乏相关技能。", "ability 是名词；able 是形容词，不能说 she is ability。"),
        ],
    },
    "accept": {
        "phonetic": "/əkˈsept/",
        "syllables": ["ac", "cept"],
        "pos": ["v."],
        "core_meanings": ["接受", "同意", "承认"],
        "etymology": "经古法语 accepter 或直接由拉丁语 acceptare 进入英语，原有“接过、接受”之意。",
        "semantic_shift": "从接过别人给的东西，扩展到同意提议，以及在心里承认现实。",
        "senses": [
            sense(1, "v.", "to take something that someone offers", "收下别人给的东西", "收下", [("accept a gift", "收下礼物"), ("accept payment", "接受付款")], [("Please accept this small gift.", "请收下这份小礼物。"), ("The shop does not accept cash.", "这家店不收现金。")], "receive：指收到，未必表示愿意收下；accept 包含愿意接受。", "refuse：拒绝收下。", "accept 是主动接受；except 是介词，意思是“除……之外”。"),
            sense(2, "v.", "to agree to an offer or request", "同意提议或请求", "同意", [("accept an offer", "接受提议"), ("accept an invitation", "接受邀请")], [("She accepted the job offer.", "她接受了那份工作邀请。"), ("I accepted his invitation to dinner.", "我接受了他的晚餐邀请。")], "agree to：明确表示同意；accept 还可指正式接受一个提议。", "reject：拒绝提议。", "accept an offer 是同意提议；receive an offer 只是收到提议。"),
            sense(3, "v.", "to recognize an unpleasant fact as true", "承认并面对不愿接受的事实", "承认现实", [("accept the truth", "接受事实"), ("accept reality", "接受现实")], [("He finally accepted the truth.", "他终于接受了事实。"), ("She accepted that the plan had failed.", "她接受了计划已经失败的事实。")], "acknowledge：强调承认事实存在；accept 还含愿意面对它。", "deny：否认事实。", "accept that 后接完整句子；accept the truth 后接名词。"),
            sense(4, "v.", "to take responsibility or blame for something", "承担责任或过错", "承担责任", [("accept responsibility", "承担责任"), ("accept the blame", "承担过错")], [("We must accept responsibility for the mistake.", "我们必须为这个错误承担责任。"), ("He accepted the blame for the delay.", "他为这次延误承担了责任。")], "take responsibility：更常见的说法；accept 强调愿意承认并承担。", "deny responsibility：否认自己有责任。", "accept responsibility 是承担责任，不是接过一个叫“责任”的物品。"),
        ],
    },
    "access": {
        "phonetic": "/ˈækses/",
        "syllables": ["ac", "cess"],
        "pos": ["n.", "v."],
        "core_meanings": ["进入或使用的机会", "通道", "获取"],
        "etymology": "经古法语 acces，最终来自拉丁语 accessus“走近、进入”；动词用法由名词发展而来。",
        "semantic_shift": "从走近一个地方，扩展到进入的通道或权利；现代用法也指获取数字信息。",
        "senses": [
            sense(1, "n.", "the right or chance to use something", "使用某物的权利或机会", "使用权", [("have access to the internet", "可以上网"), ("easy access to information", "便于获取信息")], [("All students have access to the library.", "所有学生都可以使用图书馆。"), ("Many homes still lack access to clean water.", "许多家庭仍无法获得洁净的水。")], "availability：强调东西可供使用；access 强调人能够接触或使用它。", "lack of access：表示无法获得使用机会。", "access to 后接名词；这里的 to 是介词，不接动词原形。"),
            sense(2, "n.", "a way into a place", "进入某处的通道", "通道", [("road access", "道路通行条件"), ("access to the building", "进入大楼的通道")], [("This gate gives access to the garden.", "这扇门通往花园。"), ("The road provides access to the village.", "这条路通往村庄。")], "entrance：多指具体入口；access 也可指通往入口的道路。", "exit：离开的出口。", "access 在此是“通道”，不只是登录账号的权限。"),
            sense(3, "v.", "to find or use information or a service", "获取或使用信息、服务", "获取信息", [("access a website", "访问网站"), ("access your files", "读取你的文件")], [("You can access the course online.", "你可以在线使用这门课程。"), ("I cannot access my files today.", "我今天无法读取我的文件。")], "retrieve：强调把资料取回；access 强调能够进入系统或使用资料。", "block：阻止访问。", "access 作动词直接接宾语：access a website，不说 access to a website。"),
        ],
    },
    "achieve": {
        "phonetic": "/əˈtʃiːv/",
        "syllables": ["a", "chieve"],
        "pos": ["v."],
        "core_meanings": ["实现", "取得"],
        "etymology": "源自古法语 achever“完成、做成”，与“到达终点”的表达有关。",
        "semantic_shift": "从做完一件事，发展为通过努力达到目标或取得成果。",
        "senses": [
            sense(1, "v.", "to succeed in doing or getting something through effort", "通过努力实现或取得", "取得成果", [("achieve a goal", "实现目标"), ("achieve success", "获得成功")], [("She worked hard to achieve her goal.", "她努力实现自己的目标。"), ("The team achieved a good result.", "这个团队取得了好成绩。")], "accomplish：也表示完成；achieve 常搭配目标、成果或成功。", "fail to achieve：未能实现。", "achieve 强调达到目标；receive 只是收到某物。"),
        ],
    },
    "active": {
        "phonetic": "/ˈæktɪv/",
        "syllables": ["ac", "tive"],
        "pos": ["adj."],
        "core_meanings": ["活跃的", "积极参与的", "运行中的"],
        "etymology": "经古法语 actif 或直接来自拉丁语 activus，与“做、行动”有关。",
        "semantic_shift": "从能够行动，扩展到人积极参与、身体常活动，以及系统正在运行。",
        "senses": [
            sense(1, "adj.", "moving or doing many things", "经常活动、充满活力的", "活跃的", [("an active child", "活泼的孩子"), ("stay active", "保持活跃")], [("My grandfather stays active every day.", "我爷爷每天都活动身体。"), ("The children are very active this morning.", "孩子们今天早上很活跃。")], "energetic：强调精力充沛；active 强调经常活动。", "inactive：不活跃的。", "active 不等于 athletic；后者更强调运动能力。"),
            sense(2, "adj.", "taking part in something", "积极参与某事的", "积极参与", [("an active member", "积极参与的成员"), ("take an active part", "积极参与")], [("She is an active member of the club.", "她是俱乐部的活跃成员。"), ("Students should take an active part in class.", "学生应该积极参与课堂活动。")], "involved：表示参与其中；active 更强调主动做事。", "passive：被动的，不主动参与的。", "active member 指积极参与的成员，不一定指运动员。"),
            sense(3, "adj.", "currently in use or still valid", "目前仍在使用或有效的", "有效的", [("an active account", "有效账户"), ("an active membership", "有效会员资格")], [("Your account is still active.", "你的账户仍然有效。"), ("My membership is active until June.", "我的会员资格有效期到六月。")], "valid：强调法律或规则上有效；active 强调仍可使用。", "inactive：处于停用状态的。", "active account 表示账户有效或仍在使用，不是账户自己会行动。"),
        ],
    },
}


def main():
    OUT.mkdir(exist_ok=True)
    for word, data in ENTRIES.items():
        entry = {"word": word, **data}
        (OUT / f"{word}.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRIES)} candidate entries to {OUT}")


if __name__ == "__main__":
    main()
