/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Faster O(n) Solution
var twoSum = function(nums, target) {
  let hash = new Map();
  for (const [i, num] of nums.entries()){
    //   console.log(num,i);
      const complement = target-num;
    //   console.log("complement", complement);
      if (hash.has(complement)){
          return [hash.get(complement), i]
      }
    hash.set(num, i);
  }
};

// First attempt, slower solution because of indexOf making it closer to O(n2)
// var twoSum = function(nums, target) {
//   let solution = []
//   for (const [i, num] of nums.entries()){
//       //console.log(num,i)
//       const complement = target-num;
//       //console.log("complement", complement)
//       const complementIndex = nums.indexOf(complement, i+1);
//       //console.log('complement index', complementIndex);
//       if (complementIndex > -1) return [i, complementIndex];
//   }
// };