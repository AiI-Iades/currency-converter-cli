import argparse
import requests

def convert_currency(amount, from_currency, to_currency):
    # Example API: https://api.exchangerate-api.com/
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}'
    response = requests.get(url)
    data = response.json()

    if to_currency not in data['rates']:
        raise ValueError(f"Unsupported currency: {to_currency}")

    return amount * data['rates'][to_currency.upper()] 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert currencies')
    parser.add_argument('amount', type=float, help='Amount to convert')
    parser.add_argument('from_currency', choices=['USD', 'EUR', 'GBP', 'JPY', 'CAD'], help='Currency to convert from')
    parser.add_argument('to_currency', choices=['USD', 'EUR', 'GBP', 'JPY', 'CAD'], nargs='?', default='USD', help='Currency to convert to')

    args = parser.parse_args()
    result = convert_currency(args.amount, args.from_currency, args.to_currency)
    print(f"{args.amount} {args.from_currency} = {result:.2f} {args.to_currency}")