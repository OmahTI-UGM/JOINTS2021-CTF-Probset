<?php

$password = "8682a65aa7f080e0d8511018a9f64d77";
if ($_GET['p'] === $password) {
    $token = "eyJhY2Nlc3NfdG9rZW4iOiAiWU93Z1VsWW1TcHpCQXBOeWVwY2dpTzJCR0JDa3ptIiwgImV4cGlyZXNfaW4iOiA2MDQ4MDAsICJyZWZyZXNoX3Rva2VuIjogIjJKSW9hWXNxVkpPNHFCeUYwbmtOdjJCbFprYWFkTyIsICJzY29wZSI6ICJpZGVudGlmeSBtZXNzYWdlcy5yZWFkIGd1aWxkcyIsICJ0b2tlbl90eXBlIjogIkJlYXJlciJ9";
    setcookie('token', $token, time() + 604800, "/", null, null, true);
    $_COOKIE['token'] = $token;

    header('Location: /index.php');
} else {
    header('Location: /index.php');
}