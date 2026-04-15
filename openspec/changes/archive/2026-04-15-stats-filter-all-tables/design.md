## Context

The app is a single `index.html` file. The active filter is stored in the `#typeFilter` `<select>` element's `.value`. `filterTransactions()` reads this value and re-renders only the Transactions table. The Blockchain Wallets table is rendered by `updateBlockchainWallets()`, which is called once after data loads and never again — it has no awareness of the active filter.

Each wallet row in Blockchain Wallets has a `type` field (deposit, withdrawal, or deposit/withdrawal for addresses used both ways).

## Goals / Non-Goals

**Goals:**
- When a deposit or withdrawal filter is active, hide wallet rows whose type does not include the active filter type.
- Keep the Blockchain Wallets table in sync whenever the filter changes.

**Non-Goals:**
- Adding a separate filter control on the Blockchain Wallets table.
- Filtering the Blockchain Wallets table by coin.
- Changing how addresses used for both deposit and withdrawal are handled beyond the filtering logic.

## Decisions

**Read filter value in `updateBlockchainWallets()`**
Add a filter check inside `updateBlockchainWallets()` that reads `#typeFilter`'s current value and skips rows whose type set does not include the active type. This mirrors the same pattern already used in `displayTransactions()`.

Alternative: call `displayTransactions()` and `updateBlockchainWallets()` from a shared `applyFilter()` wrapper. This is cleaner long-term but is more refactoring than needed for this change — the direct approach is sufficient.

**Call `updateBlockchainWallets()` from `filterTransactions()`**
`filterTransactions()` already calls `displayTransactions()`. Adding a call to `updateBlockchainWallets()` here ensures both tables update atomically whenever the filter changes.

**Addresses used for both deposit and withdrawal**
A wallet address can have type = `{deposit, withdrawal}`. When filtering by deposit, such addresses ARE shown (they include deposits). Same for withdrawal. Only rows that exclusively belong to the other type are hidden.

## Risks / Trade-offs

- [Low] `updateBlockchainWallets()` is also called during initial data load (not via `filterTransactions()`). At that point the filter is always empty so this is safe — no filter will be incorrectly applied on load.
