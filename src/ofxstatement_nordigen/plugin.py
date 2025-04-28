import json
from typing import Iterable
from datetime import datetime
from ofxstatement.plugin import Plugin
from ofxstatement.parser import StatementParser
from ofxstatement.statement import Statement, StatementLine

from ofxstatement_nordigen.schemas import NordigenTransactionModel


class NordigenPlugin(Plugin):
    """Retrieves Nordigen transactions and converts them to OFX format."""

    def get_parser(self, filename: str) -> "NordigenParser":
        default_ccy = self.settings.get("currency")
        account_id = self.settings.get("account")
        return NordigenParser(filename, default_ccy, account_id)


class NordigenParser(StatementParser[str]):
    def __init__(self, filename: str, currency: str = None, account_id: str = None) -> None:
        super().__init__()
        if not filename.endswith(".json"):
            raise ValueError("Only JSON files are supported")
        self.filename = filename
        self.currency = currency
        self.account_id = account_id

    def parse(self) -> Statement:
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        with open(self.filename, "r"):
            statement = super().parse()
            dates = [
                line.date for line in statement.lines if isinstance(line.date, datetime)
            ]
            if len(dates) > 0:
                statement.start_date = min(dates)
                statement.end_date = max(dates)
            statement.account_id = self.account_id
            statement.currency = self.currency or statement.currency
            return statement

    def split_records(self) -> Iterable[str]:
        """Return iterable object consisting of a line per transaction"""
        data = json.load(open(self.filename, "r"))
        transactions = data.get("transactions", {})
        booked_transactions = transactions.get("booked", [])
        return [json.dumps(transaction) for transaction in booked_transactions]

    def parse_record(self, line: str) -> StatementLine:
        """Parse given transaction line and return StatementLine object"""

        # TODO: Infer transaction type from transaction data
        statement = StatementLine()
        transaction = json.loads(line)
        transaction_data = NordigenTransactionModel(**transaction)
        statement.id = transaction_data.transactionId
        statement.date = transaction_data.bookingDateTime
        statement.amount = transaction_data.transactionAmount.amount
        statement.memo = transaction_data.remittanceInformationUnstructured
        statement.payee = transaction_data.creditorName or transaction_data.debtorName
        statement.date_user = transaction_data.valueDateTime
        statement.check_no = transaction_data.checkId
        statement.refnum = transaction_data.internalTransactionId
        statement.currency = transaction_data.transactionAmount.currency
        if transaction_data.currencyExchange and hasattr(
            transaction_data.currencyExchange, "sourceCurrency"
        ):
            statement.orig_currency = transaction_data.currencyExchange.sourceCurrency
        return statement
