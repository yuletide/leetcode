/**
 * @param {string} s
 * @return {boolean}
 */
const reverse = (s) => {
    const reverse = s.split("").reverse().join(""); 
    return reverse;
}
var isPalindrome = function(s) {
    const lower = s.toLowerCase();
    //console.log(lower);
    const removed = lower.replaceAll(/[^a-z0-9]/g, '');
    //console.log(removed);
    if (removed === "") return true;
    //console.log(reverse(removed))
    return removed === reverse(removed)
};