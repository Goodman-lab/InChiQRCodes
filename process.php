<?php
if ($_POST['InChiCode']) {
    $code = $_POST['InChiCode'];

    //Regex schema for the InChi key - reports errors helpfully, and also prevents
    //security issues by severly restricting the valid input domain (need ^ and $
    //to anchor to the entire string)
    $InChiSchema = "/^[A-Z]{14}\-[A-Z]{10}\-[A-Z]$/";

    if (preg_match($InChiSchema, $code)) {
        $escapedCode = escapeshellarg($code);

        //If this isn't the raw posted code plus quotation marks,
        //something malicious is going on, so redirect to the error page
        $expectedEscapedCode = "'" . $code . "'";
        if ($expectedEscapedCode != $escapedCode) {
            header("Location: ./error.html");
            exit();
        }


        //Run the script to generate the QR code
        //$safeCommand = "python3 test.py " . $escapedCode;
        $safeCommand = "python3 makeQrCode.py " . $escapedCode;
        exec($safeCommand);

        //Redirect to the image file generated by the script
        //header("Location: ./qr/" . $code . ".txt");
        header("Location: ./qr/" . $code . ".png");
        exit();

    } else {
        //The code is of an invalid schema, so redirect to the error page
        header("Location: ./error.html");
        exit();
    }

} else {
    //The code field isn't set, so redirect to the error page
    header("Location: ./error.html");
    exit();
}
?>
