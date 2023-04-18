package com.example.controller;

import com.example.entity.User;
import com.example.serviceimpl.UserServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;



@RestController
@RequestMapping("/api/user")
public class UserController {

    private final UserServiceImpl userService;

    @Autowired
    public UserController(UserServiceImpl userService){
        this.userService=userService;
    }


    @PostMapping ("/add")
    public void addUser(@RequestBody User user){
        userService.addUser(user);
    }

    @PostMapping("/update")
    public void updateUser(@RequestBody User user){
        userService.updateUser(user);
    }

    @GetMapping("/get/{userName}")
    public User getUser(@PathVariable("userName")String userName){
        return userService.getUser(userName);
    }

    @DeleteMapping("/delete/{userName}")
    public void deleteUser(@PathVariable("userName")String userName){
        userService.deleteUser(userName);
    }



}