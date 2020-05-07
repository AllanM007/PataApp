mapboxgl.accessToken = 'pk.eyJ1IjoiYWxsYW5tIiwiYSI6ImNrMTkybTB1bTAwNGszZ3F6M3JoZTM5Y2gifQ.EsrJ4zAtt4bpXFxnAVi1dw';

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/allanm/ck299v8du0mjs1cnxggqnxk2h',
  center: [0],
  zoom: 5
});

map.addControl(new mapboxgl.NavigationControl());
