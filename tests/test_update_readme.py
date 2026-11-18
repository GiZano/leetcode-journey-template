import pytest

import update_readme


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("O(n) // C++ comment", "O(n)"),
        ("O(1) # Python comment", "O(1)"),
        ("O(n log n) */", "O(n log n)"),
        ("  O(k)***  ", "O(k)"),
        ("  O(m)  ", "O(m)"),
        ("", "N/A"),
        ("   ", "N/A"),
        (None, "N/A"),
    ],
)
def test_clean_complexity(value, expected):
    assert update_readme.clean_complexity(value) == expected


@pytest.fixture
def problems(tmp_path, monkeypatch):
    fixtures = {
        "easy/0042-second.py": '"""Problem: 42. Second fixture\nTime: O(n)\nSpace: O(1)\n"""',
        "easy/0008-first.py": '"""Problem: 8. First fixture\nTime: O(1)\nSpace: O(n)\n"""',
        "easy/0008-first.cpp": "/* Problem: 8. First fixture */\n",
        "easy/9999-ignore.txt": "Problem: 9999. Unsupported file\n",
        "medium/0016-another.py": '"""Problem: 16. Another fixture\n"""',
    }
    for relative, content in fixtures.items():
        path = tmp_path / "solutions" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    return update_readme.parse_problems()


def test_parse_problems_groups_and_sorts_supported_files(problems):
    assert [problem["num"] for problem in problems["easy"]] == [8, 42]
    assert [problem["num"] for problem in problems["medium"]] == [16]
    assert problems["hard"] == []
    first = problems["easy"][0]
    assert (first["title"], first["t_comp"], first["s_comp"]) == ("First fixture", "O(1)", "O(n)")
    assert [(solution["name"], solution["link"]) for solution in first["solutions"]] == [
        ("C++", "./0008-first.cpp"),
        ("Python", "./0008-first.py"),
    ]


def test_parse_problems_handles_an_empty_checkout(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert update_readme.parse_problems() == {"easy": [], "medium": [], "hard": []}


def test_parse_problems_skips_an_unreadable_source(tmp_path, monkeypatch, capsys):
    source = tmp_path / "solutions" / "easy" / "0008-fixture.py"
    source.parent.mkdir(parents=True)
    source.write_bytes(b"\xff")
    monkeypatch.chdir(tmp_path)

    assert update_readme.parse_problems() == {"easy": [], "medium": [], "hard": []}
    assert "Error reading" in capsys.readouterr().out


def test_generate_tables_formats_problem_links_and_empty_categories(problems):
    tables = update_readme.generate_tables(problems)
    rows = tables["easy"].splitlines()
    assert rows[0] == "| # | Title | Complexity (Time / Space) | Solutions |"
    assert rows[2] == (
        "| 8 | **First fixture** | O(1) / O(n) | "
        "[⚙️ C++](./0008-first.cpp) · [🐍 Python](./0008-first.py) |"
    )
    assert rows[3].startswith("| 42 | **Second fixture** | O(n) / O(1) |")
    assert tables["hard"] == "*No problem solved in this category yet.*"


def test_generate_stats_counts_problems_before_language_variants(problems):
    rows = update_readme.generate_stats(problems).splitlines()
    assert "| 🟢 **Easy** | 2 | [📁 Browse Easy](./solutions/easy/README.md) |" in rows
    assert "| 🟡 **Medium** | 1 | [📁 Browse Medium](./solutions/medium/README.md) |" in rows
    assert "| 🔴 **Hard** | 0 | [📁 Browse Hard](./solutions/hard/README.md) |" in rows
    assert rows[-1] == "| 🏆 **Total** | **3** | |"


def test_update_file_replaces_only_between_markers(tmp_path):
    path = tmp_path / "README.md"
    path.write_text("Heading\n<!-- START -->\nold\n<!-- END -->\nFooter\n", encoding="utf-8")
    update_readme.update_file(path, "<!-- START -->", "<!-- END -->", "first row\nsecond row")
    assert path.read_text(encoding="utf-8") == (
        "Heading\n<!-- START -->\nfirst row\nsecond row\n<!-- END -->\nFooter\n"
    )


def test_update_file_leaves_a_document_with_missing_markers_alone(tmp_path, capsys):
    path = tmp_path / "README.md"
    path.write_text("Heading\n<!-- START -->\nExisting text\n", encoding="utf-8")
    update_readme.update_file(path, "<!-- START -->", "<!-- END -->", "replacement")
    assert path.read_text(encoding="utf-8") == "Heading\n<!-- START -->\nExisting text\n"
    assert "not found" in capsys.readouterr().out
