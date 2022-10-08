function fibonacci(){
    // prints the first 100 fibonacci numbers
    fibbArr= [0, 1];

    for (let i=0; fibbArr.length <= 100; i++){
        fibbLength= fibbArr.length;
        nextFibb= fibbArr[fibbLength - 1] + fibbArr[fibbLength - 2];
        fibbArr.push(nextFibb);
    }
    console.log(fibbArr);

}

fibonacci();