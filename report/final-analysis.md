# Skill 迭代分析与提交审核

## 资料与范围

依据现存的 13 份 Markdown 作业、`教学进程.pdf` 和 `AI_Skill_迭代开发.pdf`，整理 v1–v13。原有 v1–v10 的内容从本机旧 Skill 复制，v11–v13 根据第 10–12 周作业补写。本人确认手写作业存于桌面 `linux作业` 文件夹，并说明保留各轮 AI 原稿。

## 七轮核心变化曲线

| 轮次 | 可观察的 Skill 变化 | 对应评分关注点 |
| --- | --- | --- |
| v1→v2 | 从 Markdown 结构和学习反思扩展到命令前置条件、证据及排错 | 抽象实践经验 |
| v2→v3 | 把源码、架构、寄存器与栈的推导纳入写作检查 | 反馈具体化 |
| v3→v4 | 重写机制分析，区分时钟中断提出请求与任务实际切换 | 教材概念边界 |
| v4→v5 | 增加 QEMU 客体、镜像、符号文件与 GDB 断点核对 | 自我检查 |
| v5→v6 | 区分 API、ABI、实际入口及错误返回转换 | 复杂调用路径 |
| v6→v7 | 核对入口现场、服务函数返回、退出检查和 `iret` | 稳定性与证据 |
| v7→v8 | 区分进程创建、首次运行与父子两条返回路径 | 泛化到新任务 |

v8 与 v1 相比，Skill 从基本 Markdown 排版发展为围绕环境、源码、运行现场和证据边界的实验写作方法。v9–v13 又覆盖 ELF/exec、调度、虚拟化与容器、安全机制和受控安全实验。其中 v10 修改了旧规则，不只是继续追加：把调度原因、请求、允许上下文和切换分开；v13 加入教学进程中的标题、教材/视频及 Markdown/PDF 交付检查。

## 从 Git 仓库导出的关键节点

下表依据仓库中的提交和标签整理。提交链接可查看当时归档的文件与改动；例如在仓库目录运行 `git for-each-ref --sort=version:refname --format='%(refname:short) %(*objectname:short) %(*subject)' refs/tags`，可核对各标签指向的提交。

| 阶段 | 标签与提交 | 对应文件或迭代变化 |
| --- | --- | --- |
| 环境准备 | [提交 `4a3488d`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/4a3488d) | 建立仓库目录与项目说明。 |
| 第一次作业 | `phase1-handmade` · [提交 `594aede`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/594aede) | 归档 `handmade/homework1.md` 和 `reflection.md`。 |
| 初版 Skill | `skill-v1` · [提交 `2c9872b`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/2c9872b) | 建立 Markdown 作业的结构、示例和反思规则。 |
| 第 1 次迭代 | `skill-v2` · [提交 `6ef71dc`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/6ef71dc) | 加入命令实践的前置条件、证据和排错记录。 |
| 第 2 次迭代 | `skill-v3` · [提交 `7978057`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/7978057) | 加入源码、汇编、寄存器和栈的分析检查。 |
| 第 3 次迭代 | `skill-v4` · [提交 `8104504`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/8104504) | 修改调度表述，区分中断提出请求与任务切换。 |
| 第 4 次迭代 | `skill-v5` · [提交 `9130056`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/9130056) | 增加 QEMU、GDB、镜像和符号文件的核对。 |
| 第 5 次迭代 | `skill-v6` · [提交 `6233c71`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/6233c71) | 区分 API、ABI、系统调用入口与错误返回。 |
| 第 6 次迭代 | `skill-v7` · [提交 `7284bdf`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/7284bdf) | 加入系统调用入口、退出检查和返回现场。 |
| 第 7 次迭代 | `skill-v8` · [提交 `017427b`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/017427b) | 扩展到进程创建与父子两条执行路径。 |
| 后续扩展 | `skill-v13` · [提交 `bb107f8`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/bb107f8) | 归档至第 12 周作业对应版本。 |
| 总结报告 | `final-report` · [提交 `07e2e58`](https://github.com/lingQ738/linux-homework-skill-iteration/commit/07e2e58) | 归档报告初稿；[仓库主分支中的报告](https://github.com/lingQ738/linux-homework-skill-iteration/blob/master/report/final-analysis.md)包含后续修改。 |

上述标签与提交均在 2026 年 11 月 17 日建立，记录的是本次归档与版本整理，不能据此推断各周作业当时的 Git 提交时间。

## 个人收获

这门课给我的收获，不只是学会了 Linux 命令、系统调用和内核调试，还包括学会把完成作业时反复用到的方法写成 Skill。最初我主要关注 Markdown 的标题、代码块和示例能否写清楚；随着作业深入，我发现写出一份可信的实验报告，还要核对环境、源码版本、运行结果和截图，分清实际观察与根据原理作出的推断。把这些检查方法写进 Skill 后，它们就成了下一次作业可以复用的写作步骤。

迭代过程中，我也逐渐理解 Skill 不能靠不断堆积要求来改进。有些旧规则需要根据新作业修正，例如分析调度时，不能把“时钟中断提出调度请求”直接写成“已经完成进程切换”；分析系统调用时，也要区分库函数接口、系统调用约定和内核中的真实执行路径。每遇到一种新的问题，我需要先找出原有规则为什么不够准确，再决定是补充适用条件，还是改写原来的表述。这让我开始从“让 AI 帮我写一次作业”，转向“教 AI 按可核查的方法完成一类作业”。

完成这轮整理后，我已经能够编写具有明确用途、版本和检查规则的 Skill，也知道要用作业中的具体问题推动下一版优化。以后学习其他技术内容时，我希望继续采用这种方式：先自己弄清任务和证据，再把有效的方法整理成可复用的 Skill，并在实际使用后审阅、修改。对我来说，学会写 Skill 的价值，是把一次作业中得到的经验保留下来，让后续学习有可以持续改进的方法。
