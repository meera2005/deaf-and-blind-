
      function openWindow() {
        document.getElementById("myWindow").style.display = "block";
      }

      function closeWindow(event) {
        var window = document.getElementById("myWindow");
        if (event.target != window && event.target.parentNode != window) {
          window.style.display = "none";
        }
      }

      function submitForm() {
        var name = document.getElementById("inputName").value;
        var email = document.getElementById("inputEmail").value;
        // do something with the values
        console.log("Name: " + name + ", Email: " + email);
        document.getElementById("myWindow").style.display = "none";
      }
      function openPdf(){
        document.getElementById("myPdf").style.display="block"
      }

      function closePdf(event) {
        var window = document.getElementById("myPdf");
        if (event.target != window && event.target.parentNode != window) {
          window.style.display = "none";
        }
      }
