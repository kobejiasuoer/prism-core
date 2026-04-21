# Prism Core

Prism Core 是一个 AI Native 的投研工作流框架。

英文版本： [README.md](README.md)

这个仓库把 Prism 的工作流提炼成一个可以公开、安全展示的 demo 项目，方便别人阅读、运行和扩展，同时不暴露私有生产系统的核心 edge。

## 这个仓库为什么存在

Prism 的开源目标不是把它包装成一个实盘交易系统。

这个仓库主要用来公开 Prism 的工作流形态：

- 一个研究股票池是如何被逐步收窄的
- 多个评分阶段如何组合
- reviewer 如何把评分结果转成决策
- 结构化报告如何生成

目标是把框架层和方法结构讲清楚，同时继续保留生产环境里的 alpha 细节。

## 这个仓库是什么

- 一个公开、安全的 Prism 研究流程 demo 框架
- 一个 `dataset -> scanner -> scorer -> reviewer -> report` 的参考实现
- 一个适合继续扩展 adapter、demo 策略、测试和报告工具的起点

## 这个仓库不是什么

- 它不是投资建议
- 它不是完整的私有生产版 Prism
- 它不是一个实盘交易系统
- 它不会公开私有 prompt、真实阈值和真实运营结果

## 开源边界

这个仓库包含：

- 可公开的方法论文档
- demo 数据
- 教学用途的 demo 策略
- 可运行的 demo pipeline
- 示例报告
- 测试

这个仓库明确不包含：

- 私有 alpha 细节
- 真实阈值和生产权重
- 真实 watchlist 和运营产物
- 生产 prompt
- 私有缓存、日志、快照和 shortlist 规则

更细的规则见 [PUBLIC_VS_PRIVATE.md](PUBLIC_VS_PRIVATE.md)。

## Demo Pipeline

公开版 demo 流程如下：

`stocks.json -> demo_loader -> scorers -> demo_reviewer -> markdown_report`

这里的实现是刻意做简化的。目标不是一比一复刻私有系统，而是把工作流接口和扩展点表达清楚，让别人能在安全边界内继续演化它。

## 快速开始

先创建本地虚拟环境并安装测试依赖：

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pytest
```

运行 demo pipeline：

```bash
python -m scripts.run_demo
```

运行测试：

```bash
pytest -q
```

生成出来的示例报告会写到 `reports/examples/demo-report.md`。

## 示例输出

```markdown
# Prism Demo Report

| Symbol | Momentum | Rebound | Decision |
| --- | ---: | ---: | --- |
| DEMO001 | 74 | 49 | shortlist |
| DEMO002 | 38 | 68 | watchlist |
| DEMO003 | 57 | 44 | watchlist |
```

## 项目结构

```text
prism-core/
├── data/demo/
├── docs/
├── engine/
│   ├── adapters/
│   ├── reports/
│   ├── reviewers/
│   └── scorers/
├── reports/examples/
├── scripts/
└── tests/
```

几个关键入口：

- `engine/pipeline.py`：demo 流程主编排
- `scripts/run_demo.py`：CLI 入口
- `engine/scorers/`：公开教学版策略
- `engine/reviewers/demo_reviewer.py`：确定性的公开 reviewer

## 文档

- [README.md](README.md)
- [docs/methodology/overview.md](docs/methodology/overview.md)
- [docs/architecture/pipeline.md](docs/architecture/pipeline.md)
- [PUBLIC_VS_PRIVATE.md](PUBLIC_VS_PRIVATE.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)

## 贡献方向

欢迎围绕这些方向提交贡献：

- 框架抽象能力
- demo 策略
- adapter 和 fixtures
- 测试改进
- 报告生成能力
- 文档清晰度

提 PR 前，请确认你的改动仍然在 public-safe 边界内，不要把私有运营数据或生产逻辑带进来。

## 免责声明

Prism Core 是一个面向投研工作流的软件框架和 demo 实现，仅用于工程与学习目的，不构成任何投资建议。
