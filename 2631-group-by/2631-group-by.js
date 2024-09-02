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



/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */


// fn: 함수. 기준이 됨. 
// fn에 넣었을 때의 결과에 따라 group으로 묶음.