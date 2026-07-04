import argparse
import forex_python.converter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('from_currency', help='Currency to convert from')
    parser.add_argument('to_currency', help='Currency to convert to')
    parser.add_argument('amount', type=float, help='Amount to convert')
    args = parser.parse_args()

    converter = forex_python.converter.CurrencyConverter()
    result = converter.convert(args.amount, args.from_currency, args.to_currency)
    print(f'{args.amount} {args.from_currency} = {result} {args.to_currency}')

if __name__ == '__main__':
    main()