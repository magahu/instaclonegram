function EnableButton(){

    //debugger;

    let my_input = document.querySelector('#text-input').value;
    let my_div = document.getElementById('text-div');
    let submit_button = document.querySelector('#submit-button');

    console.log(my_input);
    //my_input.textLength

    if (my_input !== '') {
        submit_button.disabled = false;
        submit_button.hidden = false;
        my_div.hidden = true

    } else {
        submit_button.disabled = true;
        submit_button.hidden = true
        my_div.hidden = false
    }
}