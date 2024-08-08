type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let resetValue = init;
    return {
        increment: function() {
            return ++init;
        },
        decrement: function() {
            return --init;
        },
        reset: function() {
            init = resetValue;
            return init;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */