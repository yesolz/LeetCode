/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    
    const recursive = (arr, depth) => {

        let result = [];

        for (let elem of arr) {
            if (Array.isArray(elem) && depth < n) {
                result.push(...recursive(elem, depth + 1))
            } else {
                result.push(elem)
            }
        }

        return result;
        
    }

    return recursive(arr, 0)
};

