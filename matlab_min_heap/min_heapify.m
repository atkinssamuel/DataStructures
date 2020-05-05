function [array] = min_heapify(array, index, N)
    left = 2 * index;
    right = 2 * index + 1;
    
    minimum = index;
    
    if left <= N && array(left) < array(minimum)
       minimum = left; 
    end
    
    if right <= N && array(right) < array(minimum)
       minimum = right; 
    end
    
    if index ~= minimum
        temp = array(index);
        array(index) = array(minimum);
        array(minimum) = temp;
        array = min_heapify(array, minimum, N);
    end
end

