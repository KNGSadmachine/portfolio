<?php
include_once ( "./common/user_data.php" );
include_once ( "./common/common.php" );
try {
    main();
} catch (Exception $e) {
    echo $e;
}

function main() {

    //クッキー解除
    setcookie("ID", ''    , time() - 1800);
	setcookie("EMAIL", ''    , time() - 1800);

    //ログインページへリダイレクト
	header("Location:/login.php");
    exit();

}
