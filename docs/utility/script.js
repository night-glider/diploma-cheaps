const bck = document.getElementById("dynamic-background");

var mouse_pos = null
var x = 0
var y = 0


requestAnimationFrame(move_background);

function lerp (start, end, amt) {
  return (1-amt)*start+amt*end
}

onmousemove = (e) => { 
  mouse_pos = e
  
};

function move_background() {
  requestAnimationFrame(move_background);
  if( mouse_pos == null) {
    return
  }
  
  x = lerp(x, mouse_pos.clientX*0.05, 0.05)
  y = lerp(y, mouse_pos.clientY*0.05, 0.05)
  bck.style.left = `${x-100}px`
  bck.style.top = `${y-100}px`

  
}