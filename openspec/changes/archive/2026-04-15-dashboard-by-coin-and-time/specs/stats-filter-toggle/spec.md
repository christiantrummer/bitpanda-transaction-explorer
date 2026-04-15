## ADDED Requirements

### Requirement: All active filters stack with AND logic
The type filter, coin filter, and time period filter SHALL all be independent and apply simultaneously. A transaction SHALL only appear in the Transactions table if it matches all active filters.

#### Scenario: Type and coin filters both active
- **WHEN** the deposit type filter is active
- **WHEN** a coin card filter (e.g. BTC) is active
- **THEN** the Transactions table SHALL show only BTC deposit transactions

#### Scenario: Type, coin, and time filters all active
- **WHEN** the deposit type filter is active
- **WHEN** a coin card filter is active
- **WHEN** a time period filter is active
- **THEN** the Transactions table SHALL show only transactions matching all three criteria

#### Scenario: Clearing one filter keeps others active
- **WHEN** multiple filters are active
- **WHEN** user deactivates one filter
- **THEN** the remaining active filters SHALL still apply
