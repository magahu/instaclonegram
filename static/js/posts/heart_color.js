function ChangeHeart(){
    heart = document.getElementById('heart-button')
    black_heart = document.getElementById('black-heart')
    red_heart = document.getElementById('red-heart')

    if (black_heart.hidden == false){
        red_heart.hidden = false
        black_heart.hidden = true
    }else 
    if(black_heart.hidden == true){
        red_heart.hidden = true
        black_heart.hidden = false
    }

}