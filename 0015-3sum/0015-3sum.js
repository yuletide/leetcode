/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const answer = []; //new Set();
    // edge/simple case
    if (nums.length === 3){
        if (nums[0]+nums[1]+nums[2] === 0) return [nums];
        return [];
    }
    nums.sort((a,b)=>a-b);
    //console.log(nums)
    for (const [i, n] of nums.entries()){
        // first item
        //console.log("anchoring", n);

        //skip duplicate anchors
        if (i>0 && nums[i] === nums[i-1]) {
            //console.log("same as last anchor skipping");
            continue;
        };

        let l = i+1;
        let r = nums.length-1;
        while(l<r){
            const sum = n+nums[l]+nums[r];
            //console.log(`3 digits: ${n} ${nums[l]} ${nums[r]} Sum: ${sum}`);
            if (sum<0){
                // too low, bump left side
                l++;
                while(nums[l] === nums[l-1] && l<r){
                    //console.log("skipping duplicate middle");
                    l++;
                }
            } else if (sum > 0) {
                r--;
            } else {
                //console.log("match found");
                const ans = [n, nums[l], nums[r]];
                //if (!JSON.stringify(answer).includes(JSON.stringify(ans))) { // js is dumb
                   // console.log("answer already there")
                answer.push(ans)
                //}
                l++;
                while(nums[l] === nums[l-1] && l<r){
                    //console.log("skipping duplicate middle");
                    l++;
                }
            }
        }

    }
    return answer;
    // start with l, then solve sorted twosum with remaining items
    
};