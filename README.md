# Awesome Skills

整理、筛选市面上好用、好玩、值得借鉴的 Agent Skills、技能集合与相关工具。

这里不只收录“能安装的 Skill”，也关注围绕 Skill 形成的工作流、评测基准和完整应用。每个条目尽量说明它适合什么场景、解决什么问题，以及为什么值得研究，避免把仓库变成只有链接的收藏夹。

## 目录

- [Skill 评估](#skill-评估)
- [AI 资讯](#ai-资讯)
- [科研](#科研)
- [编程与 Agent 工作流](#编程与-agent-工作流)
- [办公提效与演示](#办公提效与演示)
- [写作](#写作)
- [图表与可视化](#图表与可视化)
- [设计](#设计)
- [影音创作](#影音创作)
- [如何挑选](#如何挑选)
- [收录标准](#收录标准)

## Skill 评估

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [SkillsBench](https://github.com/FlyAIBox/skillsbench)（[上游](https://github.com/benchflow-ai/skillsbench)） | Benchmark / 评测框架 | 比较有无 Skill 时的任务表现，评估 Agent 是否正确调用、组合 Skill | 仅凭示例或主观体验，很难判断一个 Skill 是否真的提升成功率，也难定位失败来自 Skill 本身还是 Agent 的使用方式 | 使用 gym-style 任务同时评估 Skill 有效性和 Agent 行为；适合 Skill 作者、Agent 开发者和模型评测人员 |
| [awesome-evals](https://github.com/FlyAIBox/awesome-evals)（[上游](https://github.com/benchflow-ai/awesome-evals)） | 精选资源清单 | 搭建 Agent 评测体系，查找论文、实践文章、演讲、工具与基准 | Agent 评估资料分散、术语混杂，初学者难以判断哪些方法可落地 | 条目带注释并覆盖轨迹、工具调用、LLM-as-a-Judge、安全评测等主题；适合需要快速建立评测知识地图的人 |

## AI 资讯

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | AI Native 信息聚合 Skill | 跟踪 AI Builder 在 X 和 YouTube 播客中的新观点，生成可读摘要 | 信息源过多、噪声高，逐个账号和长播客跟进成本大 | 强调“Follow builders, not influencers”，把一手内容重组为 digest；适合 AI 从业者、产品经理和独立开发者 |

## 科研

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [joshzyj/open-scholar-skill](https://github.com/joshzyj/open-scholar-skill/blob/main/README.zh-CN.md) | 学术研究与论文写作 Skills 套件 | 社会科学选题、文献综述、研究设计、数据分析、论文写作、引文核验、投稿与审稿回复 | 学术研究流程长且工具分散，AI 辅助写作又容易产生虚假引文、统计结果与正文不一致等风险 | 提供 34 个模块化能力，覆盖从研究问题到可复现稿件的完整流程；强调人在回路、引文核验、研究伦理和敏感数据保护，适合社会科学研究者 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 综合科研 Agent Skills 库 | 生物、化学、医学、药物研发等领域的数据库检索、分析、实验与科研工作流 | 科研 Agent 需要大量领域知识、专业数据库和专用工具，逐个接入和编写 Skill 成本高 | 原名 `claude-scientific-skills`，包含大量可直接使用的科研 Skills 与科学数据库接口，兼容 Claude Code、Codex、Cursor 等 Agent；这是 K-Dense-AI 维护的第三方项目，并非 Anthropic 官方 Skill |

## 编程与 Agent 工作流

这一类最值得深挖的不是单个提示词，而是如何把澄清需求、规划、实现、测试、调试、审查和交付变成可复用的工程流程。

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 小而可组合的工程 Skills | 需求访谈、领域建模、写规格、拆票、TDD、调试、代码审查、架构改进 | Agent 容易误解需求、跳过反馈环、产出难维护的代码 | 不接管整个开发流程，强调可修改、可组合与工程基本功；很适合拆解后改造成自己的团队规范 |
| [obra/superpowers](https://github.com/obra/superpowers) | 软件开发方法论 + Skills 框架 | 从头脑风暴、计划到分任务实施、测试和审查的完整开发流程 | Agent 直接开写导致需求不清、步骤过大、验证不足 | 把系统化调试、TDD、计划执行和子任务协作固化成纪律；适合希望建立稳定 AI 编程 SOP 的团队 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 多 Agent 编排 / Agent Harness | 在 OpenCode、Codex 等环境中处理大型或复杂代码库 | 单 Agent 容易上下文过载，研究、实现和验证缺少专业分工 | 原 `oh-my-opencode`，现更名为 `oh-my-openagent`；偏向多模型、多 Agent 编排，适合重度 Agent 用户 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 角色化开发工作流 | 用一套命令覆盖产品、设计、工程管理、发布、文档和 QA | 只让 Agent 扮演程序员，容易遗漏产品判断、交互检查和发布准备 | 将 CEO、Designer、Eng Manager、Release Manager、Doc Engineer、QA 等角色沉淀为一组强观点工具；适合创业团队和全栈开发者 |
| [code-yeongyu/lazycodex](https://github.com/code-yeongyu/lazycodex) | Codex Agent Harness | 在复杂代码库中进行长期任务、规划执行和完成验证 | 会话间知识丢失、计划与执行脱节、Agent 过早宣布完成 | 围绕项目记忆、规划、执行与 verified completion 设计；适合 Codex 用户研究持久上下文和闭环交付 |

## 办公提效与演示

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | 中文知识工作 Skills 集 | 内容卡片、论文阅读、拆书、概念学习、写作、演讲稿与旅行研究 | 阅读、理解和表达任务缺少稳定的结构化方法，结果难复用 | 不只是 PPT，覆盖“理解 → 提炼 → 表达 → 视觉化”链路；适合中文知识工作者和内容创作者 |
| [FlyAIBox/baoyu-skills](https://github.com/FlyAIBox/baoyu-skills) | 内容创作与演示 Skills 集 | 生成幻灯片、信息图、封面图、社媒卡片、漫画和文章配图 | 通用 Agent 能写内容，但缺少视觉风格、版式流程和可交付资产 | 覆盖从内容到视觉成品的多种工作流；适合运营、市场、自媒体和需要快速做演示的人 |

## 写作

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [liangdabiao/liurun-bookwriter-skills](https://github.com/liangdabiao/liurun-bookwriter-skills) | 商业长文写作 Skill | 商业评论、公众号长文、观点型文章和案例分析 | AI 长文容易平铺直叙、缺乏逻辑势能、洞察与读者节奏 | 从刘润商业写作方法中提炼结构、SCQA、案例与 callout 模板；适合商业内容作者，使用时仍需自行核实事实并避免机械模仿个人文风 |

## 图表与可视化

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [FlyAIBox/lanshu-animated-architecture-diagram](https://github.com/FlyAIBox/lanshu-animated-architecture-diagram) | 架构图生成 Skill | 技术方案讲解、系统架构展示、路演和文档配图 | 静态架构图信息层级弱，复杂数据流和组件关系难讲清楚 | 生成手绘感、带动画的架构图，强调叙事和视觉表现；适合架构师、售前、开发者和技术内容作者 |

## 设计

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Design Engineering Skills | UI 动效、交互细节、视觉打磨与前端设计实现 | Agent 生成的界面常常“功能正确但质感不足”，缺少动效原则和设计判断 | 来自 Design Engineer 的可复用设计经验；适合前端工程师、独立开发者和设计工程师 |
| [jimliu/baoyu-design](https://github.com/jimliu/baoyu-design) | 本地设计 Agent Skill | 在 Cursor、Claude Code 等环境生成 UI mockup、原型、演示和线框图 | 设计生成往往依赖特定在线产品，难接入本地 Agent 工作流，也不便继续修改 | 输出自包含 HTML，便于预览、迭代和交付；适合需要快速探索多个界面方向的产品与开发团队 |

## 影音创作

| 项目 | 类型 | 使用场景 | 解决的问题 | 亮点 / 适合谁 |
| --- | --- | --- | --- | --- |
| [jimliu/baocut](https://github.com/jimliu/baocut) | macOS 视频处理 App + Agent Skill | 转写、字幕、翻译和基于文本的粗剪 | 口播和访谈视频的机械剪辑步骤多，人工找句子、做字幕耗时 | Agent 通过 BaoCut CLI 驱动本地应用完成转写到剪辑；适合播客、访谈、课程和短视频创作者，主要面向 macOS |
| [browser-use/video-use](https://github.com/browser-use/video-use) | Coding Agent 视频编辑工具 | 用自然语言和代码 Agent 编辑、组合视频 | 传统时间线编辑器学习成本高，自动化和批量修改困难 | 把视频工程暴露给 coding agent，便于通过指令迭代；适合开发者型创作者和程序化视频工作流 |

## 如何挑选

| 你的目标 | 建议先看 |
| --- | --- |
| 评估一个 Skill 到底有没有用 | SkillsBench |
| 从零建立 Agent 评测知识体系 | awesome-evals |
| 做社会科学研究与论文投稿 | open-scholar-skill |
| 搭建生物、化学、医学和药物研发 Agent | scientific-agent-skills |
| 改善日常 AI 编程质量 | mattpocock/skills、superpowers |
| 研究复杂项目的多 Agent 编排 | oh-my-openagent、lazycodex |
| 给创业团队搭建端到端交付流程 | gstack |
| 阅读、提炼、写作和内容视觉化 | ljg-skills、baoyu-skills |
| 做商业长文 | liurun-bookwriter-skills |
| 做架构讲解和动态图表 | lanshu-animated-architecture-diagram |
| 提升 UI 与交互质感 | emilkowalski/skills、baoyu-design |
| 用 Agent 做字幕、粗剪和程序化视频 | baocut、video-use |

## 收录标准

优先收录满足以下一项或多项的项目：

- 有清晰、真实的使用场景，而不只是提示词合集；
- 把专业方法、工具链或团队流程沉淀成可复用能力；
- 提供脚本、模板、示例或评测，能够验证实际效果；
- 具有值得学习的 Skill 设计、上下文管理或 Agent 编排方式；
- 仍在维护，文档基本完整，来源和许可清晰。

提交新条目时，建议同时说明：项目类型、适用场景、解决的问题、核心亮点、运行环境、依赖与限制。涉及执行脚本、浏览器控制或第三方凭证的 Skill，请先审查源码，并在隔离环境中试用。

## License

本仓库仅整理和介绍第三方项目；各项目的代码、文档和商标归其原作者所有，请以对应仓库的许可证为准。
