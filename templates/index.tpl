<html>
  <head>
    <title>AnkiShow</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
  </head>
  <body>
    <div id="display">
        <div class='card' id="a">
          <h1 class="tpl"></h1>
          <h2 class="tpl">loading..</h2>
          <h3 class="tpl"></h3>
        </div>
        <div class='card' id="b">
          <h1 class="tpl"></h1>
          <h2 class="tpl">loading..</h2>
          <h3 class="tpl"></h3>
        </div>
    </div>
    <script type="text/javascript" src="http://code.jquery.com/jquery-2.2.4.min.js"></script>
    <script type="text/javascript" src="http://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
    <script type="text/javascript" src="{{url_for('static', filename='show.js')}}"></script>
  </body>
</html>
