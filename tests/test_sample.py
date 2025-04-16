import os

from ofxstatement.ui import UI

from ofxstatement_nordigen.plugin import NordigenPlugin


def test_sample() -> None:
    plugin = NordigenPlugin(UI(), {})
    here = os.path.dirname(__file__)
    for filename in os.listdir(here):
        if filename.endswith(".json"):
            sample_filename = os.path.join(here, filename)
            parser = plugin.get_parser(sample_filename)
            statement = parser.parse()
            assert len(statement.lines) > 0
