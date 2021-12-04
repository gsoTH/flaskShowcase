var arrBombs;
var arrClicked;
var limitBombs;
var arrHints; //contains numbers of surrounding bombs
const arrX = 9; //number of fields
const arrY = 9;
const totalNumberOfFields = arrX * arrY;
const dimensionX =400;
const dimensionY =400;
const spaceX = Math.floor(dimensionX / arrX); //widht of each square
const spaceY = Math.floor(dimensionY / arrY); //heigth of each square
var boom;
var won;
var explosionRadius;
var explosionX;
var explosionY;

function fillArray(){

    initializeArrays();

    createBombs();

    createHints();


    function createHints(){
        for(let y = 0; y < arrY; y++){
            for(let x = 0; x < arrX; x++){
                let numberOfNeighbouringBombs = 0;

                //if-statements prohibit index-errors.
                //try-catch would be more readable.
                if(x > 0){
            
                    //left
                    if(arrBombs[y][x-1]){
                        numberOfNeighbouringBombs++;
                    }
        
                    //top left
                    if(y > 0){
                        if(arrBombs[y-1][x-1]){
                            numberOfNeighbouringBombs++;
                        } 
                    }
        
                    //bottom left
                    if(y < arrY-1){
                        if(arrBombs[y+1][x-1]){
                            numberOfNeighbouringBombs++;
                        } 
                    }
                }
        
                
                if(x < arrX-1){
                    //right
                    if(arrBombs[y][x+1]){
                        numberOfNeighbouringBombs++;
                    }
        
                    //top right
                    if(y > 0){
                        if(arrBombs[y-1][x+1]){
                            numberOfNeighbouringBombs++;
                        } 
                    }
        
                    //bottom right
                    if(y < arrY-1){
                        if(arrBombs[y+1][x+1]){
                            numberOfNeighbouringBombs++;
                        } 
                    }
                }
        
                //top
                if(y > 0){
                    if(arrBombs[y-1][x]){
                        numberOfNeighbouringBombs++;
                    } 
                }
        
                //bottom
                if(y < arrY-1){
                    if(arrBombs[y+1][x]){
                        numberOfNeighbouringBombs++;
                    } 
                }
        
                arrHints[y][x] = numberOfNeighbouringBombs; 
            }
            
        }
    }


    function createBombs() {
        var numberBombs = 0;

        while (numberBombs < limitBombs) {
            var x = Math.floor(Math.random() * (arrX));
            var y = Math.floor(Math.random() * (arrY));

            if (arrBombs[y][x] == false) {
                arrBombs[y][x] = true;
                numberBombs++;
            }
        }
    }

    /**
     * Creates nested arrays.
     * 
     * js implements multidimensional arrays as nested arrays (array of arrays).
     * Therefore we have to initalize each row seperately.
     */
    function initializeArrays() {
        arrBombs = new Array(arrY);
        arrClicked = new Array(arrY);
        arrHints = new Array(arrY);

        for(let y = 0; y < arrY; y++){
            arrBombs[y] = new Array(arrX);
            arrClicked[y] = new Array(arrX);
            arrHints[y] = new Array(arrX);
            
            for(let x = 0; x < arrX; x++){
                arrBombs[y][x] = false;
                arrClicked[y][x] = false;
            }
        }
       
    }
}

function setup() {
    
    reset();

    createCanvas(dimensionX, dimensionY);
}

function reset() {
    boom = false;
    won = false;
    explosionRadius = 0;
    explosionX = -1;
    explosionY = -1;

    limitBombs= arrX + Math.floor(Math.random() * (arrY));
    fillArray();
}

function draw() {
    
    clear()
    drawButtons();
    drawGrid();
    drawExplosion();

    function drawExplosion() {
        if(boom == true){
            centerX = explosionX*spaceX + spaceX/2;
            centerY = explosionY*spaceY + spaceY/2;

            fill(250, 0, 0, 255-(explosionRadius/2));
            circle(centerX, centerY, explosionRadius);
            explosionRadius++;

            if(explosionRadius > dimensionX){
                reset();
            }
            
        }
    }

    function drawButtons() {
        let numberOfClickedFields = 0;
        for (var y = 0; y < arrY; y++) {
            for (var x = 0; x < arrX; x++) {
                if (arrClicked[y][x] == false) {
                    
                    //Standard colour == gray
                    fill(120);

                    //greenish for secured bombs
                    if(won == true){
                        fill(0,150,50);
                    }

                    //red for unexploded bombs
                    if(boom == true){
                        if(arrBombs[y][x] == true){
                            fill(200, 0, 0);
                        }    
                    }

                    //5 = radius --> rounded corners
                    rect(x * spaceX, y * spaceY, spaceX, spaceY, 5);
                } else {
                    numberOfClickedFields++;

                    if(arrBombs[y][x] == false){
                        fill(120);
                        textSize(32);
                        textAlign(CENTER, CENTER);
                        if(arrHints[y][x] != 0){
                            text(arrHints[y][x], x * spaceX + spaceX/2, y * spaceY + spaceY/2);
                        }
                    }
                }

                if((totalNumberOfFields-numberOfClickedFields) == limitBombs){
                    won = true;
                }

            }
        }
    }

    function drawGrid() {
        let maxX = spaceX * arrX;
        let maxY = spaceY * arrY;
        
        line(0, 0, maxX, 0);
        line(0, 0, 0, maxY);
        line(maxX, 0, maxX, maxY);
        line(0, maxY, maxX, maxY);

        for (var y = 0; y < arrY; y++) {
            for (var x = 0; x < arrX; x++) {
                line(x * spaceX, 0, x * spaceX, maxY);
                line(0, y * spaceY, maxX, y * spaceY);
            }
        }

        stroke(200)
    }

}

function mouseClicked() {

    if(boom == false){ //no interaction after misslick
        for (var y = 0; y < arrY; y++) 
        {
            for (var x = 0; x < arrX; x++) 
            {
                if(mouseX >= x*spaceX && mouseX < (x+1)*spaceX){
                    if(mouseY >= y*spaceY && mouseY < (y+1)*spaceY){
                        
                        if(arrBombs[y][x] == true){
                            boom = true;
                            
                            //save current position to animate explosion
                            explosionX = x;
                            explosionY = y;
                        
                        } else {
                            arrClicked[y][x] = true;

                            if(arrHints[y][x] == 0){
                                discoverNeihgbours(y, x);
    
                            }
                        }

                    }
                }
            }
        }
    }
  }

  /**
   * Uncovers surrounding fields by marking them as clicked.
   * 
   * If sourrounding contains fields where hints == 0, function will
   * call itself for those fields. 
   * @param {int} y
   * @param {int} x 
   */
  function discoverNeihgbours(y, x){
      for(let j = y-1; j<=y+1; j++){
          for(let i = x-1; i<=x+1; i++){
                try{
                    
                    if(arrHints[j][i] == 0){
                        if(arrClicked[j][i] == false){
                            arrClicked[j][i] = true;
                            //discover even more Neighbours
                            discoverNeihgbours(j, i);
                        }
                    }

                    arrClicked[j][i] = true;
                } catch (e){
                    //ignore array-index-errors
                }
              }
          }
  }
