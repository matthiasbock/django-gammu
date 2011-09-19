function FadeIn(id, opacity) {
	document.getElementById(id).style.opacity = opacity;
	document.getElementById(id).style.visibility = 'visible';
	if ( opacity < 1 ) {
		opacity = opacity + 0.15
		window.setTimeout("FadeIn('"+id+"', "+opacity+");", 50);
		}
	}

function FadeOut(id, opacity) {
	document.getElementById(id).style.opacity = opacity;
	if ( opacity > 0 ) {
		opacity = opacity - 0.15
		window.setTimeout("FadeOut('"+id+"', "+opacity+");", 40);
		}
	else {
		document.getElementById(id).style.visibility = 'hidden';
		}
	}

