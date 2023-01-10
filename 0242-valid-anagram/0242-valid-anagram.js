/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let sHash = {}
    let tHash = {}
    
    if (s==t){
        return true
    }
    
    if (s.length !== t.length){
        return false
    }
    
    // build some hashes
    s.split("").forEach(c=>{
        sHash[c] = sHash[c] ? sHash[c]+1 : 1
    })
    t.split("").forEach(c=>{
        tHash[c] = tHash[c] ? tHash[c]+1 : 1
    })
    
    console.log(sHash, tHash)
    // theres probably a nicer way to check hash equality
    for (key of Object.keys(sHash)){
        if (sHash[key] !== tHash[key]){
            return false
        }
    }
    return true
};