/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    let maxDistanceSoFar = 0;
    function computeLongestPath(node) {
        let longestPath = 0;
        if(!node.left && !node.right) {
            //node.longestPath = 0;
            return 0;
        }
        let a=0,b=0;
        if(node.left) {
            a = 1 + computeLongestPath(node.left);
        }
        if(node.right) {
            b = 1 + computeLongestPath(node.right);
        }
        maxDistanceSoFar = Math.max(a + b, maxDistanceSoFar)
        longestPath = Math.max(a, b);
        //console.log(node.val, maxDistanceSoFar, longestPath);
        return longestPath;
    }
    computeLongestPath(root);
    return maxDistanceSoFar;
};