#!/usr/bin/env python3

import os
import json
import pytest
from datetime import datetime, date
from decimal import Decimal

from ofxstatement.ui import UI
from ofxstatement import ofx
from ofxstatement.statement import StatementLine, Currency

from ofxstatement_nordigen.plugin import NordigenPlugin, NordigenParser
from ofxstatement_nordigen.schemas import NordigenTransactionModel

@pytest.mark.parametrize("filename", ["BANQUEPOPULAIRE_RIVES_DE_PARIS_CCBPFRPPMTG.json"])
def test_banquepopulaire_rives_de_paris(filename: str) -> None:
    """Test parsing the BANQUEPOPULAIRE_RIVES_DE_PARIS_CCBPFRPPMTG.json file."""
    here = os.path.dirname(__file__)
    sample_filename = os.path.join(here, "data", filename)
    expected_filename = sample_filename.replace(".json", ".ofx")

    parser = NordigenParser(sample_filename)
    statement = parser.parse()

    # Verify the statement properties
    assert len(statement.lines) == 1

    # Verify the transaction details
    transaction = statement.lines[0]
    assert transaction.id == "202500400015"
    assert transaction.date.date() == date(2025, 5, 2)
    assert transaction.amount == Decimal("-8.43")
    assert transaction.currency == Currency("EUR")
    assert transaction.refnum == "YYYYYYYYYYYYYY"

    # Check if the memo contains the combined information from remittanceInformationUnstructuredArray
    assert "CB****2222" in transaction.memo
    assert "Food Restaurant" in transaction.memo

    # Compare with expected OFX output
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
