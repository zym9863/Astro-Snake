"""使用项目根目录下的icon.png生成PWA所需的多尺寸图标。"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - 仅在运行时提示
    raise SystemExit(
        "未检测到Pillow库，请运行 `pip install Pillow` 后重试。"
    ) from exc

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_ICON = BASE_DIR / "icon.png"
OUTPUT_DIR = BASE_DIR / "public" / "icons"
ICON_SPECS: Tuple[Tuple[int, int], ...] = (
    (192, 192),
    (512, 512),
)


def ensure_output_dir() -> None:
    """确保图标输出目录存在。"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_source_icon() -> Image.Image:
    """加载源图标文件并返回 Image 对象。"""
    if not SOURCE_ICON.exists():
        raise FileNotFoundError(f"未找到源图标: {SOURCE_ICON}")
    return Image.open(SOURCE_ICON).convert("RGBA")


def resize_and_save(base_image: Image.Image, suffix: str, size: Tuple[int, int]) -> None:
    """按指定尺寸缩放源图标并保存为PNG文件。"""
    target_path = OUTPUT_DIR / f"{suffix}-{size[0]}x{size[1]}.png"
    resized = base_image.resize(size, Image.Resampling.LANCZOS)
    resized.save(target_path, format="PNG")
    print(f"生成图标: {target_path}")


def generate_variants(base_image: Image.Image, specs: Iterable[Tuple[int, int]]) -> None:
    """依据给定尺寸集合生成常规与可遮罩图标。"""
    for width, height in specs:
        resize_and_save(base_image, "icon", (width, height))
        resize_and_save(base_image, "maskable-icon", (width, height))


def main() -> None:
    """脚本入口：生成PWA所需的所有PNG图标文件。"""
    ensure_output_dir()
    with load_source_icon() as image:
        generate_variants(image, ICON_SPECS)
    print("所有图标生成完成。")


if __name__ == "__main__":
    main()
