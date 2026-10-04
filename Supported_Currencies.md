# Supported Currencies

This project uses the [`CurrencyConverter`](https://pypi.org/project/CurrencyConverter/) Python library for currency conversion. It provides daily exchange rates sourced from the **European Central Bank (ECB)** — no API key required.

**Total currencies supported:** 42 (33 actively used + 9 historical/legacy)

## Actively Used Currencies (33)

| Code | Currency                | Code | Currency               |
|------|-------------------------|------|------------------------|
| USD  | US Dollar               | NZD  | New Zealand Dollar     |
| EUR  | Euro                    | PHP  | Philippine Peso        |
| GBP  | British Pound           | PLN  | Polish Zloty           |
| INR  | Indian Rupee            | RON  | Romanian Leu           |
| JPY  | Japanese Yen            | RUB  | Russian Ruble          |
| AUD  | Australian Dollar       | SEK  | Swedish Krona          |
| CAD  | Canadian Dollar         | SGD  | Singapore Dollar       |
| CHF  | Swiss Franc             | THB  | Thai Baht              |
| CNY  | Chinese Yuan            | TRY  | Turkish Lira           |
| BRL  | Brazilian Real          | ZAR  | South African Rand     |
| BGN  | Bulgarian Lev           | CZK  | Czech Koruna           |
| HKD  | Hong Kong Dollar        | DKK  | Danish Krone           |
| HUF  | Hungarian Forint        | HRK  | Croatian Kuna          |
| IDR  | Indonesian Rupiah       | ISK  | Icelandic Krona        |
| ILS  | Israeli Shekel          | KRW  | South Korean Won       |
| MXN  | Mexican Peso            | MYR  | Malaysian Ringgit      |
| NOK  | Norwegian Krone         |      |                        |

## Legacy / Historical Currencies (9)

These are retained in the dataset for historical rate data (pre-euro currencies of countries that have since adopted the euro, or superseded national currencies). They are valid lookups but not relevant for everyday conversions.

| Code | Currency                  |
|------|---------------------------|
| EEK  | Estonian Kroon            |
| LTL  | Lithuanian Litas          |
| LVL  | Latvian Lats              |
| SIT  | Slovenian Tolar           |
| SKK  | Slovak Koruna             |
| CYP  | Cypriot Pound             |
| MTL  | Maltese Lira              |
| ROL  | Romanian Leu (old)        |
| TRL  | Turkish Lira (old)        |

## Checking Supported Currencies Programmatically

```python
from currency_converter import CurrencyConverter

c = CurrencyConverter()
print(sorted(c.currencies))   # list of all 42 currency codes
print(len(c.currencies))      # 42
```

## Notes

- Rates update daily and are **not real-time** (based on ECB's daily reference rates).
- All conversions in this project route through the base currency internally, consistent with how the library itself resolves cross-rates.
- For production use cases requiring real-time or higher-frequency rate updates, consider a dedicated FX API (e.g. exchangerate-api.com, Open Exchange Rates) instead.