def best_position(points, weights):
    '''
    points: List of tuples, each tuple contains two float elements corresponds to the x and y location of a point.
    weights: List of floats.
    
    Return: a tuple (x,y) that represents the location of the point that minimizes the weighted distance sum.
    '''

    from random import randint

    def wm_partition(values, weights, k):
        if len(values) == 1:
            return values[0]

        pivot_index = randint(0, len(values) - 1)
        pivot_value = values[pivot_index]

        left_values, left_weights = [], []
        right_values, right_weights = [], []
    
        for i in range(len(values)):
            
            if values[i] < pivot_value:
                left_values.append(values[i])
                left_weights.append(weights[i])
            else:
                right_values.append(values[i])
                right_weights.append(weights[i])
    
        sum_left_weights = sum(left_weights)

        # Recursively select the partition with the weighted mean
        if sum_left_weights > k:
            return wm_partition(left_values, left_weights, k)
        elif sum_left_weights < k:
            return wm_partition(right_values, right_weights, k - sum_left_weights)
        else:
            return pivot_value
    
    def weighted_median(vals, weights):
        k = sum(weights) / 2 # since total weight == 1, this will be 0.5
        return wm_partition(vals, weights, k)
        

    assert sum(weights) == 1.0

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    w_x_med = weighted_median(x, weights)
    w_y_med = weighted_median(y, weights)
    
    return w_x_med, w_y_med