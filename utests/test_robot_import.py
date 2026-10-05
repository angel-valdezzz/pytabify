from io import StringIO

import pytest
from robot import run
from robot.libdocpkg import LibraryDocumentation


@pytest.mark.parametrize("library", ["Pytabify", "pytabify.robot.PyTabifyLibrary"])
def test_robot_import_runs_keywords_without_alias(library, tmp_path):
    suite = tmp_path / "import.robot"
    suite.write_text(
        f"""*** Settings ***
Library    {library}

*** Test Cases ***
Create And Read A Table
    ${{records}}=    Create List    ${{{{ {{"name": "Alice"}} }}}}
    ${{table}}=    Create Data Table From Records    ${{records}}
    ${{row}}=    Get Data Table Row    ${{table}}    0
    Should Be Equal    ${{row.name}}    Alice
""",
        encoding="utf-8",
    )
    output = StringIO()
    assert run(str(suite), outputdir=str(tmp_path), stdout=output, stderr=output) == 0, (
        output.getvalue()
    )


def test_short_import_preserves_keyword_reference():
    public = LibraryDocumentation("Pytabify")
    legacy = LibraryDocumentation("pytabify.robot.PyTabifyLibrary")
    assert public.name == "Pytabify"
    assert public.doc == legacy.doc
    assert [(kw.name, kw.doc, str(kw.args)) for kw in public.keywords] == [
        (kw.name, kw.doc, str(kw.args)) for kw in legacy.keywords
    ]
