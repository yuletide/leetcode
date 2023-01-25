/**
 * @param {character[][]} board
 * @return {boolean}
 */
// this is gross but it works
const hashArray = ()=>{
    return [...Array(9)].map(()=>{return {}})
}
var isValidSudoku = function(board) {
    const rows = hashArray();
    const cols = hashArray();
    const nw = {};
    const n = {};
    const ne = {};
    const w = {};
    const c = {};
    const e = {};
    const sw = {};
    const s = {};
    const se = {};
    
    for (let i = 0; i<board.length; i++){
        // console.log("row",i);
        for (let j = 0; j<board[0].length; j++){
            // console.log("column", j)
            const cell = board[i][j];
            if (cell === ".") continue;
            // console.log(cell);
            // check if is in row or col
            if (rows[i][cell]) {
                // console.log("found in rows", rows[i][cell]);
                return false
            } else {
                rows[i][cell] = true;
            }
            
            if (cols[j][cell]) {
                // console.log("found in col", cols[j][cell]);
                return false
            } else {
                cols[j][cell] = true;
            }

            if (i < 3){
                if (j < 3){
                // NW
                    if (nw[cell]) return false;
                    nw[cell] = true;
                } else if (j >= 3 && j < 6){
                    if (n[cell]) return false;
                    n[cell] = true;
                } else if (j >= 6){
                    if (ne[cell]) return false;
                    ne[cell] = true;
                }

            } else if (i >= 3 && i < 6){
                if (j < 3){
                // NW
                    if (w[cell]) return false;
                    w[cell] = true;
                } else if (j >= 3 && j < 6){
                    if (c[cell]) return false;
                    c[cell] = true;
                } else if (j >= 6){
                    if (e[cell]) return false;
                    e[cell] = true;
                }
            } else {
                // south
                if (j < 3){
                // SW
                    if (sw[cell]) return false;
                    sw[cell] = true;
                } else if (j >= 3 && j < 6){
                    if (s[cell]) return false;
                    s[cell] = true;
                } else if (j >= 6){
                    if (se[cell]) return false;
                    se[cell] = true;
                }
            }
            
        }
    }
    return true;

};