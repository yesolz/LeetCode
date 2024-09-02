/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    
    const grouped = {}

    for (let i of this) {
        const key = fn(i)

        if (grouped[key]) {
            grouped[key].push(i)
        } else {
            grouped[key] = [i]
        }
    }

    return grouped

};
