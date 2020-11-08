<?php

class user_data {
    function get_userdata(){
        $params = array();
        define('DB_HOST','127.0.0.1');
        define('DB_NAME','auth_db');
        define('DB_USER','userK');
        define('DB_PASSWORD','pass');
    
        $options = array(PDO::MYSQL_ATTR_INIT_COMMAND=>"SET CHARACTER SET 'utf8'");

        error_reporting(E_ALL & ~E_NOTICE);
        try{
            $dbh = new PDO('mysql:host='.DB_HOST.';dbname='.DB_NAME, DB_USER, DB_PASSWORD,$options);
        } catch (PDOException $e) {
            echo $e->getMessage();
            exit;
        }
        
        $sql = 'SELECT * FROM users';
        $stmt = $dbh->query($sql);
        $params = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
        //var_dump($result);
        return $params;
    }
}
