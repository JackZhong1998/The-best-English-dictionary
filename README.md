# 词义之间

面向中文学习者的英汉多义词典第一版。收录 30 个高频多义词，每个义项有双语释义、常见搭配和至少两条例句；单词及例句提供预生成的美式发音。网页是静态站点，可在手机上直接阅读。

## 本地运行

```bash
npm ci
npm run dev
```

打开终端显示的 `/The-best-English-dictionary/` 地址。运行 `npm run build` 会校验 30 个词条、所有音频和 TypeScript，然后生成 `dist/`。

## 内容维护

- `scripts/build_content.py` 是词条源。`HEAD` 写美音音标和按发音拆分的音节，`HISTORY` 写简要词源与词义迁移，`COMPARISONS` 写每个义项的近义词、反义词和易混淆词辨析，`ROWS` 写释义、搭配与例句。修改后运行 `python3 scripts/build_content.py`，生成 `content/words/*.json`。发布数据沿用项目最初约定的 JSON 字段。
- 词源参考 [Online Etymology Dictionary](https://www.etymonline.com/)，词条页可直达对应资料。词义迁移是帮助理解常用义项的学习线索；对 `case`、`light` 等同形不同源的词明确区分。首批词中只有 `matter` 和 `order` 有两个音节，其余为单音节，不强行按字母拆开。
- `node scripts/validate.mjs --content-only` 只检查词条；`npm run check` 还检查全部音频。校验覆盖字段、音节拼回词头、词源与迁移缺项、逐义项辨析、至少两条搭配和例句、重复例句及例句长度。没有自然对应的反义词可留空。语义准确度和表达自然度仍需编辑复查。
- 安装 [edge-tts](https://github.com/rany2/edge-tts) 后运行 `python3 scripts/generate_audio.py`。脚本使用 `en-US-JennyNeural`，跳过已有 MP3；如果改动例句，应先删掉对应音频文件再重跑。文件按 `public/audio/<word>/word.mp3` 和 `s<义项>-u<用法>-e<例句>.mp3` 命名。
- 词条链接格式是 `?word=run`；发布路径配置在 `vite.config.ts` 中。新增词头时还需更新 `scripts/validate.mjs` 的首批词表。

## 发布

`.github/workflows/deploy.yml` 在推送到 `main` 后运行校验、构建并部署到 GitHub Pages。首次发布需要在仓库设置的 **Pages → Build and deployment → Source** 中选择 **GitHub Actions**。站点地址为 `https://jackzhong1998.github.io/The-best-English-dictionary/`。

本项目内容由 Codex 原创生成，面向学习使用。AI 内容可能存在遗漏或不自然表达；发现问题时请在仓库提交 Issue，并标明单词和义项。
