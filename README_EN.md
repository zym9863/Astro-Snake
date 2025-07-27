# Snake Game (Astro Snake Game)

**Language / 语言**: [中文](README.md) | [English](README_EN.md)

A classic Snake game developed with Astro framework, featuring modern UI design and complete game functionality.

## 🎮 Game Features

- 🐍 Classic Snake game mechanics
- 🎯 Real-time score tracking and high score records
- ⏸️ Pause/Resume functionality
- 🎨 Responsive design, mobile device support
- 🎪 Beautiful gradient backgrounds and animations
- 💾 Local storage for high score records
- ⌨️ Keyboard controls (Arrow keys + Spacebar)

## 🚀 Project Structure

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   ├── astro.svg
│   │   └── background.svg
│   ├── components/
│   │   ├── SnakeGame.astro    # Main Snake game component
│   │   └── Welcome.astro      # Welcome component
│   ├── layouts/
│   │   └── Layout.astro       # Page layout
│   └── pages/
│       └── index.astro        # Homepage
└── package.json
```

## 🎯 Game Instructions

- Use arrow keys `↑` `↓` `←` `→` to control snake movement
- Press `Spacebar` to start game, pause, or restart
- Eat red food to grow the snake and earn 10 points
- Avoid hitting walls or your own body
- The game automatically saves your high score record

## 🧞 Development Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`            | Install dependencies                             |
| `pnpm dev`               | Start local dev server at `localhost:4321`      |
| `pnpm build`             | Build your production site to `./dist/`          |
| `pnpm preview`           | Preview your build locally, before deploying     |
| `pnpm astro ...`         | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help`   | Get help using the Astro CLI                     |

## 🛠️ Tech Stack

- **Framework**: [Astro](https://astro.build) - Modern static site generator
- **Styling**: CSS3 with Flexbox & Grid
- **Game Logic**: Vanilla JavaScript (Canvas API)
- **Storage**: LocalStorage (for saving high scores)

## 📱 Compatibility

- Supports modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design, compatible with desktop and mobile devices
- Keyboard control optimization, suitable for desktop gaming experience

## 🎯 Quick Start

1. Clone the project
```bash
git clone https://github.com/zym9863/Astro-Snake.git
cd Astro-Snake
```

2. Install dependencies
```bash
pnpm install
```

3. Start development server
```bash
pnpm dev
```

4. Open browser and visit `http://localhost:4321`

## 📄 License

This project is for learning and entertainment purposes only.

---

🎮 **Ready to challenge your reaction speed? Start the game!**