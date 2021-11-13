<?php

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    file_put_contents('lead_error.log', json_encode($_POST) . "\n", FILE_APPEND);
    file_put_contents('lead_error.log', json_encode($_SERVER) . "\n", FILE_APPEND);
    die();
}

$_POST['url'] = $_SERVER['REQUEST_URI'];
$_POST['r_ip'] = $_SERVER['REMOTE_ADDR'];
$_POST['r_au'] = $_SERVER['HTTP_USER_AGENT'] ?? '';
$_POST['date'] = date('Y-m-d H:i:s');
file_put_contents('lead.log', json_encode($_POST) . "\n", FILE_APPEND);
