# Linux 预习作业 Skill 迭代归档

本目录按老师《AI_Skill_迭代开发.pdf》的结构整理。`skill/v1` 至 `skill/v13` 对应现有的 13 份作业：前两份为 Markdown 与命令练习，随后对应《Linux内核原理与分析》第 2 至 12 周。

## 目录与使用

- `handmade/`：第一次作业及待本人核对的手写反思。
- `skill/vN/skill.md`：第 N 版 Skill；`changelog.md` 说明本版变化。每版都保留 Codex 所需的 `name`、`description` 文件头。实际安装到 Codex 时，将选定版本复制为 `~/.codex/skills/linux-homework-md-vN/SKILL.md`。
- `output/vN/source-homework.md`：项目中现存作业的原样副本。`generated.md` 为各轮对应文件；`human-edited.md` 已由本人确认审阅，方括号保留审阅建议。
- `feedback/`：依据现存作业重建的改进线索，并非当时的原始对话反馈。
- `report/`：迭代分析和符合性审核。
- `source-skills-backup/`：从原 Codex skills 目录迁出的 v1–v10 原件，仅供本地核对，已排除在 Git 提交之外。

运行 `python build_archive.py` 可从桌面 `linux作业` 原文件重新生成版本目录。运行会覆盖本项目中的版本稿、反馈和审阅稿；现已完成审阅，请不要再运行它。课程提交前请核对手写来源、实验记录，并补充真实的远程仓库链接。

本项目实际迭代时间为每周作业完成之后。教学进程规定周作业使用“学号《Linux内核原理与分析》第X周作业”标题，重点记录问题及解决方案，并同时交 Markdown 与 PDF；作业原稿与待审阅稿仍需按此核对。
