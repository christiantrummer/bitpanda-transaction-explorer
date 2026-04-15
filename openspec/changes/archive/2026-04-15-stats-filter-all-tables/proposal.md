## Why

The deposit/withdrawal filter in Transaction Statistics currently only narrows the Transactions table. The Blockchain Wallets table (which lists unique addresses per type) is unaffected, so filtering by deposit still shows withdrawal-only addresses — inconsistent and confusing.

## What Changes

- When a deposit or withdrawal filter is active, the Blockchain Wallets table SHALL also be filtered to show only rows whose type matches the active filter.
- When the filter is cleared, the Blockchain Wallets table returns to showing all rows.
- The existing Transactions table filtering behavior is unchanged.

## Capabilities

### New Capabilities

### Modified Capabilities
- `stats-filter-toggle`: Extend the scope of the filter — it must now apply to all data tables (Transactions and Blockchain Wallets), not just the Transactions table.

## Impact

- `filterTransactions()` function in `index.html` — needs to also trigger a re-render of the Blockchain Wallets table
- `updateBlockchainWallets()` (or equivalent) — needs to respect the active filter when rendering rows
