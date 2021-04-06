<?php

require_once 'config.php';

$charactersCollection = $db->characters;
$charactersCollection->insertOne([
	'name' => "JOINTS21{regex_wangy_wangy}"
]);