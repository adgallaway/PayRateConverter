import configparser

def tax(pay):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    tax_rate = float(config['TAX']['rate']) / 100

    after_tax = pay - (pay * tax_rate)
    return after_tax