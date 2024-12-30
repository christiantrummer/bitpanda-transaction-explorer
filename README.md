# Bitpanda Transaction Explorer

A web application for exploring your Bitpanda transactions with enhanced filtering and export capabilities.

![Dashboard](dashboard.png)

## Features

- 🔄 Transaction fetching from Bitpanda API
- 🔍 Transaction filtering
- 📊 Transaction statistics
- 💾 CSV Export functionality for transaction data

## Usage

### Option 1: Use the Hosted Version (Recommended)

1. Visit [https://christiantrummer.github.io/bitpanda-transaction-explorer](https://christiantrummer.github.io/bitpanda-transaction-explorer)
2. Create a new API key at [Bitpanda API Settings](https://web.bitpanda.com/my-account/apikey) with the `Transaction` and `Balance` permissions
3. Paste the API key into the input field
4. Click "Fetch Transactions" to load your transactions

### Option 2: Run Locally

If you prefer to run the application locally, you'll need to serve it through a web server due to CORS restrictions. Simply opening the HTML file directly in a browser won't work.

You can use any web server of your choice, for example:
- Python: `python -m http.server`
- Node.js: `npx http-server`

## Security

Your data and API key remain secure as everything runs in your browser. The API key is only used to communicate directly with Bitpanda's servers - it never needs to be stored anywhere and no third parties are involved.

## Acknowledgments

Built about 90% of the code with Claude 3.5 Sonnet.