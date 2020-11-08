<?php
include_once ( "./common/common.php" );
try {
    main();
} catch (Exception $e) {
    echo $e;
}

function main(){
    $output = common::user_auth();
    if(!empty($output)){
        header("Location:/index.php");
    }

    //ユーザデータ一覧を取得
    $template = '';
    //ログイン失敗した場合の警告メッセージ表示するかどうかのフラグの設定
    $params = array(
        'LOGINF' => true,
        'user_data' => common::user_auth()
    );
   
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $user_data = user_data::get_userdata();
        $flag = 0;
        foreach($user_data as $key => $value){
           if($value["email"] == $_POST["email"] && $value["password"] == $_POST["password"]){
                $flag = 1;
                setcookie("ID", $_POST["ID"] , time()+(60*60*24*7) );
                setcookie("EMAIL", $_POST["email"] , time()+(60*60*24*7) );
                header("Location:/index.php");
                exit();
            }
        }
         $params["LOGINF"] = false;
    }
    
    //templateを指定
    $template = './template/login.html';
    $contents = common::html_output($template,$params);

    //指定した内容を出力
    echo $contents;
}
