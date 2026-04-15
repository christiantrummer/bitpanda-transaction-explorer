## Context

The app is a single `index.html` file. All state lives in JS variables: `transactions` (array), `uniqueWallets` (Map), `uniqueCoins` (Set). Filtering is done by reading `#typeFilter` (select) and two new filter values we'll add. The existing `filterTransactions()` and `updateBlockchainWallets()` functions re-render their tables from scratch on every call, which is the pattern we'll follow for the new sections too.

Transactions are fetched incrementally (page by page), so all new sections must tolerate being called repeatedly during fetch — same as `displayTransactions()` and `updateBlockchainWallets()` today.

## Goals / Non-Goals

**Goals:**
- Render a By Coin section: one card per coin, deposit and withdrawal totals side by side, clickable to filter tables.
- Render a By Time section: year rows, expandable to months, clickable to filter tables.
- All three filter dimensions (type, coin, time) stack with AND logic.
- Coin card and existing coin `<select>` stay in sync.

**Non-Goals:**
- Charts or visualisations beyond text/numbers.
- Filtering the Bitpanda Wallets table (it's not transaction-based).
- Persisting filter state across page reloads.
- Price conversion for N/A EUR values.

## Decisions

**Two new global filter variables: `activeCoinFilter` and `activeTimeFilter`**
Mirrors the existing pattern where `#typeFilter.value` holds the type filter. `activeCoinFilter` holds a coin symbol string or `null`. `activeTimeFilter` holds `{year, month}` where month is optional, or `null`. All three filter variables are read in `filterTransactions()` and `updateBlockchainWallets()`.

**By Coin: aggregate from `transactions` array on each render**
No separate data structure. On each call to `updateCoinDashboard()`, iterate `transactions`, group by coin, sum amounts and EUR values. Fast enough for the expected data size (hundreds to low thousands of transactions). This avoids maintaining a parallel data structure that could get out of sync.

**EUR totals: sum only transactions where `amount_eur` is a valid number; show count of N/A transactions separately**
E.g. "€4,230 (2 N/A)". This is more honest than silently excluding or showing a wrong total.

**By Time: aggregate from `transactions` array on each render**
Same approach as By Coin. Parse `attrs.time.date_iso8601` to extract year and month. Group and sort descending (most recent first).

**Expandable years: DOM toggle, no re-render**
Year rows are always rendered. Month rows are rendered inside a collapsible container per year. Clicking a year header toggles a CSS class to show/hide the month rows — no data re-render needed for expand/collapse.

**Coin card clicks sync the existing `#coinFilter` select**
When a coin card is activated, set `#coinFilter.value` to that coin. When deactivated, reset to `""`. When `#coinFilter` changes via the dropdown, update `activeCoinFilter` and the active card highlight accordingly. This keeps both controls in sync without duplicating filter logic.

**Insertion point in the page**
New sections are inserted as cards between the Transaction Statistics card and the Transactions card. They are hidden (`display:none`) until at least one transaction has been processed.

## Risks / Trade-offs

- [Low] Re-aggregating on every incremental fetch page could flicker or feel slow with very large datasets. Mitigation: same pattern already used by `displayTransactions()` — acceptable for this use case.
- [Low] `activeCoinFilter` and `#coinFilter` can diverge if one is updated without the other. Mitigation: always update both together in a single helper function `setCoinFilter(coin)`.
