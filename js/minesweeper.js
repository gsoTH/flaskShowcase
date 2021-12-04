var arrBombs;
var arrClicked;
var limitBombs;
const arrX = 9; //number of fields
const arrY = 9;
const dimensionX =400;
const dimensionY =400;
const spaceX = Math.floor(dimensionX / arrX); //widht of each square
const spaceY = Math.floor(dimensionY / arrY); //heigth of each square

function fillArray(){
    //Array of 9x9 fields
    initializeArrays();
    //fill arr with random bombs
    var numberBombs = 0;
    
    while(numberBombs < limitBombs){
        var x = Math.floor(Math.random() * (arrX));
        var y = Math.floor(Math.random() * (arrY));
        
        if(arrBombs[y][x] == false){
            arrBombs[y][x] = true;
            numberBombs++;
        }
    }

    //console.log(arr);
    //console.log(arrClicked);

    function initializeArrays() {
        arrBombs = [
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
        ];
        arrClicked = [
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
            [false, false, false, false, false, false, false, false, false],
        ];
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

    function drawButtons() {
        for (var y = 0; y < arrY; y++) {
            for (var x = 0; x < arrX; x++) {
                if (arrClicked[y][x] == false) {
                    //5 = radius --> rounded corners
                    rect(x * spaceX, y * spaceY, spaceX, spaceY, 5);
                    fill(120);
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
    for (var y = 0; y < arrY; y++) 
    {
        for (var x = 0; x < arrX; x++) 
        {
            if(mouseX >= x*spaceX && mouseX < (x+1)*spaceX){
                if(mouseY >= y*spaceY && mouseY < (y+1)*spaceY){
                    arrClicked[y][x] = true;
                }
            }
        }
    }
  }