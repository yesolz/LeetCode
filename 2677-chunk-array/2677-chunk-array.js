/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let chunked_arr = []
    for (let i=0; i<arr.length; i+=size){
        let chunk = arr.slice(i, i+size)
        chunked_arr.push(chunk)
    }
    return chunked_arr;
};
