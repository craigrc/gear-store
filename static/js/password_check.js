
    function checkPassword(password) {
        const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
        return regex.test(password);
    }

  function process_login(thisform) {
    var form = document.getElementById(thisform)
    var password = document.getElementById('password').value;
    if (checkPassword(password)) {
      form.submit()
    } else {
      alert('Invalid password! Please enter a password with 8 or more digits, one uppercase character and one lowercase character.');
    }
  }