<?php
include_once ( "./common/common.php" );
try {
    main();
} catch (Exception $e) {
    echo $e;
}

function main(){
    //ユーザデータ一覧を取得
    $user_data = user_data::get_userdata();


    //クッキーからログイン状態を判別
    $params = array(
        'LOGINF' => '1',
        'user_data' => common::user_auth()
    );
    //templateを指定
    $template = './template/index.html';
    $contents = common::html_output($template,$params);
    

    //指定した内容を出力
    echo $contents;
}
