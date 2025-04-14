from __future__ import annotations

import datetime
from ofxstatement.statement import Currency
from decimal import Decimal
from typing import List, Optional, Union

from pydantic import BaseModel, field_validator


class Amount(BaseModel):
    amount: Decimal
    currency: Currency

    class Config:
        arbitrary_types_allowed = True

    @field_validator("currency", mode="before")
    def validate_currency(cls, value):
        if isinstance(value, str):
            return Currency(value)
        return value


class InstructedAmount(Amount):
    targetCurrency: Optional[Currency] = None
    sourceCurrency: Optional[Currency] = None
    exchangeRate: Optional[float] = None

    @field_validator("targetCurrency", "sourceCurrency", mode="before")
    def validate_currency(cls, value):
        if isinstance(value, str):
            return Currency(value)
        return value


class Account(BaseModel):
    bban: Optional[str] = None


class ReportExchangeRate(BaseModel):
    instructedAmount: Optional[InstructedAmount] = None


class NordigenTransactionModel(BaseModel):
    """
    Nordigen data transaction model.
    """

    balanceAfterTransaction: Optional[float] = None
    bankTransactionCode: Optional[str] = None
    bookingDate: Optional[datetime.datetime] = None
    checkId: Optional[str] = None
    creditorAccount: Optional[Account] = None
    creditorAgent: Optional[str] = None
    creditorId: Optional[str] = None
    creditorName: Optional[str] = None
    currencyExchange: Optional[Union[ReportExchangeRate, InstructedAmount]] = None
    debtorAccount: Optional[Account] = None
    debtorAgent: Optional[str] = None
    debtorName: Optional[str] = None
    endToEndId: Optional[str] = None
    entryReference: Optional[str] = None
    internalTransactionId: Optional[str] = None
    mandateId: Optional[str] = None
    merchantCategoryCode: Optional[str] = None
    proprietaryBankTransactionCode: Optional[str] = None
    purposeCode: Optional[str] = None
    remittanceInformationStructured: Optional[str] = None
    remittanceInformationStructuredArray: Optional[List[str]] = None
    remittanceInformationUnstructured: Optional[str] = None
    remmittanceInformationUnstructuredArray: Optional[List[str]] = None
    transactionAmount: Amount
    transactionId: Optional[str] = None
    ultimateCreditor: Optional[str] = None
    ultimateDebtor: Optional[str] = None
    valueDate: Optional[datetime.date] = None
    valueDateTime: Optional[datetime.datetime] = None
