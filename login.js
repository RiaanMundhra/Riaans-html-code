function validate(e) {

    e.preventDefault();

    var email = document.getElementById('email').value;

    var password = document.getElementById('password').value;

    var age = document.getElementById('age').value;

    var msg = document.getElementById('message');

    if (email == '') {

        message = 'Email is required';

        msg.style.color = 'red';

    }

    else if (password == '') {

        message = 'Password is required';

        msg.style.color = 'red';

    }

    else if (age == '') {

        message = 'Age is required';

        msg.style.color = 'red';

    }

    else {

        message = 'Form Submitted';

        msg.style.color = 'green';

    }

    msg.innerText = message;

}