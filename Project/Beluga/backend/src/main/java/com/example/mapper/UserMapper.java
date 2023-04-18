package com.example.mapper;

import com.example.entity.User;
import org.apache.ibatis.annotations.*;


@Mapper
public interface UserMapper {

    @Insert("insert into user(userName,passWord,email) values(#{userName},#{passWord},#{email})")
    void addUser(User user);

    @Update("update user set passWord=#{passWord},email=#{email} where userName=#{userName}")
    void updateUser(User user);

    @Select("select * from user where userName=#{userName}")
    User getUser(String userName);

    @Delete("delete from user where userName=#{userName}")
    void deleteUser(String userName);
}
