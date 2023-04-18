package com.example.entity;


import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("user")
public class User {

    private String userName;
    private String passWord;
    private String email;
}
