def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """Функция принимает два аргумента: stocks - словарь, где ключами являются символы акций
    (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа.
    prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
    Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен."""
    return sum([stocks[x] * prices[y] for x, y in zip(sorted(stocks), sorted(prices))])


# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# # for i in stocks:
# #     values = stocks[i]*prices[i]
# #     print(values)
# #
# values = [stocks[x]*prices[y] for x,y in zip(sorted(stocks), sorted(prices))]
# print(values)
# print(sorted(stocks)[values.index(max(values))])
def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    """Функция принимает два аргумента: initial_value - начальная стоимость портфеля акций.
    current_value - текущая стоимость портфеля акций.
    Функция должна вернуть процентную доходность портфеля."""
    return ((current_value / initial_value) * 100) - 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    """Функция  принимает два аргумента: stocks - словарь с акциями и их количеством.
     prices - словарь с акциями и их текущими ценами.
     Функция возвращает символ акции (ключ),
     которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью."""
    global initial_package_price
    current_value_of_the_package = calculate_portfolio_value(stocks, prices)
    share_package = [stocks[x] * prices[y] for x, y in zip(sorted(stocks), sorted(prices))]
    # share_package = sum([stocks[stock] for stock in sorted(stocks)])
    shares_of_stock = [round(stock*100/current_value_of_the_package, 2) for stock in share_package]
    package_price_difference = current_value_of_the_package - initial_package_price
    b = [package_price_difference * percent_of_stock/100 for percent_of_stock in shares_of_stock]
    max_profitability_of_shares = [x - prices[y] for x, y in zip(b, sorted(prices))]
    return sorted(stocks)[max_profitability_of_shares.index(max(max_profitability_of_shares))]


if __name__ == '__main__':
    initial_package_price = calculate_portfolio_value({"AAPL": 10, "MSFT": 8, "GOOGL": 5, },
                                  {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50})
    # print(calculate_portfolio_return(10000, 15000))
    print(get_most_profitable_stock({"AAPL": 10, "GOOGL": 5, "MSFT": 8},
                                    {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}))
