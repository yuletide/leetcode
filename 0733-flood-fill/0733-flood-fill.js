/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, startRow, startCol, color) {
    //tags depth/breadth first search
    const initialColor = image[startRow][startCol];
    const height = image.length;
    const width = image[0].length;

    const changeColor = (row, col) => {
        if (image[row][col] === initialColor){
            // change color
            image[row][col] = color;

            if (row-1 >= 0){
                // go up
                changeColor(row-1, col)
            }

            if (row+1 < height){
                // go down
                changeColor(row+1, col)
            }

            if (col-1 >= 0){
                // go left
                changeColor(row, col-1)
            }

            if (col+1 < width){
                // go right
                changeColor(row, col+1)
            }
        }
    }

    if (initialColor === color) return image;
    changeColor(startRow, startCol);
    return image;

};