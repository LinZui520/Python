package com.example.entity;

import lombok.Data;

@Data
public class ApiResult<T> {
    private int code;
    private String message;
    private T data;

    public ApiResult(int code,String message,T data){
        this.code=code;
        this.message = message;
        this.data = data;
    }

}
