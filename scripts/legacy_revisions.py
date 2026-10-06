"""Prepare editorial candidates for five grandfathered high-frequency entries.

Reads published entries and writes only content/candidates/legacy_revisions/.
Review and staging are intentionally separate steps.
"""

import json
from pathlib import Path
from pilot_drafts import sense

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "words"
OUT = ROOT / "content" / "candidates" / "legacy_revisions"


def load(word):
    return json.loads((SOURCE / f"{word}.json").read_text(encoding="utf-8"))


def renumber(entry):
    for index, item in enumerate(entry["senses"], 1):
        item["id"] = index


def revise_break():
    entry = load("break")
    entry["core_meanings"] = ["打碎", "打断", "违反", "出故障", "骨折", "休息"]
    first = entry["senses"][0]
    first["en_definition"] = "to separate something into pieces, or to separate into pieces"
    first["zh_definition"] = "使某物碎成几块，或自行碎成几块"
    first["usages"][0]["usage_label"] = "打碎或碎裂"
    first["usages"][0]["examples"][1] = {"en": "The plate broke into three pieces.", "zh": "盘子碎成了三块。"}
    entry["senses"] = [
        first,
        sense(2, "v.", "to interrupt the continuous course of something", "打断正在持续的活动或状态", "打断", [("break the flow", "打断连贯的过程"), ("break someone's concentration", "打断某人的注意力")], [("The alarm broke the flow of the lesson.", "警报打断了课堂的连贯进程。"), ("A phone call broke my concentration.", "一通电话打断了我的思路。")], "interrupt：直接表示打断；break 常强调原本连续的状态被打破。", "continue：使活动继续进行。", "break the flow 是打断进程，不是把东西砸碎。"),
        sense(3, "v.", "to act against a rule, law, or promise", "做出违反规则、法律或诺言的事", "违反", [("break a rule", "违反规则"), ("break the law", "违法")], [("You will be punished if you break the rules.", "如果违反规则，你会受到处罚。"), ("The company broke the law.", "那家公司违反了法律。")], "violate：也表示违反规则或法律，语气较正式。", "obey：遵守规则或法律。", "break a rule 是违反规则，不是撕毁写有规则的纸。"),
        sense(4, "v.", "to end a period of silence by making a sound", "通过发声结束一段沉默或安静", "打破沉默", [("break the silence", "打破沉默"), ("break the quiet", "打破宁静")], [("A loud knock broke the silence.", "一声响亮的敲门声打破了沉默。"), ("Her laughter broke the quiet.", "她的笑声打破了宁静。")], "interrupt：可指声音打断安静；break the silence 是更固定的表达。", "remain silent：继续保持沉默。", "这里的 break 表示让安静结束，没有东西真的碎掉。"),
        sense(5, "v.", "to stop working because of a fault", "机器或车辆因故障停止运转", "出故障", [("a car breaks down", "汽车抛锚"), ("a machine breaks down", "机器出故障")], [("Our car broke down on the way home.", "我们的车在回家路上抛锚了。"), ("The washing machine broke down yesterday.", "洗衣机昨天出了故障。")], "fail：也指机器失灵；break down 更常用于车辆和设备。", "work normally：正常运转。", "机器 break down 是出故障；人 break down 还可能指情绪崩溃。"),
        sense(6, "v.", "to fracture a bone", "使骨头断裂", "骨折", [("break an arm", "胳膊骨折"), ("break a leg", "腿骨折")], [("He broke his arm while skating.", "他滑冰时摔断了胳膊。"), ("She broke her leg in the fall.", "她摔倒时腿骨折了。")], "fracture：也指骨折，医疗语境中更常用。", "", "break a leg 在真实受伤语境中是骨折；作祝福语时还有“祝你好运”的特殊用法。"),
        *entry["senses"][3:],
    ]
    renumber(entry)
    return entry


def revise_get():
    entry = load("get")
    entry["core_meanings"] = ["得到", "到达", "变得", "理解", "起床"]
    fifth = entry["senses"][4]
    fifth["usages"][0]["examples"][1] = {"en": "I got two tickets for my parents.", "zh": "我给父母买了两张票。"}
    ninth = entry["senses"][8]
    ninth["usages"][0]["collocations"][1]["translation"] = "从失去某人或某物的打击中恢复"
    ninth["usages"][0]["examples"][1] = {"en": "It took her months to get over the loss of her dog.", "zh": "她花了几个月才从失去爱犬的悲痛中走出来。"}
    ninth["synonyms"] = ["recover：常指恢复健康；get over 还可指走出失去亲友的悲痛。"]
    entry["senses"].append(sense(11, "v.", "to rise from bed after sleeping", "睡醒后起床", "起床", [("get up early", "早起"), ("get up at six", "六点起床")], [("I get up at six on school days.", "上学的日子我六点起床。"), ("She got up early to catch the train.", "她早起赶火车。")], "rise：也可表示起身，但 get up 是日常起床的常见说法。", "go to bed：上床睡觉。", "get up 是起床；wake up 是醒来，醒后不一定马上起床。"))
    renumber(entry)
    return entry


def revise_run():
    entry = load("run")
    item = entry["senses"][2]
    item["usages"][0]["collocations"][1]["translation"] = "负责一门课程"
    item["usages"][0]["examples"][1]["zh"] = "她负责一个英语班。"
    item["synonyms"] = ["manage：管理；run a class 可指负责或主持课程，不一定是创办课程。"]
    return entry


def revise_set():
    entry = load("set")
    entry["core_meanings"] = ["放置", "设定", "一套", "凝固", "落下"]
    entry["semantic_shift"] = "从放到指定位置，扩展到设定时间、目标或设备参数；“一套”、凝固和日月落下按各自语境学习。"
    group = entry["senses"][3]
    group["en_definition"] = "a group of related things kept or used together"
    group["zh_definition"] = "一起保存或使用的一组相关物品"
    group["usages"][0]["collocations"][0]["translation"] = "一套钥匙"
    group["usages"][0]["examples"][0] = {"en": "She gave me a spare set of keys.", "zh": "她给了我一套备用钥匙。"}
    group["confusables"] = ["a set of keys 强调一起使用的一组钥匙；a key 只指一把钥匙。"]
    entry["senses"].insert(5, sense(6, "v.", "to go below the horizon at the end of the day or night", "太阳或月亮降到地平线以下", "落下", [("the sun sets", "太阳落山"), ("the moon sets", "月亮落下")], [("The sun sets early in winter.", "冬天天黑得早，太阳很早就落山了。"), ("We watched the moon set over the hills.", "我们看着月亮落到山后。")], "go down：口语中也可说太阳落下；set 更常用于日月落到地平线以下。", "rise：升起。", "太阳或月亮作主语时，set 不表示“放置”。"))
    renumber(entry)
    return entry


def revise_take():
    entry = load("take")
    entry["core_meanings"] = ["拿", "乘坐", "花费", "接受", "拍摄"]
    accepting = entry["senses"][3]
    accepting["usages"][0]["collocations"][1]["translation"] = "采纳建议"
    accepting["usages"][0]["examples"][1]["zh"] = "我采纳了他的建议。"
    departure = entry["senses"][5]
    departure["synonyms"] = ["depart：指离开出发地点；take off 专指飞机离地起飞。"]
    entry["senses"].insert(6, sense(7, "v.", "to make a photograph with a camera or phone", "用相机或手机拍摄照片", "拍照", [("take a photo", "拍一张照片"), ("take a picture of someone", "给某人拍照")], [("Can you take a photo of us?", "你能给我们拍张照片吗？"), ("She took a picture of the sunset.", "她拍了一张日落的照片。")], "photograph：动词，表示拍摄；take a photo 更常见于日常口语。", "", "take a photo of 后接拍摄对象；不能用 make a photo 表示拍照。"))
    renumber(entry)
    return entry


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    revisions = {
        "break": revise_break(),
        "get": revise_get(),
        "run": revise_run(),
        "set": revise_set(),
        "take": revise_take(),
    }
    for word, entry in revisions.items():
        (OUT / f"{word}.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(revisions)} legacy revision candidates")


if __name__ == "__main__":
    main()
