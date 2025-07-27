# 贪吃蛇游戏 (Astro Snake Game)

**Language / 语言**: [中文](README.md) | [English](README_EN.md)

一个使用 Astro 框架开发的经典贪吃蛇游戏，具有现代化的界面设计和完整的游戏功能。

## 🎮 游戏特性

- 🐍 经典贪吃蛇游戏玩法
- 🎯 实时分数统计和最高分记录
- ⏸️ 暂停/继续功能
- 🎨 响应式设计，支持移动设备
- 🎪 精美的渐变背景和动画效果
- 💾 本地存储最高分记录
- ⌨️ 键盘控制 (方向键 + 空格键)

## 🚀 项目结构

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   ├── astro.svg
│   │   └── background.svg
│   ├── components/
│   │   ├── SnakeGame.astro    # 贪吃蛇游戏主组件
│   │   └── Welcome.astro      # 欢迎组件
│   ├── layouts/
│   │   └── Layout.astro       # 页面布局
│   └── pages/
│       └── index.astro        # 首页
└── package.json
```

## 🎯 游戏说明

- 使用方向键 `↑` `↓` `←` `→` 控制蛇的移动方向
- 按 `空格键` 开始游戏、暂停或重新开始
- 吃到红色食物可以增长蛇身并获得 10 分
- 避免撞墙或撞到自己的身体
- 游戏会自动保存你的最高分记录

## 🧞 开发命令

所有命令都需要在项目根目录的终端中运行：

| 命令                       | 说明                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`            | 安装依赖                                        |
| `pnpm dev`               | 启动本地开发服务器 `localhost:4321`              |
| `pnpm build`             | 构建生产版本到 `./dist/` 目录                     |
| `pnpm preview`           | 本地预览构建结果                                 |
| `pnpm astro ...`         | 运行 Astro CLI 命令，如 `astro add`, `astro check` |
| `pnpm astro -- --help`   | 获取 Astro CLI 帮助信息                          |

## 🛠️ 技术栈

- **框架**: [Astro](https://astro.build) - 现代化的静态站点生成器
- **样式**: CSS3 with Flexbox & Grid
- **游戏逻辑**: 原生 JavaScript (Canvas API)
- **存储**: LocalStorage (用于保存最高分)

## 📱 兼容性

- 支持现代浏览器 (Chrome, Firefox, Safari, Edge)
- 响应式设计，适配桌面和移动设备
- 键盘控制优化，适合桌面游戏体验

## 🎯 快速开始

1. 克隆项目
```bash
git clone https://github.com/zym9863/Astro-Snake.git
cd Astro-Snake
```

2. 安装依赖
```bash
pnpm install
```

3. 启动开发服务器
```bash
pnpm dev
```

4. 打开浏览器访问 `http://localhost:4321`

## 📄 许可证

本项目仅供学习和娱乐使用。

---

🎮 **准备好挑战自己的反应速度了吗？开始游戏吧！**