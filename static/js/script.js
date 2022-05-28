// Acquire each rating star by assigning a variable to all
const one = document.getElementById('first');
const two = document.getElementById('second');
const three = document.getElementById('third');
const four = document.getElementById('fourth');
const five = document.getElementById('fifth');

// Acquire add review form
const form = document.querySelector('.add-review');

// For each rating star, add/remove 'checked' class
const handleSelect = (selection) => {
    switch(selection) {
        case 'first': {
            one.classList.add('checked');
            two.classList.remove('checked');
            three.classList.remove('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'second': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.remove('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'third': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'fourth': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.add('checked');
            five.classList.remove('checked');
            return;
        }
        case 'fifth': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.add('checked');
            five.classList.add('checked');
            return;
        }
    }
};

// Acquire numeric value from each string value
const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1;
    } else if (stringValue === 'second') {
        numericValue = 2;
    } else if (stringValue === 'third') {
        numericValue = 3;
    } else if (stringValue === 'fourth') {
        numericValue = 4;
    } else if (stringValue === 'fifth') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
};

// Assign variable to all star ratings
const arr = [one, two, three, four, five];

// Add click event listener on each star rating
arr.forEach(item => item.addEventListener('click', (event) => {
    handleSelect(event.target.id);
}));

// Add numeric value to each star rating within the event listener
arr.forEach(item => item.addEventListener('click', (event) => {
    const val = event.target.id;
    const val_num = getNumericValue(val);
    form.ratings.value = val_num;
}));
