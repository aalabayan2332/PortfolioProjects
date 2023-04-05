<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$name = $_POST["name"];
	$email = $_POST["email"];
	$message = $_POST["message"];

	$to = "youremail@example.com"; // Replace with your own email address
	$subject = "New message from your website";
	$body = "Name: $name\nEmail: $email\nMessage:\n$message";

	if (mail($to, $subject, $body)) {
		header("Location: thankyou.html"); // Redirect to thank you page
		exit;
	} else {
		echo "Sorry, there was a problem sending your message.";
	}
}
?>
