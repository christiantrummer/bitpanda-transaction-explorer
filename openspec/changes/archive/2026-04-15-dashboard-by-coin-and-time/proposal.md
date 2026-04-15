## Why

The transaction list is useful but gives no quick overview of what's happening per coin or over time. Users want to see their deposit/withdrawal history summarised by coin and by time period without scanning every row.

## What Changes

- Add a **By Coin** section between Transaction Statistics and Transactions: one card per coin showing deposit count, deposit total (crypto + EUR), withdrawal count, withdrawal total (crypto + EUR). Missing EUR values shown as N/A. Clicking a card filters all tables by that coin (toggleable, same card click deselects).
- Add a **By Time** section below By Coin: year rows always visible, click a year to expand its months. Only years/months with activity are shown. Clicking a year or month filters all tables to that time period (toggleable).
- All filters (type, coin, time period) are independent and stack with AND logic — the existing coin `<select>` dropdown stays in sync with the coin card filter.
- Both sections update live as transactions are fetched (same as the existing tables).

## Capabilities

### New Capabilities
- `dashboard-by-coin`: Per-coin summary cards with clickable filter integration
- `dashboard-by-time`: Expandable year/month breakdown with clickable filter integration

### Modified Capabilities
- `stats-filter-toggle`: The coin card filter and time period filter are new filter dimensions that stack with the existing type filter using AND logic.

## Impact

- `index.html` — new By Coin and By Time sections added to the page
- `filterTransactions()` and `updateBlockchainWallets()` — extended to respect an active coin-card filter and active time-period filter
- Existing coin `<select>` dropdown kept in sync with coin card active state
- No new dependencies, no API changes
