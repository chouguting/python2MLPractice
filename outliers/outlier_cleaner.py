#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy
    zipall = zip(predictions, ages, net_worths)
    zipall2 = sorted(zipall, key=lambda t: abs(t[0]-t[2]))
    predictions, ages, net_worths = zip(*zipall2)
    predictions=list(predictions)
    ages = list(ages)
    net_worths = list(net_worths)
    predictions = predictions[0:int(len(predictions)*0.9)]
    ages = ages[0:int(len(ages) * 0.9)]
    net_worths = net_worths[0:int(len(net_worths) * 0.9)]
    #x-y : for x,y in abs(net_worths, predictions)
    error = abs(numpy.array(net_worths)-numpy.array(predictions))
    cleaned_data = list(zip(ages, net_worths, error))

    print("test")
    
    return cleaned_data

