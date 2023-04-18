package com.example.serviceimpl;

import com.example.entity.User;
import com.example.mapper.UserMapper;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;

    @Autowired
    public UserServiceImpl(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    public void addUser(User user){
        userMapper.addUser(user);
    }

    public void updateUser(User user){
        userMapper.updateUser(user);
    }

    public User getUser(String userName){
        return userMapper.getUser(userName);
    }

    public void deleteUser(String userName){
        userMapper.deleteUser(userName);
    }
}
