
function message(msg){
    document.getElementById('output').innerHTML = msg + "event";
}

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