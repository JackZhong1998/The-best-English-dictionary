# 四六级词头来源

本目录的 `cet2016-word-list.txt` 取自 [JavaProgrammerLB/cet-word-list](https://github.com/JavaProgrammerLB/cet-word-list) 的提交 `fe6a0a0429d8b8b84eb92aaee7f1c0020138d3c0`。该第三方仓库声明按 MIT License 发布，许可全文保存在 `cet2016-word-list-LICENSE`；这一声明不能证明其所依据的官方大纲也允许再利用。原仓库说明该列表由《全国大学英语四、六级考试大纲（2016 年修订版）》的词表图片识别整理；考试大纲仍列在[中国教育考试网](https://cet.neea.edu.cn/xhtml1/folder/16113/1588-1.htm)。这是第三方转录稿，不是考试机构直接发布的机器可读词表。

这里只用英语词头作选词范围，不复制第三方中文释义或例句。每个词条的中文释义、用法、例句和辨析由本项目另行撰写。原稿存在 OCR、词族合写、英美拼写及同形异义编号，解析脚本把可确定的独立拼写列入 `cet2016_simple.tsv`，紧缩变体记法写入 `cet2016_unresolved.tsv` 待人工核对。`scripts/expand_cet_variants.py` 为这些记法生成 `cet2016_variant_candidates.tsv` 复核队列，队列中的词形均未自动纳入词头索引；缩写、同形异义编号和可疑拼写仍要逐条确认。大写词头以及大小写可能区分词义的写法另列 `cet2016_case_review.tsv`，不能因索引统一小写就视为已经处理。原稿没有可靠的逐词四级／六级标签，核定前统一记为“四／六级大纲候选”，不冒称单独的四级或六级官方词表。
