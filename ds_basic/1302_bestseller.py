def print_bestsellers(n):
    sales_info = dict()
    max_sales = 0

    for i in range(n):
        title = input()
        if title not in sales_info:
            sales_info[title] = 0
        sales_info[title] += 1
        if sales_info[title] > max_sales:
            max_sales = sales_info[title]

    for title, sales in sorted(sales_info.items(), key=lambda x:x[0]):
        if sales == max_sales:
            print(title)
            return



if __name__ == "__main__":
    n = int(input())
    print_bestsellers(n)
