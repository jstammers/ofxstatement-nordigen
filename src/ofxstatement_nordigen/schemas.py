from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Optional
import datetime

class Amount(BaseModel):
    amount: float
    currency: str
    # targetCurrency: Optional[str] = None

class InstructedAmount(Amount):
    amount: float
    currency: Optional[str] = None
    targetCurrency: Optional[str] = None
    sourceCurrency: Optional[str] = None
    exchangeRate: Optional[float] = None

class Account(BaseModel):
    bban: Optional[str] = None


class ReportExchangeRate(BaseModel):
    instructedAmount: InstructedAmount = None

class NordigenTransactionModel(BaseModel):
    """
    Nordigen data transaction model.
    """

    balanceAfterTransaction: Optional[float] = None
    bankTransactionCode: Optional[str] = None
    bookingDate: Optional[datetime.date] = None
    checkId: Optional[str] = None
    creditorAccount: Optional[Account] = None
    creditorAgent: Optional[str] = None
    creditorId: Optional[str] = None
    creditorName: Optional[str] = None
    currencyExchange: Optional[ReportExchangeRate | InstructedAmount] = None
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
    transactionAmount: Optional[Amount] = None
    transactionId: Optional[str] = None
    ultimateCreditor: Optional[str] = None
    ultimateDebtor: Optional[str] = None
    valueDate: Optional[datetime.date] = None
    valueDateTime: Optional[datetime.datetime] = None

    # @check()
    # def check_booking_status(self):
    #     if self.booking_status