/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    
    const map = new Map();

    arr1.forEach(obj => {
        map.set(obj.id, obj);
    })

    arr2.forEach(obj => {
        if (map.has(obj.id)) {
            const merged = {...map.get(obj.id), ...obj}
            map.set(obj.id, merged)
        } else {
            map.set(obj.id, obj)
        }
    })

    const joinedArr = Array.from(map.values()).sort((a, b) => a.id - b.id);

    return joinedArr;

};