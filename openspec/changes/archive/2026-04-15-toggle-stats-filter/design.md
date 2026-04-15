## Context

The Transaction Statistics section renders clickable boxes for deposit and withdrawal counts/values. Clicking a box sets a filter that narrows the tables below. The filter state is held in a React state variable. Currently there is no path to clear the filter once set — the click handler only ever assigns a new filter value.

## Goals / Non-Goals

**Goals:**
- Allow a user to click an already-active filter box to deselect it and return to the unfiltered view.
- Show a clear visual indicator on the active filter box so users know a filter is applied.

**Non-Goals:**
- Multi-select filtering (selecting both deposit and withdrawal simultaneously).
- Adding a separate "clear filter" button.
- Changing any other aspect of the statistics display or table behavior.

## Decisions

**Toggle via conditional setState**
When a stat box is clicked, check if its type matches the current active filter. If it does, clear the filter (set to `null` / `undefined`); otherwise, set it to the clicked type. This is a one-line conditional change in the existing click handler — no new state, no new components.

Alternative considered: a separate "clear" button. Rejected — the toggle approach is discoverable (the active item is clickable) and requires no extra UI element.

**Active state styling**
Apply a CSS class (e.g. `active` or `selected`) to the box whose type matches the current filter. Use the existing styling system (Tailwind or CSS module, whichever is already in use) to highlight it — e.g. a brighter border or background.

## Risks / Trade-offs

- [Low] If the filter state is lifted to a parent component or a context, the toggle logic goes there instead of the stat box component. The approach is the same regardless of where the state lives.

## Migration Plan

No data migration needed. The change is purely frontend state logic and styling — no API calls, no persistence. Deploy as a normal UI update.
