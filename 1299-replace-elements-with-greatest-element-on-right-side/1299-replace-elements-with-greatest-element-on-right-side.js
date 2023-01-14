/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {

    if (arr.length == 1) return [-1];

    let returned = [arr[arr.length-1],-1];
    let last = returned[0];
    for (let i = arr.length-2; i>0; i--){
        //console.log(arr[i], i)
        if (arr[i]>last){
            returned.unshift(arr[i])
            last = arr[i];
        } else{
            returned.unshift(last);
        }
        // returned.unshift()
    }
    return returned
    
};