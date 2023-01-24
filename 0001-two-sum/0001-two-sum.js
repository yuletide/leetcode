/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  // brute force:
  let solution = []
  for (const [i, num] of nums.entries()){
      //console.log(num,i)
      const complement = target-num;
      //console.log("complement", complement)
      const complementIndex = nums.indexOf(complement, i+1);
      //console.log('complement index', complementIndex);
      if (complementIndex > -1) return [i, complementIndex];
  }
};