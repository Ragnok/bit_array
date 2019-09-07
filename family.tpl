<!DOCTYPE html>
<html>
  <head>
    <title> {{lastname.title()}} Family </title>
</head>
  <body>
    <h1> The <em> {{lastname.title()}} </em> Family </h1>
    <hr>
    <ol>
      % for name in first_names:
      <li> {{name.title()}} </li>
      % end
    </ol>
</body>
</html>
