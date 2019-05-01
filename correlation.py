from pylab import plot, show

def find_correlation(x, y):
    n=len(x)
    products = []
    for xi, yi in zip(x,y):
        products.append(xi * yi)
    sum_products = sum(products)

    sum_x=sum(x)
    sum_y=sum(y)

    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi**2)
    y_square_sum =  sum(y_square)

    numerator = n*sum_products - sum_x * sum_y
    denominator1 = n*x_square_sum - squared_sum_x
    denominator2 = n*y_square_sum - squared_sum_y
    denominator = (denominator1*denominator2)**0.5
    correlation = numerator / denominator

    return correlation
    
high_school = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
college = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
data = range(1,11)
c = find_correlation(high_school, college)
print('Correlation between data sets is: {}'.format(c))

show(plot(data, high_school, data, college, marker='o'))
