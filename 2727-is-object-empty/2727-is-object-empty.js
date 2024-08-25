/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {

    // 배열인 경우
    if (Array.isArray(obj)) {
        return obj.length === 0
    }
    // 객체인 경우
    return Object.keys(obj).length === 0
};