<img width="1317" alt="image" src="https://github.com/user-attachments/assets/ff7aa231-5e6d-48de-9a2b-43a9c12b814e">



<h3> 🎨 이미지 변환 및 NFT metadata 생성 서비스, NFTLIX-AI </h3>   

- 이미지 만화화 API   
- 이미지 흑백화 API   
- 이미지 누끼 제작 API   
- 이미지 nft metadata 생성 API 


## 🔗 Download (Docker image)
```bash
docker pull ghcr.io/nftlix/nftlix-ai:0.1
```

## 🪄 Usage
```bash
docker run -p 8000:8000 \
  -e AWS_ACCESS_KEY=your-aws-access-key \
  -e AWS_SECRET_KEY=your-aws-secret-key \
  -e AWS_S3_IMAGE_BUCKET=your-aws-s3-image-bucket \
  -e AWS_S3_METADATA_BUCKET=your-aws-s3-metadata-bucket \
  -e BLACK_AND_WHITE_DIR=your-aws-s3-black-and-white-dir \
  -e CARTOONIZATION_DIR=your-aws-s3-cartoonization-dir \
  -e NUKKI_DIR=your-aws-s3-nukki-dir \
  nftlix-ai
```

## 🧩 System Architecture
![ai architecture](https://github.com/user-attachments/assets/98cabeb1-18dc-4f38-81d8-15043c23aa92)
