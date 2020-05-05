function [array, element] = min_heap_extract(array, N)
    element = array(1);
    array(1) = array(N);
    N = N - 1;
    array = min_heapify(array, 1, N);
end