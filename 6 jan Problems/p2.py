from array import*

def count_span(stocks ,spans, days):
    
    for i in range(days):
        span = 1 
        j = i-1

        while(j >=0 and stocks[i] > stocks[j]):
            span += 1
            j -= 1

        spans.append(span)

    return spans

days = 8

stocks = array('i',[60, 70, 80, 100, 90, 75, 80, 120])

spans = array('i',[])

count_span(stocks, spans, days)

print(stocks)
print("The span of the stock prices is: ")
print(spans)