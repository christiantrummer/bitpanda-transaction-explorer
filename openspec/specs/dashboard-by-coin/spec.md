## Requirements

### Requirement: By Coin section shows per-coin deposit and withdrawal totals
The page SHALL display a By Coin section with one card per coin that has at least one transaction. Each card SHALL show deposit count, total deposited amount (crypto), total deposited EUR value, withdrawal count, total withdrawn amount (crypto), and total withdrawn EUR value.

#### Scenario: Card shows deposit and withdrawal totals
- **WHEN** transactions have been fetched
- **THEN** a card SHALL appear for each coin with at least one transaction
- **THEN** each card SHALL show deposit count and crypto total for deposits
- **THEN** each card SHALL show withdrawal count and crypto total for withdrawals

#### Scenario: EUR total with all values present
- **WHEN** all transactions for a coin have a valid EUR value
- **THEN** the EUR total SHALL be shown as a formatted euro amount (e.g. €4,230)

#### Scenario: EUR total with some N/A values
- **WHEN** some transactions for a coin are missing EUR value
- **THEN** the EUR total SHALL show the sum of available values plus a count of missing ones (e.g. €4,230 (2 N/A))

#### Scenario: EUR total with all N/A values
- **WHEN** all transactions for a coin are missing EUR value
- **THEN** the EUR total SHALL show N/A

#### Scenario: Cards sorted by total EUR volume
- **WHEN** multiple coins are present
- **THEN** coin cards SHALL be sorted by total EUR volume (deposits + withdrawals) descending
- **THEN** coins with all N/A EUR values SHALL appear last

#### Scenario: Section updates during fetch
- **WHEN** new transaction pages are fetched incrementally
- **THEN** the By Coin section SHALL update to reflect the latest data after each page

### Requirement: Coin card filters all tables
Clicking a coin card SHALL activate a coin filter that applies to the Transactions table and Blockchain Wallets table. Clicking the active coin card again SHALL deactivate the filter and show all coins.

#### Scenario: Click coin card to filter
- **WHEN** user clicks a coin card
- **THEN** the Transactions table SHALL show only transactions for that coin
- **THEN** the Blockchain Wallets table SHALL show only addresses for that coin
- **THEN** the coin card SHALL appear visually highlighted

#### Scenario: Click active coin card to deselect
- **WHEN** a coin card is active
- **WHEN** user clicks the same coin card again
- **THEN** the coin filter SHALL be cleared
- **THEN** both tables SHALL show all coins again
- **THEN** no coin card SHALL appear highlighted

#### Scenario: Coin card and dropdown stay in sync
- **WHEN** user clicks a coin card
- **THEN** the coin filter dropdown SHALL update to show the selected coin
- **WHEN** user changes the coin filter dropdown
- **THEN** the corresponding coin card SHALL become highlighted (or deselected if dropdown set to All)
