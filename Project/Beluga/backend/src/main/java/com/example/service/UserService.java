package com.example.service;

import com.example.entity.User;

public interface UserService {
    void addUser(User user);

    void updateUser(User user);

    User getUser(String userName);

    void deleteUser(String userName);

}
