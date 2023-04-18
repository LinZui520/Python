package com.example.controller;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.util.Objects;
import java.util.UUID;

@RestController
@RequestMapping("/api/image")
public class PictureController {
    @Value("${file.upload.path}")
    private String path;


    @Value("${base.picture.url}")
    private String basePictureUrl;

    @PostMapping("/upload")
    public String uploadPicture(@RequestParam("file")MultipartFile file) {
        //获取文件名
        String name = file.getOriginalFilename();
        //获取文件后缀名
        name= Objects.requireNonNull(name).substring(name.lastIndexOf("."));

        //重新生成文件名
        name=UUID.randomUUID().toString().replace("-","")+name;
        try{
            file.transferTo(new File(path+"/"+name));
            System.out.println("上传成功");
        }catch (Exception e){
            System.out.println("上传失败");
        }

        return basePictureUrl+name;
    }


}
