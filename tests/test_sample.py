import os
import pytest
from ofxstatement.ui import UI

from ofxstatement_nordigen.plugin import NordigenPlugin, NordigenParser
from ofxstatement import ofx


def test_sample() -> None:
    plugin = NordigenPlugin(UI(), {})
    here = os.path.dirname(__file__)
    for filename in os.listdir(here):
        if filename.endswith(".json"):
            sample_filename = os.path.join(here, filename)
            parser = plugin.get_parser(sample_filename)
            statement = parser.parse()
            assert len(statement.lines) > 0


@pytest.mark.parametrize("filename", ["test_date.json"])
def test_parse_record(filename: str) -> None:
    here = os.path.dirname(__file__)
    sample_filename = os.path.join(here, "data", filename)
    expected_filename = sample_filename.replace(".json", ".ofx")

    parser = NordigenParser(sample_filename)
    statement = parser.parse()

    expected = open(expected_filename, "r").read()
    writer = ofx.OfxWriter(statement)
    result = writer.toxml(pretty=True)

    # Get everything between the <STMTTRNRS> and </STMTTRNRS> tags
    result = result[
        result.index("<STMTTRNRS>") : result.index("</STMTTRNRS>") + len("</STMTTRNRS>")
    ]
    expected = expected[
        expected.index("<STMTTRNRS>") : expected.index("</STMTTRNRS>")
        + len("</STMTTRNRS>")
    ]

    assert result == expected
