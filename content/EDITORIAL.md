# 词表与制词流程

## 首批词表的来源与状态

`pilot_cet4.tsv` 是本项目独立挑选的 100 个常见英语词头与新写的基础中文提示，不是官方四级词表，也没有复制其他词典的释义、例句或选词顺序。`CET4-level candidate` 只表示计划面向四级程度读者；发布前仍需按教学范围核对。`catalog.json` 中的 `source_file` 指向可追溯的词表文件。

现有 30 个完整词条标为 `published`，但 `review_records` 为空：这表示此前没有独立复核记录，不把它们冒充为已复核。其余 70 个只有 `basic_zh`，标为 `basic`，不能展示不存在的详细释义或播放按钮。

## 批次和复核

词表每批 25 个词，首批 100 个分成四批。一个本地 Codex 制词 Agent 按原有 JSON 接口写候选词条；另一个 Agent 查看义项区分、发音/音标、词源依据、例句自然度、搭配和辨析，然后记录结论。`content_pipeline.py` 不调用模型 API，也不会自行撰写词条。

首批 100 词中，**新写的每个完整词条均需独立复核**。以后每批至少抽取 3/25 词复核（按词头 SHA-256 排序固定样本），多音、多词源或短语动词的高风险词额外必审。抽检发现重复性错误时，应人工复核整批并暂停发布；这个质量判断不能由结构校验替代。

```bash
python3 scripts/content_pipeline.py status
python3 scripts/content_pipeline.py stage ability /path/to/ability.json --author agent-name
python3 scripts/content_pipeline.py review ability --reviewer another-agent --decision accept --notes '义项、例句和辨析已核对'
python3 scripts/content_pipeline.py publish ability
```

`stage` 检查主要结构、至少两组例句和搭配、例句长度；`review` 要求复核者与作者不同，并记录候选内容哈希；`publish` 再核对哈希。修改候选词条需重新 `stage`，旧复核记录失效。新增一个 25 词批次可用 `extend /path/to/new-batch.tsv --category CET6`，输入 TSV 必须含 `word` 和原创 `basic_zh` 两列；输入文件会保存到 `content/wordlists/`。六级、考研阶段的词表需要另行整理与核对，目前并未宣称已完成。

音频与内容是两个关卡：高频词发布时校验预生成音频；其他词须在站点的在线 TTS 及缓存可用后才开放相应播放入口。任何线上生成失败都应保留可读的文字内容。

首批候选词的词源事实核对参考 [ability](https://www.etymonline.com/word/ability)、[accept](https://www.etymonline.com/word/accept)、[access](https://www.etymonline.com/word/access)、[achieve](https://www.etymonline.com/word/achieve)、[active](https://www.etymonline.com/word/active) 的 Etymonline 词条；中文说明为重新撰写的简述，并非复制原文。

第二组候选词参考 [activity](https://www.etymonline.com/word/activity)、[advantage](https://www.etymonline.com/word/advantage)、[affect](https://www.etymonline.com/word/affect)、[afford](https://www.etymonline.com/word/afford)、[agree](https://www.etymonline.com/word/agree) 的 Etymonline 词条。
