var arrBombs;
var arrClicked;
var limitBombs;
const arrX = 9; //number of fields
const arrY = 9;
const dimensionX =400;
const dimensionY =400;
const spaceX = Math.floor(dimensionX / arrX); //widht of each square
const spaceY = Math.floor(dimensionY / arrY); //heigth of each square
var boom = false;
var explosionRadius = 0;
var explosionX = -1;
var explosionY = -1;

function fillArray(){

    initializeArrays();

    createBombs();


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

        for(let y = 0; y < arrY; y++){
            arrBombs[y] = new Array(arrX);
            arrClicked[y] = new Array(arrX);
            
            for(let x = 0; x < arrX; x++){
                arrBombs[y][x] = false;
                arrClicked[y][x] = false;
            }
        }
       
    }
}

function setup() {
    
    limitBombs= arrX + Math.floor(Math.random() * (arrY));
    fillArray();


    createCanvas(dimensionX, dimensionY);
    
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
            fill('red');
            circle(centerX, centerY, explosionRadius);
            explosionRadius++;
            
        }
    }

    function drawButtons() {
        for (var y = 0; y < arrY; y++) {
            for (var x = 0; x < arrX; x++) {
                if (arrClicked[y][x] == false) {
                    //5 = radius --> rounded corners
                    fill(120);
                    rect(x * spaceX, y * spaceY, spaceX, spaceY, 5);
                    
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
                        arrClicked[y][x] = true;

                        if(arrBombs[y][x] =true){
                            boom = true;
                            explosionX = x;
                            explosionY = y;
                        }
                    }
                }
            }
        }
    }

  }
