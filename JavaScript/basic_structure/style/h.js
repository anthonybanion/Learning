/*Brief: This is a simple JavaScript file that changes the style of the HTML elements.
 *Details: Using the querySelector method.
 *Date: 03/08/2024
 *Version: 1.0*/


function insertText(elemnt, text){
    document.querySelector(elemnt).innerHTML = text;
}
insertText("h1", "Hello World");
insertText("p", "Enter a value");

let elemnt = document.querySelector("h1");  // by tag name
elemnt.style.color = "red";
elemnt.style.backgroundColor = "orange";
elemnt.style.fontSize = "40px";
elemnt.style.padding = "20px";
elemnt.style.border = "2px solid black";
elemnt.style.borderRadius = "10px";
elemnt.style.textAlign = "center";
elemnt.style.fontFamily = "Arial, sans-serif";

let elemnt2 = document.querySelector("#paragraph");  // by id
elemnt2.style.color = "blue";
elemnt2.style.backgroundColor = "lightblue";
elemnt2.style.fontSize = "20px";
elemnt2.style.padding = "10px";
elemnt2.style.border = "2px solid red";
elemnt2.style.borderRadius = "10px";
elemnt2.style.textAlign = "center";
elemnt2.style.fontFamily = "Arial, sans-serif";
elemnt2.style.margin = "10px";

let elemnt3 = document.querySelector(".container");  // by class
elemnt3.style.color = "green";
elemnt3.style.backgroundColor = "lightgray";
elemnt3.style.fontSize = "30px";
elemnt3.style.padding = "15px";
elemnt3.style.border = "2px solid green";
elemnt3.style.borderRadius = "10px";
elemnt3.style.textAlign = "center";
elemnt3.style.fontFamily = "Arial, sans-serif";
elemnt3.style.margin = "10px";

/*  HTML file
<body>
    <div class="container">
    <h1></h1>
    <p></p>
    </div>
    <script src="./JavaScript/basic_structure/style/h.js">  </script>
</body>
*/