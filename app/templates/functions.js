/* Funtions for Infographics gallery */
function upDate(previewPic){
    var src = previewPic.getAttribute( "src" );
    document.getElementById('image').style.backgroundImage = "url('" + src + "')";
    document.getElementById('image').innerHTML = previewPic.alt;
}

function unDo(){
    var text = "Hover over an image below to display here.";
    document.getElementById('image').style.backgroundImage = "url('')";
    document.getElementById('image').innerHTML= text;
}

/* Functions for Nav Menu */
/* Open */
function openNav() {
    document.getElementById("myNav").style.height = "100%";
  }
  
  /* Close */
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
  }