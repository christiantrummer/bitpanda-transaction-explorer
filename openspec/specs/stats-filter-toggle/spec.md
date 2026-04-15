## Requirements

### Requirement: Filter box toggles off when clicked while active
When a stat box (deposit or withdrawal) is already the active filter, clicking it again SHALL clear the filter and display all transactions in all data tables below.

#### Scenario: Click active deposit filter to deselect
- **WHEN** the deposit stat box is active (filter is set to deposit)
- **WHEN** the user clicks the deposit stat box again
- **THEN** the filter SHALL be cleared
- **THEN** all transactions (deposits and withdrawals) SHALL be shown in the Transactions table
- **THEN** all wallet addresses SHALL be shown in the Blockchain Wallets table

#### Scenario: Click active withdrawal filter to deselect
- **WHEN** the withdrawal stat box is active (filter is set to withdrawal)
- **WHEN** the user clicks the withdrawal stat box again
- **THEN** the filter SHALL be cleared
- **THEN** all transactions (deposits and withdrawals) SHALL be shown in the Transactions table
- **THEN** all wallet addresses SHALL be shown in the Blockchain Wallets table

#### Scenario: Switching between filters still works
- **WHEN** the deposit stat box is active
- **WHEN** the user clicks the withdrawal stat box
- **THEN** the filter SHALL switch to withdrawal (not clear)
- **THEN** only withdrawal transactions SHALL be shown in the Transactions table
- **THEN** only withdrawal wallet addresses SHALL be shown in the Blockchain Wallets table

### Requirement: Active filter applies to Blockchain Wallets table
When a deposit or withdrawal filter is active, the Blockchain Wallets table SHALL show only rows whose address type includes the active filter type. When the filter is cleared, all wallet rows SHALL be shown.

#### Scenario: Deposit filter hides withdrawal-only wallets
- **WHEN** the deposit filter is active
- **THEN** wallet addresses used exclusively for withdrawals SHALL NOT be shown in the Blockchain Wallets table
- **THEN** wallet addresses used for deposits (including deposit/withdrawal) SHALL be shown

#### Scenario: Withdrawal filter hides deposit-only wallets
- **WHEN** the withdrawal filter is active
- **THEN** wallet addresses used exclusively for deposits SHALL NOT be shown in the Blockchain Wallets table
- **THEN** wallet addresses used for withdrawals (including deposit/withdrawal) SHALL be shown

#### Scenario: No filter shows all wallets
- **WHEN** no filter is active
- **THEN** all wallet addresses SHALL be shown in the Blockchain Wallets table regardless of type

### Requirement: Active filter box has a visible selected state
The currently active stat box SHALL display a visual indicator distinguishing it from inactive boxes, so users can tell a filter is applied.

#### Scenario: Active box is visually highlighted
- **WHEN** a stat box is clicked and its filter is applied
- **THEN** that stat box SHALL appear visually distinct (e.g. highlighted border or background) compared to inactive boxes

#### Scenario: No box is highlighted when no filter is active
- **WHEN** no filter is active (initial state or after toggling off)
- **THEN** no stat box SHALL display the active/selected visual state
