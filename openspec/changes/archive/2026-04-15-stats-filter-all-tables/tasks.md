## 1. Update updateBlockchainWallets() to respect the active filter

- [x] 1.1 Locate `updateBlockchainWallets()` and identify where rows are rendered
- [x] 1.2 Read the current `#typeFilter` value at the start of the function
- [x] 1.3 Skip wallet rows whose type set does not include the active filter type (deposit-only rows hidden when withdrawal filter active, and vice versa)
- [x] 1.4 Addresses used for both deposit and withdrawal remain visible under either filter

## 2. Keep Blockchain Wallets in sync when the filter changes

- [x] 2.1 In `filterTransactions()`, add a call to `updateBlockchainWallets()` so both tables update together when a stat box is clicked

## 3. Verify end-to-end behavior

- [ ] 3.1 Click Deposits → Transactions shows only deposits AND Blockchain Wallets shows only deposit/mixed addresses
- [ ] 3.2 Click Deposits again → both tables show all rows
- [ ] 3.3 Click Withdrawals → Transactions shows only withdrawals AND Blockchain Wallets shows only withdrawal/mixed addresses
- [ ] 3.4 Addresses with both deposit and withdrawal types remain visible under either filter
