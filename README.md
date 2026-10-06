# 词义之间

面向中文学习者的英汉词典。网站先收录词头和原创基础释义，再由本地 Codex 制作并复核完整词条；尚未精修的词仍可查询。现已发布 125 个完整词条，包括 100 词试批和第五批 25 个四／六级大纲候选词。前 100 词附有 869 个预生成音频文件，新扩词暂不预生成音频。`content/catalog.json` 保存每词的状态与复核记录；首批的“CET4-level candidate”是独立编辑选择，不声称来自官方四级词表。

## 本地运行和校验

```bash
npm ci
npm run dev
npm run build
python3 -m unittest scripts/test_audio.py scripts/test_content_pipeline.py
node scripts/import_entries.mjs --dry-run
python3 scripts/content_pipeline.py status
python3 scripts/cet_progress.py
node scripts/batch_report.mjs
```

Vite 开发服务器使用导出的静态试批数据，入口为 `http://127.0.0.1:5173/`。构建检查覆盖 JSON 字段、基础释义、重复例句、例句长度、已预生成音频的引用以及前端类型。已复核的新词可走按需 TTS，不要求提前提交 MP3。

## 内容流水线

- `content/catalog.json` 是可恢复进度清单，保存来源、考试类别、`basic`/`draft`/`reviewed`/`published` 状态、版本和复核记录。`draft` 和 `reviewed` 在线上显示为基础释义；只有 `published` 才显示完整词条。
- `content/pilot_cet4.tsv` 是独立整理的 100 词试批。新增四／六级词头以 [MIT 许可的 2016 大纲转录稿](content/sources/README.md)为选词清单，不复制第三方释义或例句。`scripts/build_cet_backlog.py` 将原稿拆为 7,600 个明确拼写、214 个待核对的变体记法及 39 个需核对大小写的拼写；`scripts/cet_progress.py` 报告已发布覆盖。转录稿没有可靠的逐词等级标签，核定前只标“四／六级大纲候选”。
- `scripts/content_pipeline.py` 提供 `status`、`stage`、`review`、`publish` 等命令。候选 JSON 先进入 `content/drafts/`，独立复核通过后才进入 `content/words/`。当前试批首批逐词复核；后续每批 25 词，抽检至少 10%，另查多音、多词源、短语动词等高风险词。出现系统性错误时复核整批。
- 已发布词条可通过同样的 `stage → review → publish` 路径修订，审核期间旧版仍可读。`review --issues-found N --corrections N` 为后续批次记录结构化质量数据；`scripts/batch_report.mjs` 汇总每批词数、复核记录及音频完整性，历史未记录的错误数显示为未知，不推测。
- 原有 30 词的生成源在 `scripts/build_content.py`，音频生成脚本在 `scripts/generate_audio.py`。`content/audio_manifest.json` 记录文本、音色和参数的哈希；修改例句后脚本会重做相应 MP3，构建校验也会拒绝过期音频。词源和词义迁移无可靠说明时可以留空。

## Vercel 部署

`vercel.json` 保证 `/word/:word` 直达链接返回 Vite 页面。网页从 `/api/words` 分页查询词头，从 `/api/entries/:word` 获取单个词条；当数据库不可用时，已发布的 125 词仍可通过静态导出阅读。正式扩大到数万词时，数据库是搜索的主要来源，不能把完整 JSON 打进浏览器包。

运行数据库初始化脚本 `db/schema.sql`、`db/audio.sql`，在 Vercel 项目设置 `DATABASE_URL`，然后运行 `node scripts/import_entries.mjs`。每次内容发布后可用 `node scripts/import_entries.mjs --batch N` 仅导入对应 25 词批次；脚本按词头幂等更新，中断后可重跑。Python Function 的依赖列在 `requirements.txt`。按需发音还需要以下环境变量：

| 变量 | 用途 |
| --- | --- |
| `R2_ACCOUNT_ID`、`R2_BUCKET` | Cloudflare R2 账号和桶 |
| `R2_ACCESS_KEY_ID`、`R2_SECRET_ACCESS_KEY` | 仅限目标桶的读写凭据 |
| `AUDIO_VISITOR_SALT` | 匿名访客每日限额的哈希盐 |
| `AUDIO_GENERATION_ENABLED` | 预览环境实测时设为 `1`；默认关闭在线生成 |
| `AUDIO_VISITOR_DAILY_LIMIT` | 可选，默认每天 5 次新生成 |
| `AUDIO_GLOBAL_DAILY_LIMIT` | 可选，默认全站每天 100 次新生成 |
| `AUDIO_STORAGE_MAX_BYTES` | 可选，默认 8 GB；达到阈值暂停新增生成 |

当前 Cloudflare 中已创建私有桶 `best-english-dictionary-audio`，Vercel 的 `tts-preview` 分支已配置桶名及账号 ID。尚未创建该桶专用访问凭证，也尚未配置 Neon `DATABASE_URL`；因此预览环境的在线生成和 R2 缓存实测仍未完成，正式环境保持 `AUDIO_GENERATION_ENABLED=0`。

`GET /api/audio?word=...` 只能读取已发布词条的词头；例句需加 `senseId`、`usageId`、`exampleId`。接口不能接受任意 TTS 文本。首次生成可能返回 202，浏览器等待后重试；成功音频由 R2 缓存，缓存命中不计入新生成额度。当前 100 个完整词条优先读取仓库内的预生成 MP3。线上 `edge-tts` 依赖外部服务，必须在 Vercel 预览环境完成单词、例句、首次等待、失败重试、并发去重和 R2 命中实测后才启用正式站；若不稳定，保留本地预生成，不自动切换付费 TTS。

音频结果会写入数据库的 `audio_generation_events`；`audio_generation_daily` 和 `audio_generation_failures_daily` 视图分别提供每日失败率与错误原因统计。关闭新增在线生成时，已缓存的 R2 音频仍可播放。

旧 GitHub Pages 工作流暂时保留，且构建使用原仓库子路径。Vercel 正式站完成阅读及音频验证后，再关闭该工作流。当前没有把 `DATABASE_URL` 或 R2 凭据写入仓库。

内容由 Codex 原创制作，自动检查不能替代语义复核。发现词义或例句问题，请在仓库 Issue 标明单词和义项。
