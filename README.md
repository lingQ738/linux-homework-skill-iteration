# Linux 预习作业 Skill 迭代归档

本目录按老师《AI_Skill_迭代开发.pdf》的结构整理。`skill/v1` 至 `skill/v13` 对应现有的 13 份作业：前两份为 Markdown 与命令练习，随后对应《Linux内核原理与分析》第 2 至 12 周。

## 目录与使用

- `handmade/`：第一次作业及待本人核对的手写反思。
- `skill/vN/skill.md`：第 N 版 Skill；`changelog.md` 说明本版变化。每版都保留 Codex 所需的 `name`、`description` 文件头。实际安装到 Codex 时，将选定版本复制为 `~/.codex/skills/linux-homework-md-vN/SKILL.md`。
- `output/vN/source-homework.md`：项目中现存作业的原样副本。`generated.md` 是标明来源的**事后代理稿**，因为当时的 AI 原稿没有保存；`human-edited.md` 是 AI 准备的待本人审阅稿，方括号保留待核对事项。不要把它们写成当时的真实 AI 输出或已完成的人工审阅。
- `feedback/`：依据现存作业重建的改进线索，并非当时的原始对话反馈。
- `report/`：迭代分析和符合性审核。

运行 `python build_archive.py` 可从桌面 `linux作业` 原文件重新生成版本目录。运行会覆盖本项目中的版本稿、反馈和待审阅稿；本人审阅或补充历史材料后，请不要再运行它。课程提交前请本人确认手写来源、实际修改和实验记录，并补充真实的远程仓库链接。

本项目在 2026-11-17 事后整理；Git 提交和标签记录整理过程，不代表历史上的实际迭代时间。教学进程规定周作业使用“学号《Linux内核原理与分析》第X周作业”标题，重点记录问题及解决方案，并同时交 Markdown 与 PDF；作业原稿与待审阅稿仍需按此核对。
