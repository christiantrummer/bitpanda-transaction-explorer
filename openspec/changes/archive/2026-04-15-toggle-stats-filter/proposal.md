## Why

Clicking a deposit or withdrawal stat box in Transaction Statistics filters the tables below, but there is no way to clear the filter — the user is stuck in a filtered view until they reload the page. Clicking the active filter box again should toggle it off and restore the unfiltered view.

## What Changes

- Clicking a stat box that is **already active** deselects it and removes the filter, showing all transactions again.
- The active stat box gets a visible selected/highlighted state so users know which filter is applied.
- Only one filter can be active at a time (existing behavior); clicking a different box still switches the filter.

## Capabilities

### New Capabilities
- `stats-filter-toggle`: Toggle behavior for Transaction Statistics filter boxes — clicking an active filter deselects it and clears the filter.

### Modified Capabilities

## Impact

- `TransactionStatistics` component (filter click handler and active state styling)
- The table(s) below that react to the filter state
