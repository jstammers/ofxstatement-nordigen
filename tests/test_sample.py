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
            assert statement.start_date is not None
            assert statement.end_date is not None
            assert statement.account_id is not None


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

    # Get everything between the <STMTTRN> and </STMTTRN> tags
    result = result[
        result.index("<STMTTRN>") : result.index("</STMTTRN>") + len("</STMTTRN>")
    ]
    expected = expected[
        expected.index("<STMTTRN>") : expected.index("</STMTTRN>") + len("</STMTTRN>")
    ]

    assert result == expected
