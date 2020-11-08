<?php
include_once ( "./common/user_data.php" );

class common {
    function html_output($template,$params=array()){
    
   //htmlを取り込む
    ob_start();
    require $template;
    $contents = ob_get_clean();
   
    //出力内容を返す
    return $contents;

    }
    function user_auth(){
        $user_data = user_data::get_userdata();
        $output = array();
        if(isset($_COOKIE["EMAIL"])){
            foreach($user_data as $key => $value){
                if($_COOKIE["EMAIL"] == $value["email"]){
                    $output = $value;
                    break;
                }
            }
        }
        return $output;
    }
}
