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


@pytest.mark.parametrize("filename", ["CAISSEDEPARGNE_ILE_DE_FRANCE_CEPAFRPP751.json"])
def test_CAISSEDEPARGNE_ILE_DE_FRANCE(filename: str) -> None:
    """Test parsing the CAISSEDEPARGNE_ILE_DE_FRANCE_CEPAFRPP751.json file."""
    here = os.path.dirname(__file__)
    sample_filename = os.path.join(here, "data", filename)
    expected_filename = sample_filename.replace(".json", ".ofx")

    parser = NordigenParser(sample_filename)
    statement = parser.parse()

    # Verify the statement properties
    assert len(statement.lines) == 1

    # Verify the transaction details
    transaction = statement.lines[0]
    assert transaction.id == "6666666"

    assert (
        transaction.date is not None
    )  # Fix for mypy: Check that date is not None before accessing date() method
    assert transaction.date.date() == date(2025, 5, 13)

    assert transaction.amount == Decimal("-1")

    assert (
        transaction.currency is not None
    )  # Fix for mypy: Check that currency is not None before accessing symbol attribute
    assert transaction.currency.symbol == "EUR"

    # Check if the memo contains the combined information from remittanceInformationUnstructuredArray
    assert (
        transaction.memo is not None
    )  # Fix for mypy: Check that memo is not None before using 'in' operator
    assert "PRLV assurance" in transaction.memo
