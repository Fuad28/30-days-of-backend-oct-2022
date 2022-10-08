function BoO(word){
    //Checks if a word contains special characters or a space.

    let special_chars= /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

    if ((typeof(word) !== 'string') || (special_chars.test(word)))
        console.log('Please remove all spaces or special characters');

    else if (['bolu', 'odun'].includes(word.toLowerCase()))
        console.log(`Welcome back, ${word}`);

    else {console.log(`It is nice to meet you, ${word}`)}
        
};

//Tests
BoO('Micheal Jackson');
BoO('Micheal');
BoO('Bolu');

