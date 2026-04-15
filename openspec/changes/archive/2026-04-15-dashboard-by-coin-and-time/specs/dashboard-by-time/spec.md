## ADDED Requirements

### Requirement: By Time section shows transaction totals grouped by year
The page SHALL display a By Time section with one row per year that has at least one transaction. Each year row SHALL show deposit count, total deposited EUR, withdrawal count, and total withdrawn EUR for that year. Years SHALL be sorted descending (most recent first). Years with no transactions SHALL NOT be shown.

#### Scenario: Year rows shown for active years only
- **WHEN** transactions span multiple years
- **THEN** one row SHALL appear per year with at least one transaction
- **THEN** years with no transactions SHALL NOT appear
- **THEN** rows SHALL be sorted most recent year first

#### Scenario: Year row shows deposit and withdrawal totals
- **WHEN** a year has both deposits and withdrawals
- **THEN** the year row SHALL show deposit count and EUR total for deposits
- **THEN** the year row SHALL show withdrawal count and EUR total for withdrawals

#### Scenario: EUR values follow N/A rules
- **WHEN** some transactions in a year have no EUR value
- **THEN** EUR totals SHALL follow the same N/A display rules as the By Coin section

### Requirement: Year rows expand to show monthly breakdown
Clicking a year row SHALL expand it to show one sub-row per month with activity in that year. Clicking the year row again SHALL collapse the month rows.

#### Scenario: Expand year to see months
- **WHEN** user clicks a year row
- **THEN** month sub-rows SHALL appear below it for each month with at least one transaction
- **THEN** months with no transactions SHALL NOT appear
- **THEN** months SHALL be sorted chronologically within the year

#### Scenario: Collapse year
- **WHEN** a year row is expanded
- **WHEN** user clicks the year row again
- **THEN** the month sub-rows SHALL collapse and no longer be visible

#### Scenario: Month row shows deposit and withdrawal totals
- **WHEN** a month row is visible
- **THEN** it SHALL show deposit count and EUR total for deposits in that month
- **THEN** it SHALL show withdrawal count and EUR total for withdrawals in that month

### Requirement: Time period filter applied by clicking year or month row
Clicking a year or month row SHALL activate a time period filter on the Transactions table. Clicking the active row again SHALL clear the filter.

#### Scenario: Click year row to filter by year
- **WHEN** user clicks a year row
- **THEN** the Transactions table SHALL show only transactions from that year
- **THEN** the year row SHALL appear visually highlighted

#### Scenario: Click month row to filter by month
- **WHEN** a year is expanded and user clicks a month row
- **THEN** the Transactions table SHALL show only transactions from that month and year
- **THEN** the month row SHALL appear visually highlighted

#### Scenario: Click active year or month row to deselect
- **WHEN** a time period filter is active
- **WHEN** user clicks the same row again
- **THEN** the time period filter SHALL be cleared
- **THEN** the Transactions table SHALL show transactions for all periods

#### Scenario: Only one time period active at a time
- **WHEN** a year filter is active and user clicks a month row
- **THEN** the month filter SHALL replace the year filter (not stack)
- **THEN** only the clicked month row SHALL be highlighted
