function [array] = min_heap_insert(array, element, N)
    N = N + 1;
    array(N) = element;
    print_heap(array);
    parent = floor(N/2);
    current = N;
    while array(parent) > array(current)
        temp = array(parent);
        array(parent) = array(current);
        array(current) = temp;
        current = parent;
        parent = floor(current/2);
        if parent < 1
            return
        end
    end
end

