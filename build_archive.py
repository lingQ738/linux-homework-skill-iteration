from pathlib import Path
import re
import shutil

HOME = Path(r"C:\Users\ACER")
PROJECT = HOME / "Desktop" / "预习作业-skill迭代"
SOURCE = HOME / "Desktop" / "linux作业"
SKILLS = HOME / ".codex" / "skills"

first = SOURCE / "Linux作业1-20262803李令琪.md"
second = SOURCE / "20262803-李令琪-Linux命令实践2.md"
homeworks = [first, second]
for week in range(2, 13):
    candidates = list(SOURCE.rglob(f"*第{week}周作业.md"))
    if week == 12:
        candidates = list((SOURCE / f"20262803《Linux内核原理与分析》第{week}周作业").glob("*.md"))
    if len(candidates) != 1:
        raise RuntimeError(f"第 {week} 周作业数量为 {len(candidates)}")
    homeworks.append(candidates[0])
assert len(homeworks) == 13

deltas = {
    1: "从 Markdown 基础作业提炼标题、代码块、示例和学习反思写法。",
    2: "命令实践增加前置条件、运行证据、截图路径和故障处理。",
    3: "源码与汇编分析增加环境、寄存器、栈和推导核验。",
    4: "重写机制分析，区分调度请求、实际切换和日志证据。",
    5: "启动调试增加宿主/客体、镜像/符号和断点证据链。",
    6: "系统调用对照增加 API、ABI、实际入口和错误转换。",
    7: "增加入口现场、返回路径和 GDB 观察边界。",
    8: "增加进程创建阶段、首次运行及父子返回路径。",
    9: "增加 ELF、链接方式与 exec 装载路径。",
    10: "修订调度分析，区分调度时机、允许上下文和实际切换。",
    11: "教材阅读型作业增加概念层次比较与未实践内容标注。",
    12: "安全章节增加主体、对象、操作、策略与防护边界分析。",
    13: "安全实验增加受控样本、成功判据、异常分支及口令处理。",
}

skill10 = (SKILLS / "linux-homework-md-v10" / "SKILL.md").read_text(encoding="utf-8")
additions = {
    11: "\n## 教材阅读与概念对照\n\n- 阅读型作业写明实际阅读的章节、课程视频和参考资料；把教材结论、官方资料、个人理解及计划中的验证分开。未运行的命令只作为验证方案。\n- 比较虚拟机、容器等概念时，先明确隔离边界、共享的内核或硬件、资源控制位置和适用条件；不要由使用 QEMU 推断一定启用了 KVM。\n",
    12: "\n## 安全机制分析\n\n- 先说明保护目标，再写主体、对象、操作、凭据和适用策略；文件内容权限与父目录中的删除权限应分别分析。\n- 区分 DAC、Capabilities、seccomp、LSM、namespace、cgroup 与 TEE 的作用边界；不能由部署某一机制就断言系统整体安全。有关硬件和软件依赖的实践未完成时只写待验证方案。\n",
    13: "\n## 受控安全实验\n\n- 密码测试、恢复或类似安全实验只使用本人创建或获授权的本地样本，交代样本、字典和运行范围，不把示例口令写成真实账户凭据。\n- 程序实验给出可复现输入、执行命令、成功判据与失败记录；验证结果应核对实际解出的内容，不能仅以未抛异常判断成功。区分密码错误、文件不存在、格式不支持等异常，保留必要的诊断信息。\n\n## 课程交付检查\n\n- 对照教学进程核查当周教材、已指定的视频和实验；第 10、11 周没有单列新视频时不要编造已观看记录。作业说明实际遇到的问题、解决过程及仍待验证的部分。\n- 按课程要求使用“学号《Linux内核原理与分析》第X周作业”作为周作业标题，并同时交付 Markdown 与转换后的 PDF；实验专题标题可保留为副标题。\n",
}

def prep(path):
    path.mkdir(parents=True, exist_ok=True)
    return path

def copy_assets(text, source_file, output_dir):
    refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)|<img\s+[^>]*src=[\"']([^\"']+)", text, re.I | re.S)
    for md_ref, html_ref in refs:
        ref = (md_ref or html_ref).strip()
        if ref.startswith(("http:", "https:")):
            continue
        asset = Path(ref)
        if asset.is_absolute():
            continue
        full = (source_file.parent / asset).resolve()
        if full.is_file() and full.is_relative_to(SOURCE):
            destination = output_dir / asset
            prep(destination.parent)
            shutil.copy2(full, destination)

for n, source_file in enumerate(homeworks, 1):
    skill_dir = prep(PROJECT / "skill" / f"v{n}")
    if n <= 10:
        content = (SKILLS / f"linux-homework-md-v{n}" / "SKILL.md").read_text(encoding="utf-8")
    else:
        content = skill10.replace("linux-homework-md-v10", f"linux-homework-md-v{n}")
        content = re.sub(r"description:.*\n", f"description: 根据前{n}次 Linux 作业整理的中文 Markdown 写作方法，涵盖本轮课程主题；用户指定 v{n} 时使用。\n", content, count=1)
        for k in range(11, n + 1):
            content += additions[k]
    (skill_dir / "skill.md").write_text(content, encoding="utf-8")
    (skill_dir / "changelog.md").write_text(
        f"# v{n} 设计记录\n\n- 对应现有作业：`{source_file.relative_to(SOURCE)}`。\n- 可复用变化：{deltas[n]}\n- 本目录为依据现存文件在 2026-11-17 重建的归档，不代表当时的原始开发记录。\n",
        encoding="utf-8",
    )

    out = prep(PROJECT / "output" / f"v{n}")
    original = source_file.read_text(encoding="utf-8")
    (out / "source-homework.md").write_text(original, encoding="utf-8")
    (out / "generated.md").write_text(
        "> **事后重建的原稿代理：**未保留本轮真实 AI 原稿。以下复制现存作业以便核对内容，不能作为当时未修改的 AI 输出证据。\n\n"
        + original,
        encoding="utf-8",
    )
    copy_assets(original, source_file, out)

    review = (
        "> **待本人审阅稿：**由 AI 根据现有作业整理，尚未经学生本人确认。"
        "下列方括号是待核对事项，不能视为已经完成的人工批注。\n\n"
        f"> [待人工核对：本轮 `{source_file.name}` 是否为真实提交稿；补充你实际修改的理由和过程。]\n\n"
    )
    edited = original
    if n >= 3:
        week = n - 1
        expected = f"20262803《Linux内核原理与分析》第{week}周作业"
        first_line = edited.splitlines()[0]
        if first_line != f"# {expected}":
            edited = edited.replace(first_line, f"# {expected}\n\n## 原作业主题：{first_line.lstrip('# ').strip()}", 1)
            review += "> [AI 建议：按教学进程统一作业主标题；原主题保留为副标题，请人工确认提交命名。]\n\n"
    if n == 2:
        review += "> [AI 修改：将原文 Typora 本机截图复制到本目录并改为相对路径；请人工核对截图与正文是否对应。]\n\n"
        image_dir = prep(out / "images")
        for absolute in set(re.findall(r"!\[[^\]]*\]\((C:[^)]+\.png)\)", edited)):
            image = Path(absolute)
            if image.is_file():
                shutil.copy2(image, image_dir / image.name)
                edited = edited.replace(absolute, f"images/{image.name}")
    if n == 13:
        review += "> [AI 建议：原代码使用 `except Exception` 捕获全部错误，需人工核对是否把文件缺失或格式错误误判为密码错误。]\n\n"
    (out / "human-edited.md").write_text(review + edited, encoding="utf-8")

    if n > 1:
        feedback = prep(PROJECT / "feedback") / f"v{n-1}-to-v{n}.md"
        feedback.write_text(
            f"# v{n-1} → v{n} 反馈重建\n\n- 新作业：`{source_file.relative_to(SOURCE)}`。\n- 据作业可提出的改进：{deltas[n]}\n- 这是事后归纳，非当时提交给 AI 的原始反馈；请用真实记录补充或替换。\n",
            encoding="utf-8",
        )

prep(PROJECT / "handmade")
shutil.copy2(first, PROJECT / "handmade" / "homework1.md")
(PROJECT / "handmade" / "reflection.md").write_text(
    "# 手写反思：待本人核对的提纲\n\n> 本文件由 AI 根据第一次作业归纳，不能代替本人对真实写作过程的回忆。请核对后改写成自己的亲历记录。\n\n"
    "- 第一次作业中列出的未系统掌握内容：LaTeX 公式、Mermaid、Marp、Pandoc 与结构化 Prompt。哪些是在手写时真正卡住的？请补具体位置和处理过程。\n"
    "- 当时希望 AI 怎样帮：请按真实经历写出希望获得的解释、示例、排版或检查支持，避免把后来的 skill 功能倒写成当时想法。\n"
    "- 与 skill v1 的对照：v1 重点写了层级、代码块和学习反思。请说明哪些确实来自手写经验，哪些是后来补充。\n"
    "- 第一次作业正文出现“AI 返回内容的学习”字样；请核对这是否符合老师对 Phase 1 完全手写、禁止 AI 辅助的要求。\n",
    encoding="utf-8",
)
print(f"created {len(homeworks)} version folders in {PROJECT}")
