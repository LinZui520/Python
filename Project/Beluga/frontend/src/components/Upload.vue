<script setup lang="ts">
  import { ref } from 'vue'
  import type { UploadInstance } from 'element-plus'

  const uploadRef = ref<typeof UploadInstance>()
  let url=ref('')

  const submitUpload = () => {
    uploadRef.value!.submit()
  }

  const sub = (res:any) => {
    console.log(res)
    url.value=res
  }
  
  
  
</script>

<template>
  <el-upload
    ref="uploadRef"
    class="upload-demo"
    action="/api/image/upload"
    :auto-upload="false"
    :on-success="sub"
  >
    <template #trigger>
      <el-button type="primary">select file</el-button>
    </template>

    <el-button class="ml-3" type="success" @click="submitUpload">
      upload to server
    </el-button>

    <template #tip>
      <div class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </template>
  </el-upload>
  <img :src="url">
</template>

<style scoped>

</style>