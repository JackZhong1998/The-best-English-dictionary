# 词表与制词流程

## 首批词表的来源与状态

`pilot_cet4.tsv` 是本项目独立挑选的 100 个常见英语词头与新写的基础中文提示，不是官方四级词表，也没有复制其他词典的释义、例句或选词顺序。`CET4-level candidate` 只表示计划面向四级程度读者；发布前仍需按教学范围核对。`catalog.json` 中的 `source_file` 指向可追溯的词表文件。

原有 30 个完整词条标为 `published`，但 `review_records` 为空：这表示此前没有独立复核记录，不把它们冒充为已复核。新写的 70 个词条完成独立复核后也已发布；100 词试批现均为完整词条。后续批次仍应让未完成精修的词保持 `basic` 状态。

四／六级扩词的选词清单、许可与解析方式见 [`content/sources/README.md`](sources/README.md)。第三方转录稿共 5,377 行；脚本提取 7,600 个明确独立拼写，214 个缩写或变体记法及 39 个需核对大小写的拼写保留待核对。行数不是词条总数。第五至第十二批各 25 词均已发布，分别有 97、79、76、84、80、78、74 和 84 个义项；每个词可追溯到原稿行号，词义与例句另行原创撰写。逐词四级／六级归属未从转录稿中确认，暂统一标“四／六级大纲候选”。

## 批次和复核

词表每批 25 个词，首批 100 个分成四批。一个本地 Codex 制词 Agent 按原有 JSON 接口写候选词条；另一个 Agent 查看义项区分、发音/音标、词源依据、例句自然度、搭配和辨析，然后记录结论。`content_pipeline.py` 不调用模型 API，也不会自行撰写词条。

首批 100 词中，**新写的每个完整词条均需独立复核**。以后每批至少抽取 3/25 词复核（按词头 SHA-256 排序固定样本），多音、多词源或短语动词的高风险词额外必审。第五批初审发现近义词误归类等重复性问题，第五至第十二批均已对全部 25 词逐词复核并修订，复核结果记录在 `catalog.json`。以后若抽检发现系统性错误，也应复核整批并暂停发布；这个质量判断不能由结构校验替代。

```bash
python3 scripts/content_pipeline.py status
python3 scripts/content_pipeline.py stage ability /path/to/ability.json --author agent-name
python3 scripts/content_pipeline.py review ability --reviewer another-agent --decision accept --notes '义项、例句和辨析已核对'
python3 scripts/content_pipeline.py publish ability
```

`stage` 检查主要结构、至少两组例句和搭配、例句长度；`review` 要求复核者与作者不同，并记录候选内容哈希；`publish` 再核对哈希。修改候选词条需重新 `stage`，旧复核记录失效。新增一个 25 词批次可用 `extend /path/to/new-batch.tsv --category CET6`，输入 TSV 必须含 `word` 和原创 `basic_zh` 两列；输入文件会保存到 `content/wordlists/`。六级、考研阶段的词表需要另行整理与核对，目前并未宣称已完成。

修订已发布词条时仍使用相同的 `stage → review → publish` 命令。`stage` 会在 `catalog.json` 的该词下记录 `revision`，保持主状态为 `published`，线上继续读取 `content/words/` 中的旧版本。另一位复核者接受新稿后，`publish` 校验内容哈希，再替换旧文件并增加版本号；原有复核记录不会丢失。中途停下可用 `status` 查看待修订词，随后从 `review` 或 `publish` 接着做。如果审核后修改了稿件，必须重新 `stage` 并复核。

`review` 可选填 `--issues-found 2 --corrections 1`，分别记录本次发现的问题数和已完成的修订数。未填时不写数字字段，批次报告将其显示为“未记录”，不会推测为零。

音频与内容是两个关卡：原有高频词发布时校验预生成音频；第五批按扩词优先的要求暂不生成音频，保留按需 TTS 接口。任何线上生成失败都应保留可读的文字内容。

首批候选词的词源事实核对参考 [ability](https://www.etymonline.com/word/ability)、[accept](https://www.etymonline.com/word/accept)、[access](https://www.etymonline.com/word/access)、[achieve](https://www.etymonline.com/word/achieve)、[active](https://www.etymonline.com/word/active) 的 Etymonline 词条；中文说明为重新撰写的简述，并非复制原文。

第二组候选词参考 [activity](https://www.etymonline.com/word/activity)、[advantage](https://www.etymonline.com/word/advantage)、[affect](https://www.etymonline.com/word/affect)、[afford](https://www.etymonline.com/word/afford)、[agree](https://www.etymonline.com/word/agree) 的 Etymonline 词条。

接下来的十词分别核对了 Etymonline 的 [address](https://www.etymonline.com/word/address)、[allow](https://www.etymonline.com/word/allow)、[almost](https://www.etymonline.com/word/almost)、[among](https://www.etymonline.com/word/among)、[amount](https://www.etymonline.com/word/amount)、[appear](https://www.etymonline.com/word/appear)、[apply](https://www.etymonline.com/word/apply)、[approach](https://www.etymonline.com/word/approach)、[area](https://www.etymonline.com/word/area)、[argue](https://www.etymonline.com/word/argue) 词源词条。词源以可核查的简述为限；例如 area 的更早来源不确定，不写成确定的拉丁语词根演化链。

第三组十词的词源简述参考 Etymonline 的 [arrange](https://www.etymonline.com/word/arrange)、[arrive](https://www.etymonline.com/word/arrive)、[article](https://www.etymonline.com/word/article)、[attend](https://www.etymonline.com/word/attend)、[avoid](https://www.etymonline.com/word/avoid)、[basic](https://www.etymonline.com/word/basic)、[become](https://www.etymonline.com/word/become)、[begin](https://www.etymonline.com/word/begin)、[believe](https://www.etymonline.com/word/believe)、[benefit](https://www.etymonline.com/word/benefit) 词条。前两词由独立复核 Agent 检查，后八词在制词 Agent 中断后由未参与撰写的主 Agent 逐词复核；复核身份和结果记录在 `catalog.json`。

第四组十词的词源事实参考 Etymonline 的 [build](https://www.etymonline.com/word/build)、[business](https://www.etymonline.com/word/business)、[cause](https://www.etymonline.com/word/cause)、[choose](https://www.etymonline.com/word/choose)、[collect](https://www.etymonline.com/word/collect)、[common](https://www.etymonline.com/word/common)、[compare](https://www.etymonline.com/word/compare)、[complete](https://www.etymonline.com/word/complete)、[concern](https://www.etymonline.com/word/concern)、[consider](https://www.etymonline.com/word/consider)。制词 Agent 写候选稿，未参与撰写的主 Agent 逐词复核并修订两处表达；复核记录在 `catalog.json`。

第五组十词的词源事实参考 Etymonline 的 [contain](https://www.etymonline.com/word/contain)、[continue](https://www.etymonline.com/word/continue)、[control](https://www.etymonline.com/word/control)、[create](https://www.etymonline.com/word/create)、[culture](https://www.etymonline.com/word/culture)、[decide](https://www.etymonline.com/word/decide)、[develop](https://www.etymonline.com/word/develop)、[difference](https://www.etymonline.com/word/difference)、[effect](https://www.etymonline.com/word/effect)、[effort](https://www.etymonline.com/word/effort)。全部由另一位 Agent 逐词复核，发现的表达问题修订后才发布。预生成音频的新鲜度由 `audio_manifest.json` 和构建校验共同检查。

本组十词的词源与词义迁移说明核对了 Etymonline 的 [enough](https://www.etymonline.com/word/enough)、[enter](https://www.etymonline.com/word/enter)、[environment](https://www.etymonline.com/word/environment)、[example](https://www.etymonline.com/word/example)、[expect](https://www.etymonline.com/word/expect)、[experience](https://www.etymonline.com/word/experience)、[explain](https://www.etymonline.com/word/explain)、[express](https://www.etymonline.com/word/express)、[fact](https://www.etymonline.com/word/fact)、[fail](https://www.etymonline.com/word/fail) 词条；中文说明由本项目独立撰写。

最后十个候选词的词源简述参考 Etymonline 的 [focus](https://www.etymonline.com/word/focus)、[follow](https://www.etymonline.com/word/follow)、[improve](https://www.etymonline.com/word/improve)、[include](https://www.etymonline.com/word/include)、[increase](https://www.etymonline.com/word/increase)、[influence](https://www.etymonline.com/word/influence)、[information](https://www.etymonline.com/word/information)、[involve](https://www.etymonline.com/word/involve)、[issue](https://www.etymonline.com/word/issue)、[knowledge](https://www.etymonline.com/word/knowledge)。词源只简述可核实的主要来路：focus 的拉丁语更早来源与 knowledge 的词尾来源不确定，不作推断。increase 名词和动词的重音不同，候选词条仅以动词读音作主音标，名词读音写入辨析；独立复核时需核对单词音频读音。

第六组十词的词源事实参考 Etymonline 的 [enough](https://www.etymonline.com/word/enough)、[enter](https://www.etymonline.com/word/enter)、[environment](https://www.etymonline.com/word/environment)、[example](https://www.etymonline.com/word/example)、[expect](https://www.etymonline.com/word/expect)、[experience](https://www.etymonline.com/word/experience)、[explain](https://www.etymonline.com/word/explain)、[express](https://www.etymonline.com/word/express)、[fact](https://www.etymonline.com/word/fact)、[fail](https://www.etymonline.com/word/fail)。主 Agent 对作者候选稿独立检查义项、例句、中译及辨析后发布。

原有高频词的 `break`、`get`、`run`、`set`、`take` 已完成独立复核修订，五词均升至内容版本 2。`set` 的日月落下定义和 `take someone’s advice` 的搭配、辨析在复核后修正，最终稿由主 Agent 再检查。

最后十词的词源事实参考 Etymonline 的 [focus](https://www.etymonline.com/word/focus)、[follow](https://www.etymonline.com/word/follow)、[improve](https://www.etymonline.com/word/improve)、[include](https://www.etymonline.com/word/include)、[increase](https://www.etymonline.com/word/increase)、[influence](https://www.etymonline.com/word/influence)、[information](https://www.etymonline.com/word/information)、[involve](https://www.etymonline.com/word/involve)、[issue](https://www.etymonline.com/word/issue)、[knowledge](https://www.etymonline.com/word/knowledge)。独立 QA 指出 `focus` 词源先后、`follow` 高频时序义缺项、`information` 重复义项和 `increase` 名动词重音问题，主 Agent 修订并核对最终稿。`increase` 的两种美音以 `to increase` 和 `an increase` 短语录音示范，避免孤立拼写的重音歧义；两段录音均受文件和文本哈希校验。Cambridge 列出[动词和名词的不同重音](https://dictionary.cambridge.org/pronunciation/english/increase)。
