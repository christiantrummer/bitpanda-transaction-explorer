## 1. Filter state and helper

- [x] 1.1 Add `activeCoinFilter` (null or coin symbol) and `activeTimeFilter` (null or `{year, month?}`) global variables
- [x] 1.2 Add `setCoinFilter(coin)` helper that sets `activeCoinFilter`, syncs `#coinFilter` dropdown, and re-renders all tables
- [x] 1.3 Add `setTimeFilter(year, month)` helper that sets `activeTimeFilter` and re-renders the Transactions table
- [x] 1.4 Extend `filterTransactions()` to apply `activeCoinFilter` (skip tx where coin !== activeCoinFilter) and `activeTimeFilter` (skip tx outside the year/month)
- [x] 1.5 Extend `updateBlockchainWallets()` to apply `activeCoinFilter` (skip wallets for other coins)
- [x] 1.6 Add `onchange` handler to `#coinFilter` dropdown to call `setCoinFilter()` and keep coin cards in sync

## 2. By Coin section — HTML + CSS

- [x] 2.1 Add By Coin card section to the page between Transaction Statistics and Transactions (hidden until data loads)
- [x] 2.2 Add CSS for coin cards (grid layout, deposit/withdrawal columns, active/highlighted state matching existing `.stat-card.active` style)

## 3. By Coin section — rendering

- [x] 3.1 Write `updateCoinDashboard()`: aggregate transactions by coin (deposit count, crypto total, EUR total; same for withdrawals)
- [x] 3.2 Handle EUR totals: sum valid values, count N/As, display as "€X,XXX", "€X,XXX (N N/A)", or "N/A"
- [x] 3.3 Sort coin cards by total EUR volume descending; coins with all-N/A EUR last
- [x] 3.4 Render one card per coin; attach click handler to toggle `activeCoinFilter` via `setCoinFilter()`
- [x] 3.5 Apply `.active` highlight to the card matching `activeCoinFilter`
- [x] 3.6 Call `updateCoinDashboard()` from the fetch loop (same cadence as `displayTransactions()`)

## 4. By Time section — HTML + CSS

- [x] 4.1 Add By Time card section below By Coin (hidden until data loads)
- [x] 4.2 Add CSS for year rows, month sub-rows, expand/collapse chevron, and active highlight

## 5. By Time section — rendering

- [x] 5.1 Write `updateTimeDashboard()`: aggregate transactions by year and month
- [x] 5.2 Render year rows sorted descending; skip years with no transactions
- [x] 5.3 Render month sub-rows inside a collapsible container per year; skip months with no transactions; sort chronologically
- [x] 5.4 Attach click handler to year rows: toggle expand/collapse of month rows AND toggle `activeTimeFilter` for year via `setTimeFilter()`
- [x] 5.5 Attach click handler to month rows: toggle `activeTimeFilter` for that month via `setTimeFilter()`; only one time period active at a time
- [x] 5.6 Apply active highlight to the row matching `activeTimeFilter`
- [x] 5.7 Call `updateTimeDashboard()` from the fetch loop (same cadence as `displayTransactions()`)

## 6. Verify end-to-end

- [ ] 6.1 Coin card click filters Transactions and Blockchain Wallets; second click clears; dropdown stays in sync
- [ ] 6.2 Dropdown change highlights correct coin card (or clears all if set to All)
- [ ] 6.3 Year row click filters Transactions to that year; second click clears
- [ ] 6.4 Month row click filters Transactions to that month; replaces active year filter
- [ ] 6.5 Type + coin + time filters all stack correctly (AND logic)
- [ ] 6.6 Sections update incrementally during fetch without breaking layout

