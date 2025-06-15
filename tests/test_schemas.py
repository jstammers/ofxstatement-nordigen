import pytest

from ofxstatement_nordigen.schemas import NordigenTransactionModel


@pytest.mark.parametrize(
    "data",
    [
        {
            "transactionId": "123456789",
            "transactionAmount": {"amount": 100.0, "currency": "EUR"},
            "valueDate": "2023-10-01",
            "valueDateTime": "2023-10-01T12:00:00Z",
            "remittanceInformationStructured": "Payment for invoice #12345",
        },
        {
            "transactionId": "987654321",
            "entryReference": "REF123456",
            "bookingDate": "2025-03-31",
            "bookingDateTime": "2025-03-31T00:00:00+00:00",
            "transactionAmount": {"amount": "-1521.00", "currency": "GBP"},
            "remittanceInformationUnstructured": "Payment for invoice #67890",
            "additionalInformation": "Payment received",
            "proprietaryBankTransactionCode": "BP",
            "internalTransactionId": "INT123456",
        },
        {
            "transactionId": "anonymized_transaction_id",
            "entryReference": "anonymized_entry_reference",
            "bookingDate": "2025-04-05",
            "valueDate": "2025-04-05",
            "bookingDateTime": "2025-04-05T00:00:00+00:00",
            "valueDateTime": "2025-04-05T00:00:00+00:00",
            "transactionAmount": {"amount": "0.00", "currency": "XXX"},
            "currencyExchange": [{"sourceCurrency": "XXX", "exchangeRate": "0.0"}],
            "remittanceInformationUnstructured": "anonymized_remittance_information",
            "additionalInformation": "anonymized_additional_information",
            "additionalDataStructured": {
                "CardSchemeName": "anonymized_card_scheme",
                "Name": "anonymized_name",
                "Identification": "anonymized_identification",
            },
            "internalTransactionId": "anonymized_internal_transaction_id",
        },
        {
            "transactionId": "anonymized_transaction_id",
            "bookingDate": "2025-04-05",
            "bookingDateTime": "2025-05-05T07:20:42.19Z",
            "transactionAmount": {"amount": "-100.0000", "currency": "GBP"},
            "currencyExchange": [
                {
                    "quotationDate": "2025-04-05",
                    "sourceCurrency": "AUD",
                    "exchangeRate": "2.04501",
                    "unitCurrency": "GBP",
                    "targetCurrency": "GBP",
                }
            ],
            "remittanceInformationUnstructured": "anonymized_remittance_information",
            "proprietaryBankTransactionCode": "anonymized_code",
            "internalTransactionId": "anonymized_internal_transaction_id",
        },
    ],
)
def test_go_cardless_transaction_model(data):
    validated = NordigenTransactionModel(**data)
    print(validated)
    assert validated is not None
