import shutil
import subprocess
from pathlib import Path

root = Path(__file__).parent

# 1. Rendu du site français (vide et recrée _site/)
subprocess.run(["quarto", "render"], cwd=root, check=True)

# 2. Rendu du site anglais (produit en/_site/)
subprocess.run(["quarto", "render", "en"], cwd=root, check=True)

# 3. Copie de la version anglaise dans _site/en
dest = root / "_site" / "en"
shutil.rmtree(dest, ignore_errors=True)
shutil.copytree(root / "en" / "_site", dest)

# 4. Publication sur GitHub Pages sans relancer le rendu
subprocess.run(["quarto", "publish", "gh-pages", "--no-render"], cwd=root, check=True)
