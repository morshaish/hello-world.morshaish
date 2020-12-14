/*function checkEmail(email){
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function Validate(email) {
        if(checkEmail(email)==false) {
            window.alert("Email is valid!");
        }
        else {
            window.alert("Email is not valid, please try again");
        }  

    }

function greet(name) {
 //   var x= `thank you${name}`;
   window.alert(name);
}
*/
function mouseOverMail() {
    document.getElementById("addMail").innerHTML="shmor1994@gmail.com";
  }

  function mouseOverPhone() {
      document.getElementById("addPhone").innerHTML="050-9006495";
    }

    function mouseOverlinkedin() {
        document.getElementById("addLinkedin").innerHTML="See My Linkedin Profile";
      }

      function mouseOverCV() {
        document.getElementById("addCV").innerHTML="Download My CV";
      }