# LeetCode Journey Template

An automated repository template designed to document, organize, and track your LeetCode problem-solving progress with automatic GitHub Actions updates.

---

## Features

- **Automated Statistics & Tables:** A built-in GitHub Actions workflow executes on push to update solution tables and overall progress counts.
- **Multi-Language Support:** Works with C++, Python, Rust, Java, Go, TypeScript, C#, and more.
- **Difficulty Organization:** Dedicated folders for `easy`, `medium`, and `hard` problems, each maintaining its own index table.
- **Starter Templates:** Ready-to-use solution files and local test runners located in `utils/`.
- **AI Coding Guidelines:** Zero-spoiler mentor guidelines included in `AGENT.md`.

---

## Quick Start

### 1. Create your repository
Click the **Use this template** button on GitHub to initialize your personal repository from this template.

### 2. Configure GitHub Actions Permissions
To allow the workflow to commit the updated README tables back to your repository:
1. Open your repository on GitHub.
2. Go to **Settings** > **Actions** > **General**.
3. Under **Workflow permissions**, select **Read and write permissions**.
4. Click **Save**.

### 3. Clone and Customize
Clone your repository locally:
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

Personalize the title, links, and profile information in `README.md`.

### 4. Add your first solution
Copy a starter template from `utils/` to the matching difficulty directory:
```bash
# Example for a Python solution:
cp utils/template.py solutions/easy/0001-two-sum.py

# Example for a C++ solution:
cp utils/template.cpp solutions/easy/0001-two-sum.cpp
```

Make sure the file begins with the required docstring format:
```python
"""
Problem: 1. Two Sum
Time: O(n)
Space: O(n)
"""
```

### 5. Push your code
Push your commits to your default branch:
```bash
git add .
git commit -m "feat: add 0001-two-sum"
git push
```
The GitHub Action will automatically run `update_readme.py` and commit the updated tables and stats.

---

## Progress Tracker

<!-- STATS_START -->
| Difficulty | Solved | View Solutions |
| :---: | :---: | :--- |
| 🟢 **Easy** | 0 | [📁 Browse Easy](./solutions/easy/README.md) |
| 🟡 **Medium** | 0 | [📁 Browse Medium](./solutions/medium/README.md) |
| 🔴 **Hard** | 0 | [📁 Browse Hard](./solutions/hard/README.md) |
| 🏆 **Total** | **0** | |
<!-- STATS_END -->

---

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── update_readme.yml   # Automation pipeline
├── solutions/
│   ├── easy/                   # Easy difficulty solutions
│   ├── medium/                 # Medium difficulty solutions
│   └── hard/                   # Hard difficulty solutions
├── utils/                      # Templates and test runners
├── AGENT.md                    # Zero-spoiler mentor prompt for AI assistants
├── update_readme.py            # Table generation script
└── README.md                   # Main progress dashboard
```

---

## License

This project is open-source and free to use under the MIT License.
