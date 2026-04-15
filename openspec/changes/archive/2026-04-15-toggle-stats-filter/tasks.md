## 1. Locate filter state and click handler

- [x] 1.1 Find the TransactionStatistics component and identify where the active filter state is held
- [x] 1.2 Find the click handler for the deposit/withdrawal stat boxes

## 2. Implement toggle logic

- [x] 2.1 Update the click handler so clicking the already-active filter sets the filter to null/undefined (toggle off)
- [x] 2.2 Verify that clicking a different (inactive) box still switches the filter as before

## 3. Add active state styling

- [x] 3.1 Apply an active/selected CSS class to the stat box whose type matches the current filter
- [x] 3.2 Ensure no box shows the active style when the filter is cleared

## 4. Verify end-to-end behavior

- [ ] 4.1 Click deposit → tables show only deposits; click deposit again → all transactions shown
- [ ] 4.2 Click withdrawal → tables show only withdrawals; click withdrawal again → all transactions shown
- [ ] 4.3 Click deposit then withdrawal → switches filter (does not clear)
