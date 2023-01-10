/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = 0;

    // optimization: if the current bar is shorter than a past one we can skip that inner loop
    // let maxHeight = 0;

    // for (let i = 0; i<height.length; i++){
    //     if (height[i] < maxHeight){
    //         break
    //     }
    //     maxHeight = height[i];
    
    //     for (let j = height.length-1; j<i; j--){
    //         // area = width * height of smaller bar
    //         // width = j-i
    //         // height = smaller of the two bars
            
    //         const smallerWall = height[i] < height[j] ? height[i] : height[j];
    //         const area = (j-i)*smallerWall;
    //         maxArea = Math.max(maxArea, area);
            
    //         //console.log(`Checking ${i}, ${j}: ${height[i]}, ${height[j]}, smaller ${smallerWall}, area ${area}`);
    //     }
    // }

    let l = 0;
    let r = height.length-1;
    while (l<r){
        const area = (r-l)*Math.min(height[l], height[r]);
        maxArea = Math.max(maxArea, area)
        //console.log(`${l}, ${r}: ${height[l]}, ${height[r]}: ${area}`)
        if (height[l] < height[r]){
            l++
        } else {
            r--
        }
    }
    return maxArea;
};