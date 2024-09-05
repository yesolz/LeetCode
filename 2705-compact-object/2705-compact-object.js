/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {

    if (Array.isArray(obj)) {
        return obj.map(compactObject).filter(Boolean)
    }

    if (typeof obj === 'object' && obj !==null) {
        const newObj = {}
        for (let key in obj) {
            const value = compactObject(obj[key])
            if (Boolean(value)) {
                newObj[key] = value
            }
        }
        return newObj
    }

    return obj
};